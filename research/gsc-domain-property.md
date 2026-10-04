# GSC Domain property 研究（workspace: 2026-11-15 北區醫美工作坊・自有靜態站）

開放決策代號：
- **(a)** Domain property vs URL-prefix property：域名驗證（DNS TXT）是否涵蓋所有子網域與協定變體？TXT record 要加在哪？
- **(b)** 驗證後 sitemap 提交與 URL 手動請求收錄的限制（免費層配額）
- **(c)** 純靜態站（Cloudflare Pages）的 sitemap 是自動生成还是要手動建——影響收尾工作單

條目為 append-only；每條 = URL / tier / argument（一句）。Tier 定義：primary = Google 官方文件（本輪直接抓取全文）、廠商官方文件（本輪直接抓取全文）；secondary = 博客、轉述、搜尋快照。所有 URL 均於 2026-10-04 實際抓取或經搜尋快取確認存在且內容如所述。

---

## 條目

### Decision (a) — 兩種 property 的涵蓋範圍與驗證方式

- **URL**: https://support.google.com/webmasters/answer/10431861
  **tier**: primary（Google Search Central 官方術語頁「Domain property」，本輪直接抓取全文）
  **argument**: (a) Domain property 定義為「不含協定、不含路徑」的 property（example.com），官方明文「Can include subdomains」——一個 Domain property 同時涵蓋所有子網域與 http/https 變體，與 URL-prefix property（含協定、可含路徑）相對。

- **URL**: https://support.google.com/webmasters/answer/10432366
  **tier**: primary（Google Search Central 官方術語頁「URL-prefix property」，本輪直接抓取全文）
  **argument**: (a) URL-prefix property 只涵蓋「你輸入的那個完整前綴」——https://example.com 與 https://www.example.com 是兩個不同 property，要分別建、分別驗；要一站看全站就要用 Domain property。

- **URL**: https://support.google.com/webmasters/answer/35179 （實抓為同一頁 /webmasters/answer/9008080）
  **tier**: primary（Google「Verify your site ownership」官方說明，本輪直接抓取全文）
  **argument**: (a) Domain property 只能用域名驗證器（域名註冊商/DNS）驗證；TXT record 的 Host/Name 欄留空或填 @（apex），value 貼 GSC 給的完整字串（含 google-site-verification= 前綴）；若 apex 已有 CNAME 且 target 是父域，則改用 CNAME 驗證流程。驗證根域即自動驗證所有子網域（反向不成立：驗 m.example.com 不會驗到 example.com）；HTML 檔案/meta tag/GA/GTM 四法只能用於 URL-prefix property，且 DNS 驗證成功後 record 不能刪（GSC 會定期複查，失效會過期）。

- **URL**: https://support.google.com/webmasters/answer/35179 （同上，Manual domain name provider 小節）
  **tier**: primary（Google 官方文件，本輪直接抓取全文）
  **argument**: (a) 手動 DNS 驗證官方明言「可能要等兩三天才开始生效」——驗證按鈕按下去失敗先等一兩天再說；因為 DNS 由 Cloudflare 管，機主（帳號持有者）自己在 Cloudflare DNS 加 TXT 即可，不用登入 GSC 以外的一切都能自動化。

### Decision (b) — sitemap 提交與 URL 手動請求收錄的配額

- **URL**: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
  **tier**: primary（Google Search Central 官方文件，本輪直接抓取全文；與 hosting-and-deployment.md 同一頁，重述 R3 相关段落）
  **argument**: (b)(c) sitemap 建議放站根（不經 GSC 提交時只影響父目錄以下）、UTF-8、絕對 canonical URL；單檔上限 50MB/50,000 URL；Google 忽略 priority/changefreq，只採信可驗證的 lastmod；提交是 hint 不保證收錄；小站（≤約500頁且從首頁可達全部頁面）官方明言可以不用 sitemap，直接 request indexing 首頁即可。

- **URL**: https://support.google.com/webmasters/answer/7451001
  **tier**: primary（GSC「Sitemaps report」官方說明，本輪直接抓取全文）
  **argument**: (b) 經 GSC 提交 sitemap 必須有該 property 的 owner 權限（無權限就走 robots.txt 的 Sitemap: 行）；Sitemaps report 只顯示「掛在當前 property」下提交的 sitemap——用 Domain property 提交則全域可見；提交後 Google 立即抓一次、之後按自己的節奏重抓；報告最多列 1,000 個提交記錄。

