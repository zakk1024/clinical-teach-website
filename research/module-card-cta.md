# Research — 模組卡重複連結問題（run 6 grill，2026-09-10）

問題（使用者提出）：模組卡的標題連結與「下一步：〈同名文字〉」按鈕指向同一頁——同一張卡兩個完全相同的連結，按鈕無資訊量。

## 來源（實抓／搜尋，無編造）

1. **URL**: https://tryhackme.com/path/outline/beginner — **tier: primary（實抓）**
   發現：Section → 課程清單，每個 module 是**單一**可點擊項目（圖示＋名稱＝同一連結）；進度以狀態圖標標示在同一行，無第二個指向同處的死連結。
2. **URL**: https://www.kodekloud.com/learning-paths — **tier: primary（實抓）**
   發現：每張 path 卡恰好一個連結（整卡即連結）；卡上放的是標題之外的資訊（課程數、時數）。
3. **URL**: https://www.coursera.org/learn/packt-mastering-quickbooks-online-eslmf（＋specializations 頁）— **tier: secondary（搜尋摘錄）**
   發現：模組卡是「展開大綱」動作（展開 what you will learn），與註冊/繼續動作分離；course 層 Continue 只在有進度時出現。
4. **Duolingo 路徑設計**（見 research/progress-display.md 來源 #1）— **tier: secondary**
   發現：每節點單一入口，進度畫在節點自身——動作與資訊同體不分離。
5. **UX pattern 共識（搜尋所獲，轉述）** — **tier: tertiary**
   course card 模式：標題＋簡述＋**單一 CTA，且 CTA 文字由狀態驅動**（未開始＝Start、有進度＝Continue）。二個同向連結＝死像素。

## 綜合（只有結論，無編造）
五家最大公约：**卡上第二元素必須攜帶標題沒有的資訊（進度、時間、狀態）才配存在**。本站「下一步」按鈕複誦標題＋同一連結＝五家全滅測試失敗——它當初是從 Q2 TryHackMe 映射表搬來的（映射寫「下一步按鈕」），但 TryHackMe 的 Continue 只在「你正在這裡」的節點出現，是狀態驅動——我們搬了按鈕、沒搬狀態。

## 選項（送審）
- A（建議）狀態驅動：按鈕只服務 resume——只在進度 0–100% 的卡出現、文字「繼續・剩下 N 項」；無進度卡無按鈕、整卡可點。
- B 資訊化常駐：按鈕留每張卡，文字自帶資訊（剩下 N 項未完成）。
- C 砍掉：整卡可點、標題唯一入口（TryHackMe 原法）。
