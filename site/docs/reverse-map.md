# 反向對帳鏡像（站上互動 → M-ID）

映射表正本在 `../../.scratch/medical-aesthetic-teaching-site/deliverables/mapping-tryhackme.md`（已落盤禁改），
此檔為同步回填鏡像——站上每個互動元件的穩定 ID 都指回映射表某行，指不回去＝判輸。

| 站上互動實作（穩定 ID） | 對應 M-ID |
|------------------------|-----------|
| `m1-check-*` 標記完成核取框、`m1-progress-*` 細進度條＋百分比（localStorage `mats-progress`） | M1 |
| `m2-submit-*` 提交即場判定＋單次 200ms 回饋動畫（`--accent`/`--warn`，非綠） | M2 |
| `m3-lock-*` 模組鏈硬門檻鎖提示（前一模組達標前顯示鎖＋剩餘題數） | M3 |
| `content/progress.json` `points` 欄保留、UI 不渲染數值 | M4（棄·簡化落點） |
| `m5-seal-*` 單色線條 SVG 印章槽，達標點亮＋單次 300ms 描邊 | M5 |
| ~~`m6-streak` 連擊日曆~~ → **Q10 裁決（2026-09-09）：砍除**——回訪假設不可觀測（使用者裁決，Feynman 不可觀測論＋Taleb 可逆性論）；測試燈 M6 連帶下架（Elon 記帳） | M6→下架 |
| `content/progress.json` `users` 欄佔位、無排行榜 UI | M7（棄·落點） |
| `m8-hint-*`／`m8-ladder-*` 三級提示階梯（L1 概念回顧錨點→L2 改述→L3 揭示），答錯自動展開 L1 | M8 |
| `m9-drop-*`／`m9-tray-*` 拖曳配對＋單選/是非題型（`m2-input-*`），客戶端判定 | M9 |
| `m10-path-cards` 註冊表驅動路徑卡＋編號＋下一步按鈕＋整體進度條 | M10 |
| `m11-bookmark-*` 細線書籤圖標（localStorage `mats-bookmarks`）＋首頁收藏架 `m11-bookmark-shelf` | M11 |
| `m12-scroll-progress` 頂部 2px `--accent` 閱讀進度線＋章節單次淡入（150–300ms） | M12 |
| `m13-cert-entry`／`m13-certificate` 全模組達標→證書入口（姓名 localStorage `mats-name`，列印為 PDF） | M13 |
| 無凍結卡 UI、無補救道具欄位（M6 斷一天即斷連） | M14（棄·落點） |
| `course-thread-lift.json` 測驗互動：`m2-input-thread-lift-basics-q1/q2`＋`m2-submit-*` 即時判定、`m8-ladder-*` 三級提示、`m9-drop/tray-match-1` 拖曳配對（皆由框架引擎渲染，內容層零框架改動） | M2＋M8＋M9 |
| `collagen-stimulator-full-face`：`m2-q1`–`m2-q3`（單選＋是非）、`m8-ladder-*`/`m8-hint-*` 提示階梯、`m9-match-1` 拖曳配對 | M2／M8／M9（課程 3 回填） |
| `nose-thread-lift`：`m2-q1`／`m2-q2`（單選＋是非，答錯展開提示階梯）、`m8-ladder-*`/`m8-hint-*` 三級提示、`m9-match-1` 拖曳配對 | M2／M8／M9（課程 1 回填） |
