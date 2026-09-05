# Medical-Aesthetic Teaching Site（靜態骨架）

本機靜態站＋git repo，無後端（事前登記 Q5）。互動機制全部對應
`.scratch/medical-aesthetic-teaching-site/deliverables/mapping-tryhackme.md` 的 M-ID，
反向對帳見 `docs/reverse-map.md`（.scratch 已落盤檔禁改，故回填鏡像於此）。

## 結構（框架層 vs 內容層）
- `courses.yml` — 課程註冊表（索引）。**新增一門課＝content/courses/ 加一個檔案＋此檔加一行；框架層（pages/、assets/）零改動。**
- `content/courses/*.json` — 課程內容（模組→單元→測驗，題庫 schema 照映射表 M9）。
- `content/progress.json` — M1/M4/M7 資料層 schema（運行時真資料存 localStorage：`mats-progress`、`mats-bookmarks`、`mats-streak`、`mats-name`）。
- `content/paths.yml` — 路徑編排（M10 資料層，M3 順序陣列）。
- `pages/index.html` — 首頁骨架（M5 印章槽、M6 連擊、M10 路徑卡、M11 收藏架、M12 進度線）。
- `pages/course.html` — 教學頁骨架（內容由 JSON 渲染；M1/M2/M3/M8/M9 互動）。
- `pages/certificate.html` — M13 證書。
- `assets/css/site.css` — 全站樣式（視覺基線：淺底＋單一 `--accent`＋無襯線＋150–300ms 單次動效；無終端機元素、無等寬字體族、無黑底綠字）。
- `assets/js/site.js` — 互動引擎（只認 `data-mid="M<n>"` 標記，不認具體內容）。

## 互動元件穩定 ID 規則
`m1-check-*`、`m1-progress-*`、`m2-input-*`／`m2-submit-*`、`m3-lock-*`、`m5-seal-*`、
`m6-streak`、`m8-ladder-*`／`m8-hint-*`、`m9-drop-*`／`m9-tray-*`、`m10-path-cards`、
`m11-bookmark-*`／`m11-bookmark-shelf`、`m12-scroll-progress`、`m13-cert-entry`。

## 跑法
`cd site && python3 -m http.server 8777` → http://127.0.0.1:8777/pages/index.html

> 注意：雙擊直接開 harness.html 會白頁（file:// 沒起伺服器）。正確跑法：終端 A `python3 -m http.server 8777 --directory site`（從 repo 根目錄起），終端 B 跑 `python3 site/tests/run_harness.py`。
