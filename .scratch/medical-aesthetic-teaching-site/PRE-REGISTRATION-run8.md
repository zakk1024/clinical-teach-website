# 第 8 跑（渲染＋繪圖輪）事前登記 — nose 課 M2/M3 進站（2026-09-11 派工前寫死，commit 先於派工）

## 輸入（已鎖）
- 兩份草稿已獲使用者批准（2026-09-11 房間裁決）：deliverables/nose-m2-draft.md、nose-m3-draft.md。
- 本跑範圍：註冊表加 nose 課列（group=thread-lift，data 層改動由執行官親自動）；內容 JSON 由起草 agent 產；10 張重畫 SVG 由繪圖 agent 產，2 張 CC-BY（A6/A10）留佔位待真實圖檔入庫（素材授權分級規則）。

## 觸碰面（跑前寫死）
預登檔／courses.yml（註冊表 1 行）／site/content/courses/nose-thread-lift.json（僅含已批准兩模組，不空殼佔位）／assets/media/illustrations/ 10 張 SVG（每張 caption＋來源 DOI 寫進檔頭註解）／測試表不動（註冊表驅動的渲染由既有斷言自動涵蓋——若涵蓋不到即預測 #3 兌現）。

## 三條預測（跑前寫死，落空不改寫）
1. 觸碰次數＝區間 **≤8**。
2. **基線預期（run6 教訓買進）**：新增断言或新增渲染面首跑至少紅一次。
3. 10 張重畫 SVG 至少 1 張的來源標註對不上 research 落盤檔（agent 畫圖愛自己加比例數字）——驗收逐張核 DOI。

## 機械判準
- 註冊表渲染：nose 課落對組（既有 M15 涵蓋）。
- 每张 SVG 檔頭有 DOI 註解且能在 research/nose-thread-lift.md 溯源。
- 內容 JSON 每個引用分層標籤在檔（文獻層/臨床經驗層）。
## 人眼判
- 使用者開瀏覽器看 nose 課頁＋圖，點頭才算渲染完成。
