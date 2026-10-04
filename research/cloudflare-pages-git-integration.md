# Cloudflare Pages Git integration 與 Direct Upload 上限研究（workspace: 2026-11-15 北區醫美工作坊・自有靜態站）

開放決策代號：
- **(R1)** 部署路徑二選一：private GitHub repo + Git integration（push 即自動部署）vs Direct Upload（手動 wrangler／拖放上傳）。子問題：免費層是否支援 private repo 的 Git integration；若走 Direct Upload，免費層限額是多少。

條目為 append-only；每條 = URL / tier / argument（一句）。Tier 定義：primary = 廠商官方文件／官方條款、經本輪直接抓取驗證的頁面本體；secondary = 博客、轉述、廠商論壇回複。所有 URL 均於 2026-10-04 實際抓取或經搜尋快取確認存在且內容如所述。

---

## 條目

### Decision (R1) — 免費層 Git integration 支援 private repo

- **URL**: https://developers.cloudflare.com/pages/get-started/git-integration/
  **tier**: primary（Cloudflare Pages 官方文件，本輪直接抓取全文）
  **argument**: (R1) 明文「Both private and public repositories are supported」——免費層 Git integration 直接吃 private GitHub repo，決策 (R1) 的主答案：自動部署路徑不需要为此升級付費方案。

- **URL**: https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/
  **tier**: primary（Cloudflare Pages 官方 GitHub integration 文件，本輪直接抓取全文）
  **argument**: (R1) 授權經「Cloudflare Workers and Pages」GitHub App 完成，個人帳號或組織帳號皆可、可按 repo 授權——本專案的本地無 remote repo 推到 GitHub private 後即可掛上，無額外門檻；但只支援 GitHub/GitLab 雲端實例，self-hosted Git 不行（要 self-hosted 就得走 Direct Upload + CI）。

- **URL**: https://developers.cloudflare.com/pages/platform/limits/
  **tier**: primary（Cloudflare Pages 官方 Limits 頁，本輪直接抓取全文）
  **argument**: (R1) 免費層限額表寫的是「Builds per month 500、1 concurrent build、build timeout 20 分鐘」，且明文限額只 20,000 檔/站、單檔 25 MiB、100 projects/帳號、100 custom domains/專案——對純 HTML 站全部遠超需求，兩條路徑在「量」面都構不成瓶頸。

- **URL**: https://developers.cloudflare.com/pages/get-started/direct-upload/
  **tier**: primary（Cloudflare Pages 官方 Direct Upload 頁，本輪直接抓取全文；官方 repo 源文件 cloudflare-docs/src/content/docs/pages/get-started/direct-upload.mdx 同步核對）
  **argument**: (R1) Direct Upload 走 Wrangler CLI 或儀表板拖放（Wrangler 20,000 檔、拖放 1,000 檔，單檔同 25 MiB），且官方明文「選擇 Direct Upload 後不能改切 Git integration，要自動部署需重開新專案」——路徑選擇是單向門：若未來可能加 remote repo，應一開始就選 Git integration。

- **URL**: https://community.cloudflare.com/t/builds-vs-deployments/494717
  **tier**: secondary（Cloudflare 官方論壇，Cloudflare 員工 Erisa 2023-04 回複；非文件本體故標 secondary）
  **argument**: (R1) 官方員工明文「wrangler pages publish/deploy 不計入 500 builds/月限額，目前 unlimited（官方保留未來另設 Direct Upload 限額的權利）」——即 500/月只計 CI build，手動 wrangler 部署不計；這是 Direct Upload 限額問題的最強現存答案，但因無官方文件明文，作為 secondary 佐證。

- **URL**: https://picklog.cc/blog/cloudflare-pages-direct-upload-limits
  **tier**: secondary（第三方博客，2026-08 以自己的 103 次部署實測佐證）
  **argument**: (R1) 獨立實測佐証上條：Direct Upload 部署不吃 500 builds/月額度，實務剩下的天花板是檔案數/單檔大小與 API rate limit（1,200 req/5min）——對低頻手動部署的單頁站，Direct Upload 與 Git integration 在免費層實務上都跑得住，真正的差異在上面的單向門條款與便利度。

### 搜了但沒有（searched-and-absent）

- **Query**: Cloudflare Pages Direct Upload 免費層限額官方明文（direct upload deployments 是否計入 500 builds/月）; **searched via**: web search + 直接抓取（developers.cloudflare.com/pages/platform/limits/、/pages/get-started/direct-upload/、/pages/how-to/use-direct-upload-with-continuous-integration/）; **result**: 官方文件全鏈無任何明文寫 Direct Upload 部署是否計入 500/月 —— limits 頁只有 Builds 表且明說指「push to your Git repository」觸發的 build，無 Deployments 小節；「Direct Upload 不計入、unlimited」的結論在官方文件中無明文，僅有 secondary 層級的論壇官方員工回複（見上條），故不列 unverified 條目、以論壇回複為最強答案。

---
