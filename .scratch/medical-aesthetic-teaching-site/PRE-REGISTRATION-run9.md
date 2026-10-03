# 第 9 跑（落地頁入站＋部署＋SEO 執行輪）事前登記（2026-10-01 開跑前寫死）

## 順序違規記錄（先寫先認）
研究閘 subagent（hosting/deployment）在本檔寫入**之前**已派出——違反「預登先拍後跑」。照 promo-191 素材輪先例記帳：研究閘無返工、觸碰預測＝各 1（含本檔落盤），不追溯補預測。

## 閘門裁決
- 執行模型檔位：本機 llama-server 槽（runtime 層 model=qwen38-uncensored @ 127.0.0.1:8085）——同 run2 起各跑同槽＝甜區直通組隊（本機唯一有實測數據檔位，Qwen 屬未測格已在前跑記錄）。
- 任務過閘：多步驟（研究閘→域名/部署決策→landing 搬入→SEO 管線落地）→ 組隊增益大。

## 本跑輸入（盤點實測，2026-10-01）
- 本 repo：git 乾淨 HEAD `891b64f`；雙殼 17/17 零紅（本 session 重跑驗證）；server 8777 已起。
- **未結帳（run8）**：使用者視覺簽字 nose 課頁（硬重新整理）——簽字＋預測帳對帳才算 run8 完成。
- 落地頁現居 `/Users/zakk/Desktop/MrBeast/SEO/.scratch/promo-191/deliverable-landing/`（DATA PENDING 清零、四閘過、素材齊；canonical 佔位=https://vesuyan.com/tmias191/）。
- ADR-0002（MrBeast repo，2026-09-30 Zack 拍板）：一頁式掛自建教學網站，**不再掛 vesuyan.com**——canonical 佔位與此決定尚未對帳，本跑必須處理。
- 時間錨：workshop 2026-11-15；報名主通道=私域（LINE群/學會郵件），SEO/GEO=下場資產（ADR-0002 已鎖，本跑不重開）。
- 研究閘現存檔：MrBeast/research/ 六檔＋本 repo research/ 四檔＋新派 hosting-and-deployment.md。

## 三條預測（跑前寫死，落空不改寫）
1. 研究 subagent 觸碰＝1（研究無返工；基線：新斷言首跑必紅——本跑研究檔首寫若含未經 fetch 驗證的 URL，即兌現）。
2. landing 搬入本 repo 後，既有雙殼 17 斷言會紅至少一次（landing 是新增渲染面——基線預期）。
3. 域名/部署決策會被「部署时限」反推鎖定（11/15 前上線＋GSC 手動請求收錄＝新域數週收錄慢），最終收斂到免費層方案（Cloudflare Pages／Netlify 級）——若收斂到需買域＋另購託管即落空。

## 簽字輪結果（2026-10-01，使用者親眼）
- **Run8 簽字：未過閘**——使用者判：解剖圖太粗糙。10 張重畫 SVG 退回；解剖圖正確性＋精美性另開 frontier（圖風 room 已有 Session-3 研究＋試管判決在 image model workspace：風格閘過、解剖閘全滅——死因＝任務錯配，非僅模型爛）。
- **Bug BUG-1（本跑修）**：M3 模組鎖注記顯示 bug——pending 計數數「已建立未勾記錄」，零進度時顯示「剩餘 0 項」但鎖著（site.js renderLocks）。機制層正確（勾滿 M2 解鎖正常，Playwright 實測 locked→unlocked＋渲染 2666 字元）；只修顯示。新斷言：模組零進度時鎖注記數字＝該模組單元總數。

## 已鎖（本輪使用者逐條答覆 2026-10-01）
- Q2 鎖定：落地頁＝獨立 marketing 頁 `site/landing/tmias191/`，assets 整包搬入，courses.yml／框架層零改動。
- Q3 鎖定：落地頁角色＝SEO/GEO 長期入口＋報名漏斗，課後為下一場課服務（ADR-0002 原確認）。
- Q4 輸入：使用者無現成域名——域名＋註冊商為本輪開放決策。