- **URL**: https://support.google.com/webmasters/answer/9012289
  **tier**: primary（GSC「URL Inspection tool」官方說明，本輪直接抓取全文）
  **argument**: (b) Request Indexing 官方只說「每個你擁有的 property 有每日檢查/請求上限」且「不保證收錄」，頁面多要很多頁就該交 sitemap 而不是逐個點；Google 官方從未公布這個每日配額的數字（社群共識約 10–12/天，見下方 secondary）。

- **URL**: https://developers.google.com/search/apis/indexing-api/v3/using-api ＋ /v3/quota-pricing
  **tier**: primary（Google Indexing API 官方文件兩頁，本輪直接抓取全文）
  **argument**: (b) Indexing API 官方限定只給 JobPosting 或 VideoObject+BroadcastEvent 頁面用，預設配額 200 requests/天/project（要超額要填表申請）——本專案（教學靜態頁）兩類都不符，正式的批量收錄路徑只有 sitemap＋GSC UI 的 Request Indexing；URL Inspection API 是唯讀（2,000 次/天/property，官方 limits 頁數字，經搜尋快取核），不能代替按鈕。

- **URL**: https://indexing.io/google-search-console-api ＋ https://patrickstox.com/technical-seo/tools/search-engine-tools/google-search-console/url-inspection-tool ＋ https://indexbolt.com/blog/request-indexing-google-search-console
  **tier**: secondary（三家 SEO 專業站互相一致，2026-10-04 經搜尋快取核）
  **argument**: (b) 社群共識：GSC UI 的 Request Indexing 實際配額約 10–12 次/天/property，超了就報 quota exceeded、隔日重置（Google 官方頁只承認「有每日上限」不給數字）；本站頁面數遠低於配額，逐頁手動請求收錄在配額內可行。

### Decision (c) — 純靜態站的 sitemap 要不要手動建

- **URL**: https://developers.cloudflare.com/pages/ ＋ https://developers.cloudflare.com/pages/framework-guides/deploy-a-hugo-site/
  **tier**: primary（Cloudflare Pages 官方文件，本輪直接抓取全文）
  **argument**: (c) Cloudflare Pages 官方文件沒有任何「自動生成 sitemap」的功能——Pages 只負責部署你 build 出來的靜態檔；用 Hugo/Astro 等生成器時 sitemap 由生成器產出，純手寫靜態 HTML 站則 sitemap.xml 要自己寫進 repo（Google 官方也接受純文字 sitemap，一行一個 URL）。

- **URL**: https://gohugo.io/templates/sitemap ＋ https://gohugo.io/configuration/sitemap
  **tier**: secondary（Hugo 官方文件，經搜尋快取核；站方文件本體）
  **argument**: (c) 若站體改走 Hugo：sitemap.xml 是內建預設自動生成（可关閉、可 per-page front matter 排除）——「要不要手動建 sitemap」實際取決於站是用什麼生成的；純靜態 HTML ＝ 手動寫一個 sitemap.xml 放 repo 根，工作量約半小時。

### 搜了但沒有（searched-and-absent）

- **Query**: Cloudflare Pages 官方文件中「自動生成 sitemap」的功能; **searched via**: web search（developers.cloudflare.com 官方域）; **result**: 官方只有「用 Worker 從 CMS 動態產 sitemap」的第三方教程與框架指南（Hugo 等自帶），Pages 本身無自動 sitemap 功能——純靜態站需在 build 產出或手寫 sitemap.xml，Google 官方確認這是站主自己的責任（见上列 primary 條目）。

---

## 對收尾工作單的落點（僅為上述條目的直接推論）

1. **驗證**：建 **Domain property**（ apex TXT，Host 欄留空/`@`）——一站涵蓋 www/apex、http/https、未來子網域，且驗證不隨換主機失效；TXT 由機主在 Cloudflare DNS 加（機主動作），加完 specialist 可代跑 GSC 驗證按鈕前的 dig 預檢。
2. **sitemap**：純靜態站 → 手寫 `sitemap.xml`（只列 canonical、200、可收錄頁，lastmod 要誠實）放站根＋robots.txt 加 `Sitemap:` 行，上線後經 GSC Sitemaps report 提交（需 owner 權限＝機主帳號）。
3. **收錄**：頁面數在 ~10–12/天的 Request Indexing 社群配額內，逐頁手動請求可行；批量正式機制＝sitemap；Indexing API 對本站內容類型不合規，不要用。
