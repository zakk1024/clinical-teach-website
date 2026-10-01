# 主機與部署研究（workspace: 2026-11-15 北區醫美工作坊・自有靜態站）

開放決策代號：
- **(a)** 四家靜態主機（Cloudflare Pages / Netlify / Vercel / GitHub Pages）中，免費層條款、自訂網域+HTTPS、以及主機選擇本身是否影響 Google 收錄/爬蟲/AI 爬蟲存取——即「選主機」是 SEO 決策還是純營運決策
- **(b)** Google 官方文件中實際存在的靜態站 SEO 基礎建設（sitemap 提交、Search Console 驗證、robots.txt 語意）

條目為 append-only；每條 = URL / tier / argument（一句）。Tier 定義：primary = Google 官方文件、廠商官方文件／官方條款、經本輪直接抓取驗證的頁面本體；secondary = 博客、轉述、廠商自述案例。所有 URL 均於 2026-10-01 實際抓取或經搜尋快取確認存在且內容如所述。

---

## 條目

### Decision (a) — 免費層條款對商業/行銷站的限制

- **URL**: https://vercel.com/legal/terms （§4 Hobby Plan）
  **tier**: primary（Vercel 官方服務條款，2026-06-01 版，本輪直接抓取全文）
  **argument**: (a) Hobby 免費條款明文「僅限個人或非商業用途」，且 Vercel 保留無理由關閉免費層部署的權利——工作坊若算商業推廣，掛 Vercel 免費層是違反條款的選項，且內容預設會被拿去訓練 AI。

- **URL**: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
  **tier**: primary（GitHub 官方文件，本輪直接抓取全文）
  **argument**: (a) GitHub Pages 明文「不適用於也不允許免費託管線上商業、電商或以商業交易為主的網站」——行銷/報名 landing page 落在排除範圍，GitHub Pages 對本專案是條款上不合規的選項（教育練習性質的複製站除外）。

- **URL**: https://www.netlify.com/legal/self-serve-subscription-agreement/
  **tier**: primary（Netlify 官方自服務訂閱協議，本輪直接抓取全文）
  **argument**: (a) 免費層沒有「非商業使用」禁令（僅引用一般使用條款、超量計費），但「Free Usage Tier 專案可被無理由、無通知停用，無 SLA」——四家中條款上唯一容許免費跑商業站的是 Netlify（與 Cloudflare），代價是免費層保障最薄。

- **URL**: https://www.cloudflare.com/terms/ （Self-Serve Subscription Agreement）
  **tier**: primary（Cloudflare 官方自服務協議，本輪直接抓取全文）
  **argument**: (a) 免費層的明文限制是「不得在免費服務上處理信用卡個資」與禁止轉售/存 PHI 等，不含一般商業用途禁令——靜態行銷站（報名走外部表單、不在站上收卡）在 Cloudflare 免費層條款的四個選項中限制最少。

- **URL**: https://developers.cloudflare.com/pages/platform/limits/
  **tier**: primary（Cloudflare Pages 官方文件，本輪直接抓取全文）
  **argument**: (a) 免費層 100 個自訂網域/專案、20,000 檔/站、單檔 25 MiB、每月 500 次 build——對單頁+課程頁的規模全部遠超需求；四家免費層在「量」的面向沒有差異，差異全部在上面的條款面。

- **URL**: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages
  **tier**: primary（GitHub 官方文件，本輪直接抓取全文）
  **argument**: (a) 四家全部支援自訂網域（apex 與 www 都支援）＋自動 HTTPS——「能不能掛自訂網域讓社群爬蟲抓到 og:image」在主機面不構成差異，不构成選擇依據。

- **URL**: https://docs.netlify.com/manage/domains/get-started-with-domains/
  **tier**: primary（Netlify 官方文件，本輪直接抓取全文）
  **argument**: (a) Netlify DNS 管理下的網域自動簽發 SSL 憑證、外部 DNS 走 ACME——與 GitHub Pages／Cloudflare Pages 同級，再次確認 HTTPS 部分是四家共通的最低標，不是差異點。

### Decision (a) — 社群/AI 爬蟲對主機的差異

- **URL**: https://developers.facebook.com/documentation/sharing/webmasters/web-crawlers
  **tier**: primary（Meta 官方 crawler 文件，本輪經搜尋快取抓取全文；HTTP 200）
  **argument**: (a) facebookexternalhit 只在連結被分享時抓 OG（快取至下次分享/約 30 天），且「為安全檢查可繞過 robots.txt」；要求 gzip/deflate、OG 標籤必須在前 1MB 內——任何正統靜態主機都滿足，真正要做的是上線後用 Sharing Debugger 強制重抓，主機選擇本身不影響 FB/LINE 預覽。

- **URL**: https://help2.line.me/linesearchbot/web/?contentId=50006055&lang=en
  **tier**: primary（LINE 官方帮助中心「What is Linespider?」，本輪直接抓取；內容為 JS 渲染但標題與摘述可核）
  **argument**: (a) 官方明文 Linespider 遵守 Robots Exclusion Protocol——已確認事實再獲官方來源確認；它不做 JS 執行，OG 標籤必须在初始 HTML 裡，這对所有候選主機同樣成立，是靜態站的預設優勢而非主機差異。

### Decision (b) — Google 官方文件中實際存在的 SEO 基礎建設

- **URL**: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
  **tier**: primary（Google Search Central 官方文件，本輪直接抓取全文）
  **argument**: (b) 官方列出的動作就是：做 sitemap（XML/RSS/文字）、UTF-8、絕對 canonical URL、放在影響目標 URL 的目錄、經 Search Console 或 robots.txt 提交——這是 Google 官方文件裡「主機商能提供的 SEO 功能」的全部清單，四家靜態主机都能原樣滿足。

- **URL**: https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget
  **tier**: primary（Google Search Central 官方文件，本輪直接抓取全文）
  **argument**: (b) crawl budget 由「容量上限×需求」決定，容量上限随服务器响应速度（crawl health）浮动，但官方明言这是大站问题——对几个页面的静态站，主机差异只在「CDN 全球节点回应快、不会超时」这种底线层面，不构成排名或收錄速度的可择差异。

- **URL**: https://support.google.com/webmasters/answer/35179
  **tier**: primary（Search Console 官方说明「Verify your site ownership」，本輪確認 HTTP 200 且標題相符）
  **argument**: (b) 验证方法为 DNS TXT（Domain property 唯一方式）＋HTML 檔案/meta tag/GA/GTM（仅 URL-prefix property）——Domain property 需要 DNS 控制权，这让「域名放在 Cloudflare DNS」这类决定先于主机选择发生，属于域名决策而非主机决策。

### 搜了但沒有（searched-and-absent）

- **Query**: GPTBot / ClaudeBot 官方文件中關於「爬蟲是否因託管商不同而有差異」的聲明; **searched via**: web search（developers.openai.com、docs.anthropic.com、perplexity.ai 官方域）; **result**: 各家都有自家爬蟲的 UA/robots 頁（openai.com/bot、docs.anthropic.com 對應頁、perplexity.ai/perplexitybot，均 HTTP 200/存在），但內容只講 UA token 與 robots 服從，無任何按託管商區分的機制——「主機選擇影響 AI 爬蟲存取」在四家官方文件中均無依據（AI 引用 null effect 的既有結論不重做）。
- **Query**: 任一靜態主機商官方文件中聲稱「選我們對 Google 收錄/排名有幫助」; **searched via**: web search（四家官方 docs 域名）; **result**: 無——四家官方文件都不對 SEO 效果做任何承諾，所有「X 主機 SEO 更好」的說法都只存在於二手博客。

---