## Round 2 鎖定（2026-10-01，使用者逐條答覆）
- **Q5 域名＝qqhairdoctor.com**（使用者拍板）。實測（本輪 whois＋NS）：NXDOMAIN＋registrar "No match"＝**可註冊**。商標面一句備註：QQ 字標在騰訊商標地盤，註冊商註冊不等於商標 clearance——使用者品牌決策，風險已告知。
- **Q6 註冊商＝Cloudflare Registrar＋站掛 Cloudflare Pages**（研究閘：註冊商不影響 SEO；Cloudflare 成本價無加價、同帳號整合；TLD 支援 430+，下單前查 .com  obviously 在）。
- **Q7 部署 KPI（防自欺條款）**：本場驗收＝域名註冊完成＋GSC 域名驗證＋sitemap 提交＋落地頁手動請求收錄各一次；排名與報名歸因計入下一場（ADR-0002 原句）。研究判死「11/15 前見效」——誰簽誰輸。
- 落盤連動：ADR-0002「掛自建教學網站」由本 ADR 系列接住——落地頁 canonical 佔位（vesuyan.com/tmias191/）部署時必須改寫為 qqhairdoctor.com 實際路徑（判準已列）。

## Round 2 鎖定（2026-10-01，使用者逐條答覆）
- **Q5 鎖定：域名＝qqhairdoctor.com**（本輪 RDAP 實測 404＝未註冊可買）。品牌判斷歸使用者；研究證據支持：域名不買排名買記憶點（Illyes，既有落盤）。
- **Q6 鎖定：Cloudflare Registrar 註冊＋Cloudflare Pages 託管**（研究閘：法律軸上免費層無商業禁令；Registrar 成本價無加價＋同家 DNS 整合；註冊與 DNS 是使用者手，agent 不動註冊台）。
- **Q7 鎖定：本場 KPI＝域名註冊完成＋GSC 域名驗證通過＋sitemap 提交＋落地頁手動請求收錄各一次（憑證＝截圖）；排名與報名歸因計入下一場（ADR-0002 原句）。**
- 預測帳預帳：預測 3「收斂到免費層方案」——**中**（Cloudflare 免費層＋.com 成本價購買，非另購託管）。預測 2「landing 搬入後雙殼紅至少一次」預測將落空——Q2 鎖定獨立頁不進框架，雙殼不渲染它；落空照規矩不改寫。

## 執行鏈（預登，開跑前寫死）
1. **使用者手（agent 動不了註冊台）**：Cloudflare 註冊 qqhairdoctor.com → Nameserver 指 Cloudflare → GSC 域名驗證（TXT）。
2. **派工單 A（frontend-developer）**：landing 整包搬入 site/landing/tmias191/（index.html＋assets 三檔），canonical/og:url/og:image 佔位改 qqhairdoctor.com 最終路徑；單檔零外部 JS/字體鎖照 promo-191 規格不破。
3. **BUG-1 修復（執行官親手）**：site.js renderLocks pending 顯示改 total−checked；新斷言入雙殼表。
4. **收尾（使用者手＋覆核）**：push＋Cloudflare Pages 部署（production branch）→ GSC 提交 sitemap＋手動請求收錄 landing URL → 截圖三張落 .scratch。
- 預測觸碰（區間，跑前寫死）：派工單 A：2–4（中——搬移＋佔位改寫＋雙向核）；BUG-1：1–3。

## 機械判準（本跑範圍內可驗者）
- 落地頁入站後 canonical/og:url/og:image 三者與實際部署 URL 一致（grep 可驗，搬入未改佔位＝紅）。
- Event JSON-LD 搬入後不破（JSON parse 可驗）。
- 雙殼 17/17＋新面斷言連跑零紅才算修復。
- 「上線」＝公網 URL 可 curl 到＋GSC 已驗證域名（做不到＝明寫未完成，不收口）。
