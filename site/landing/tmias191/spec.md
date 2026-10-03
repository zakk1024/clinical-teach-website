# 規格 — Vesuyan 分享落地頁（tmias191）

**交付物**：`index.html`（同目錄，單一 HTML 檔、無框架、內聯 CSS、行動優先、繁體中文）。部署家＝自建教學網站（Q15 鎖定 2026-09-30：3 週內上線；域名待定＝Q23，佔位 `<落地頁>` 保留至域名定案）。原案 vesuyan.com 子頁已廢——佔位 URL `vesuyan.com/tmias191/` 為歷史佔位，部署時全數換成教學網站實際網址（canonical／og:url 須與之一致）。

## 這頁是什麼／不是什麼

- **是**：社群分享時的 OG 載體＋UTM 歸因中樞（ADR-0002）。本場（2026-11-15）不指望搜尋排名。
- **不是**：SEO 頁。官方課程頁是第三方學會 CMS 頁（[id=191](https://www.tmias.org.tw/events/content.php?id=191&p=1&c=Y)）——無 canonical、無 schema.org Event、title/description CMS 模板自動生成、og:image 指向被 robots.txt Disallow 的 `/upload/*`（Google 圖搜索引被封，社群抓取正常）。本頁把這些控制權全部拿回來。
- canonical＝self：跨域 canonical 是單向 hint，會把 authority 倒貼給平台頁——已定案不指回學會頁。

## 頁面內容（鎖定規格）

- 課程資訊：薛乃維醫師主講，TMIAS 微整學院大師淬煉系列鼻埋線工作坊；2026-11-15（日）09:00–12:30，08:30 報到；台北市大安區信義路三段 151 號 7 樓（維序妍診所）；主辦＝台灣微整形美容醫學會；特管時數 4 小時；限量 hands-on 6 名＋observer 15 名。
- **單一 CTA**＝官方報名鏈 `https://www.surveycake.com/s/7m3mA`。全站只有這一個 CTA，不塞第二個。
- 無 analytics script（Zack 端自己接）；不動 vesuyan.com 現有頁面結構。

## Meta 規格

- title／description：手寫（見 HTML；description 前段講賣點，不放 URL——學會頁的教訓就是前段被 surveycake 連結吃掉）。
- og:title／og:description／og:image（1200×630）＋ twitter:card summary_large_image fallback。
- **og:image 目前是佔位絕對 URL**（`https://vesuyan.com/tmias191/og-image.jpg`）：上線後要放真實圖檔，且路徑**不能**落在任何 robots.txt Disallow 位置（學會頁就是栽在 /upload/*）。
- schema.org Event JSON-LD——本頁唯一自有槓桿（官方 CMS 頁加不了，本頁加得上）：名稱／時間／地點／主辦／主講／名額（performerMaxAttendeeCount 21）／報名 URL 全寫入。

## UTM 總表（每通道一條；帖文連結＝本頁 URL＋對應 UTM）

頁內主 CTA 預設**不帶 UTM**（直接流量）。各社群貼文／郵件用的連結如下（以部署路徑 `https://vesuyan.com/tmias191/` 為例）：

| 通道 | 連結 |
|---|---|
| IG（自有＋boost） | `https://vesuyan.com/tmias191/?utm_source=ig&utm_medium=social&utm_campaign=tmias191` |
| LINE 群 | `https://vesuyan.com/tmias191/?utm_source=line-group&utm_medium=social&utm_campaign=tmias191` |
| Vesuyan 官網 | `https://vesuyan.com/tmias191/?utm_source=vesuyan-site&utm_medium=social&utm_campaign=tmias191` |
| Email（秘書代發） | `https://vesuyan.com/tmias191/?utm_source=email&utm_medium=email&utm_campaign=tmias191` |

（FB 若启用：`utm_source=fb`，medium=social，campaign 同。新增通道照 `utm_source=<通道>`／`utm_medium=social|email`／`utm_campaign=tmias191` 規則加行。）

## 上線驗證指令（DOM 存在只是代理指標——實抓驗證預覽實效）

1. **OG 預覽實效**（過閘①）：上線後跑
   `curl -s "https://www.facebook.com/ads/tools/inspect/summary.html?url=<部署URL>"` 或用 LinkedIn Post Inspector / Twitter Card Validator 實抓，確認標題＋圖片**真的渲染出來**（學會頁 og:image 實測 `facebookexternalhit` 回 200——本頁圖片路徑要同標準）。
2. **JSON-LD**：`curl -s <部署URL> | python3 -c "import sys,re,json; print(json.loads(re.search(r'application/ld\+json.*?>(.*?)</script>', sys.stdin.read(), re.S).group(1))['@type'])"` 應輸出 `Event`；再用 Google Rich Results Test 跑一次。
3. **CTA**（過閘③）：全檔僅一個 `<a href>`，指向 `https://www.surveycake.com/s/7m3mA`，無 UTM。
4. **行動預覽**：手機（或 devtools 375px）檢查 CTA 拇指區、字級、loading（單檔無框架、無外部請求，除字體外）。

## 待辦交接（非本頁職責，但擋上線）

- [ ] 部署路徑定案 → 替換 HTML 內三處 `vesuyan.com/tmias191/` 佔位。
- [ ] og-image.jpg 1200×630 真實圖檔上線（放可被抓取路徑）。
