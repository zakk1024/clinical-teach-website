# Run9 執行單（2026-10-01 開跑前寫死——預登先拍後跑）

## 事前登記
| 執行者 | 交付物 | 自報檔位憑據 | 預測踢出（區間） | 預測觸碰（區間，含難度） |
|---|---|---|---|---|
| 主 agent（本尊） | BUG-1 修復＋新斷言＋連跑 | runtime 本機槽 qwen38-uncensored | n/a（自抓自修另記一欄） | 1–2（易：單函數＋一斷言） |
| frontend-developer | 落地頁搬入＋canonical/og:url/og:image 改寫＋assets 整包 | runtime 層同槽（配置層不算數） | 0–2 | 2–4（中：單檔 HTML 搬移＋三處 URL 改寫＋路徑改寫） |
| Zack 本人的手 | 域名註冊＋Cloudflare Pages 部署＋GSC 驗證＋sitemap 提交 | 人手，不進返工帳 | n/a | 外部依賴，不在預測內 |

跑爆區間＝「這尺寸任務不配這條管線」，下次直走單兵。整跑跑完才讀數。

## 驗收標準（能打回的才叫標準）
1. **BUG-1**：零進度状态下鎖注記顯示數字＝該模組單元總數（Playwright 實測，非 DOM 存在判）；新斷言進雙殼表，連跑五連零紅（含既有 17 斷言回歸）。
2. **搬入**：site/landing/tmias191/index.html＋assets/ 三檔齊（sha256 與 MrBeast 源對帳，唯一允許差異＝canonical/og:url/og:image 三行＋頁內相對路徑）；框架層（pages/、assets/css、assets/js、courses.yml）零 diff。
3. **canonical/og 一致性**：grep 可驗——canonical、og:url、og:image 三者全部指向部署基準路徑（部署前＝佔位值佔位路徑，部署後＝實際 URL）；JSON-LD parse 通過；CTA destination 仍唯一（surveycake 計數與搬入前一致）。
4. **上線閘（Zack 手動段完成後驗）**：公網 URL curl 200＋Linespider UA 抓 og:image 路徑回 200（robots.txt 不得 Disallow assets）＋GSC 驗證截斷＋sitemap 提交＋請求收錄各留痕（截圖或截圖存檔路徑落盤）。

## 依賴順序
BUG-1（獨立，先修）∥ 搬入（等 canonical 目標定案——本檔已鎖）→ 部署（人手）→ 上線閘驗證。
域名註冊等待期＝可並行做 BUG-1＋本機驗收。
