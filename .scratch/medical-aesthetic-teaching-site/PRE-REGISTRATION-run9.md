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

## 機械判準（本跑範圍內可驗者）
- 落地頁入站後 canonical/og:url/og:image 三者與實際部署 URL 一致（grep 可驗，搬入未改佔位＝紅）。
- Event JSON-LD 搬入後不破（JSON parse 可驗）。
- 雙殼 17/17＋新面斷言連跑零紅才算修復。
- 「上線」＝公網 URL 可 curl 到＋GSC 已驗證域名（做不到＝明寫未完成，不收口）。
