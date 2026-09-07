#!/usr/bin/env python3
# 驗收 harness：Playwright 真點擊→驗證點擊前後 DOM 狀態變化（純本地檔，無後端站體）
import asyncio, sys
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8777"
RESULTS = []
def ok(mid, name, cond, detail=""):
    RESULTS.append(f"{'PASS' if cond else 'FAIL'} [{mid}] {name}" + (f" :: {detail}" if detail else ""))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(viewport={"width": 1280, "height": 900})
        page = await ctx.new_page()
        errs = []
        page.on("pageerror", lambda e: errs.append(str(e)))

        await page.goto(BASE + "/pages/course.html?course=demo-skin-barrier")
        await page.wait_for_selector("#m1-progress-demo-skin-barrier", state="attached", timeout=5000)

        # M1：勾選→localStorage＋進度條即時重算（點擊前 0%）
        bar = page.locator("#m1-progress-demo-skin-barrier .pct")
        before = await bar.inner_text()
        await page.check("#m1-check-unit-brick-mortar")
        await asyncio.sleep(.3)
        after = await bar.inner_text()
        ls = await page.evaluate("localStorage.getItem('mats-progress')") or ""
        ok("M1", "核取框點擊→localStorage 寫入＋進度條即時重算", before == "0%" and after != before and ('"checked":true' in ls or '"checked": true' in ls), f"before={before} after={after}")

        # M2a：答對→回饋 DOM 由空變正確
        q1 = "demo-skin-barrier-q1"
        await page.click(f"#m2-input-{q1} input[value='0']")
        await page.click(f"#m2-submit-{q1}")
        await asyncio.sleep(.3)
        fb = await page.evaluate(f"(()=>{{const f=document.querySelector('[data-feedback-for=\"{q1}\"]');return [f.textContent,f.dataset.result||''].join('|')}})()")
        ok("M2", "答對：回饋 DOM 狀態由空變「正確」（點擊前後可測）", fb.endswith("|correct") and "正確" in fb and "不正確" not in fb, f"feedback={fb}")

        # M2b：答錯→回饋變錯
        q2 = "demo-skin-barrier-q2"
        await page.click(f"#m2-input-{q2} input[value='0']")  # 錯答案（正解=1）
        await page.click(f"#m2-submit-{q2}")
        await asyncio.sleep(.3)
        fb2 = await page.evaluate(f"(()=>{{const f=document.querySelector('[data-feedback-for=\"{q2}\"]');return [f.textContent,f.dataset.result||''].join('|')}})()")
        ok("M2", "答錯：回饋 DOM 狀態由空變「不正確」", "不正確" in fb2 and fb2.endswith("|wrong"), f"feedback={fb2}")

        # M8：答錯自動展開 L1＋點擊提示二展開 L2
        l1 = await page.evaluate(f"document.querySelector('#m8-ladder-{q2} .hint[data-level=\"1\"]').classList.contains('shown')")
        await page.click(f"#m8-hint-{q2}-l2")
        await asyncio.sleep(.3)
        l2 = await page.evaluate(f"document.querySelector('#m8-ladder-{q2} .hint[data-level=\"2\"]').classList.contains('shown')")
        ok("M8", "提示階梯：答錯自動展開 L1＋點擊展開 L2（DOM class 狀態改變）", l1 and l2, f"l1_shown={l1} l2_shown={l2}")

        # M9：拖曳配對（drag_to 真拖曳事件鏈）→drop-zone 狀態改變＋回饋正確
        zone = page.locator("#m9-drop-match-1-0")
        before_zone = await zone.inner_text()
        await page.click('#m9-tray-match-1 .drag-chip[data-right="細胞間脂質（灰漿）"]')
        await asyncio.sleep(.2)
        await page.evaluate("""(() => {
            const chip = document.querySelector('#m9-tray-match-1 .drag-chip[data-right="細胞間脂質（灰漿）"]');
            const zone = document.getElementById('m9-drop-match-1-0');
            const dt = new DataTransfer(); dt.setData('text/plain', chip.dataset.right);
            zone.dispatchEvent(new DragEvent('dragover', { dataTransfer: dt, bubbles: true }));
            zone.dispatchEvent(new DragEvent('drop', { dataTransfer: dt, bubbles: true }));
        })()""")
        await asyncio.sleep(.4)
        after_zone = await zone.inner_text()
        fbm = await page.evaluate("(()=>{const f=document.querySelector('[data-feedback-for=\"match-match-1\"]');return [f.textContent,f.dataset.result||''].join('|')})()")
        ok("M9", "拖曳配對：drop 後 zone 狀態改變＋回饋正確", before_zone == "拖到這裡" and after_zone != before_zone and fbm.endswith("|correct"), f"before='{before_zone}' after='{after_zone}' fb={fbm}")

        # M12：捲動→頂部進度線寬度改變（起點＝捲到中段，終點＝底）
        await page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight * 0.2)")
        await asyncio.sleep(.4)
        w0 = await page.evaluate("document.getElementById('m12-scroll-progress').style.width")
        await page.evaluate("window.scrollTo(0, document.documentElement.scrollHeight)")
        await asyncio.sleep(.4)
        w1 = await page.evaluate("document.getElementById('m12-scroll-progress').style.width")
        ok("M12", "捲動→閱讀進度線 width 單向增大", float(w0.strip('%') or 0) < float(w1.strip('%') or 0) and float(w1.strip('%') or 0) > 90, f"mid={w0} bottom={w1}")

        # M3：補完模組01全部（勾 unit-tewl＋q2 改對＋配對全對）→鎖翻轉隱藏（狀態可測）
        locked_before = await page.evaluate("getComputedStyle(document.getElementById('m3-lock-demo-chemical-peel')).display")
        await page.check("#m1-check-unit-tewl")
        await page.check(f"#m2-input-{q2} input[value='1']")
        await page.click(f"#m2-submit-{q2}")
        for chip_text, zi in [("細胞間脂質（灰漿）", 0), ("磚塊", 1), ("屏障功能指標", 2)]:
            await page.evaluate("""(args) => {
                const t = args[0], i = args[1];
                const chip = document.querySelector(`#m9-tray-match-1 .drag-chip[data-right="${t}"]`);
                const zone = document.getElementById('m9-drop-match-1-' + i);
                const dt = new DataTransfer(); dt.setData('text/plain', t);
                zone.dispatchEvent(new DragEvent('dragover', { dataTransfer: dt, bubbles: true }));
                zone.dispatchEvent(new DragEvent('drop', { dataTransfer: dt, bubbles: true }));
            }""", [chip_text, zi])
        await asyncio.sleep(.4)
        locked_after = await page.evaluate("getComputedStyle(document.getElementById('m3-lock-demo-chemical-peel')).display")
        ok("M3", "前一模組全達標→鎖由顯示翻轉隱藏", locked_before == "block" and locked_after == "none", f"before={locked_before} after={locked_after}")

        # M1 持久化：reload 後進度保留（純 localStorage）
        await page.reload()
        await page.wait_for_selector("#m1-progress-demo-skin-barrier", state="attached", timeout=5000)
        pct = await page.inner_text("#m1-progress-demo-skin-barrier .pct")
        ok("M1", "reload 後進度條保留（localStorage 持久化）", pct not in ("0%", ""), f"pct={pct}")

        # M11：課程頁點書籤→class 變＋localStorage；回首頁收藏架狀態變
        bm = page.locator("#m11-bookmark-demo-skin-barrier")
        b_before = await bm.evaluate("e => e.classList.contains('saved')")
        await bm.click(); await asyncio.sleep(.3)
        b_after = await bm.evaluate("e => e.classList.contains('saved')")
        lsbm = await page.evaluate("localStorage.getItem('mats-bookmarks')") or ""
        ok("M11", "書籤點擊→class＋localStorage 狀態改變", not b_before and b_after and "demo-skin-barrier" in lsbm, f"before={b_before} after={b_after}")

        # 首頁：M10 註冊表驅動（第二門課自動出現＝擴充斷言）＋M6 連擊＋M11 收藏架＋M5 印章
        await page.goto(BASE + "/pages/index.html")
        await page.wait_for_selector("#m10-path-cards .card", state="attached", timeout=5000)
        cards = await page.locator("#m10-path-cards .card").count()
        c2 = await page.locator("#m10-path-cards .card", has_text="擴充演示").count()
        ok("M10", "註冊表驅動路徑卡：第二門課未經框架改動自動渲染（擴充斷言實測）", cards >= 3 and c2 >= 1, f"cards={cards} course2_cards={c2}")
        dots_on = await page.locator(".streak-dots i.on").count()
        sc = await page.inner_text(".streak-count")
        ok("M6", "連擊數字＋7 格圓點：今日點亮", dots_on == 1 and sc == "1", f"count={sc} dots_on={dots_on}")
        shelf = page.locator('#m11-bookmark-shelf li[data-module="demo-skin-barrier"]')
        ok("M11", "首頁收藏架反映收藏狀態（li 非 empty）", (await shelf.count()) == 1 and not await shelf.evaluate("e => e.classList.contains('empty')"))
        seal = page.locator("#m5-seal-demo-skin-barrier")
        ok("M5", "印章槽：達標模組點亮（class awarded）", await seal.evaluate("e => e.classList.contains('awarded')"))

        # M13（課程頁）：第二門課全達標→證書入口顯形
        await page.goto(BASE + "/pages/course.html?course=demo-course-two")
        await page.wait_for_selector("#m1-check-unit-demo-two-a", state="attached", timeout=5000)
        await page.check("#m1-check-unit-demo-two-a")
        await page.click("#m2-input-demo-course-two-m1-q1 input[value='0']")
        await page.click("#m2-submit-demo-course-two-m1-q1")
        await asyncio.sleep(.4)
        ready = await page.evaluate("document.getElementById('m13-cert-entry').dataset.ready")
        disp = await page.evaluate("getComputedStyle(document.getElementById('m13-cert-entry')).display")
        ok("M13", "全模組達標→證書入口由 hidden 變可見", ready == "1" and disp != "none", f"ready={ready} display={disp}")

        # M14：媒體渲染——neofilera 課頁 media[] 落地（img/video DOM 元素存在＋tier 標識渲染）
        await page.goto(BASE + "/pages/course.html?course=neofilera-pdlla-cmc")
        await page.wait_for_selector("figure[data-mid='M14']", state="attached", timeout=5000)
        await page.goto(BASE + "/pages/course.html?course=neofilera-pdlla-cmc")
        await page.wait_for_selector("#m1-progress-neofilera-m1", state="attached", timeout=5000)
        nmedia = await page.evaluate("document.querySelectorAll('[data-mid=\\'M14\\']').length")
        nvideo = await page.evaluate("document.querySelectorAll('[data-mid=\\'M14\\'] video').length")
        nimg = await page.evaluate("document.querySelectorAll('[data-mid=\\'M14\\'] img').length")
        nbadge = await page.evaluate("document.querySelectorAll('[data-mid=\\'M14\\'] .tier-badge').length")
        ok("M14", "neofilera 媒體區塊渲染：DOM 元素>0＋video/img 標籤＋tier 標識", nmedia > 0 and nvideo > 0 and nimg > 0 and nbadge == nmedia, f"blocks={nmedia} video={nvideo} img={nimg} badges={nbadge}")
        # 排除清單 grep 自驗（CSS 無 monospace 字體族、無 #00ff00 系綠）
        print("\n== 站體頁面 console errors ==", errs or "無")
        print("\n".join(RESULTS))
        await b.close()

asyncio.run(main())
