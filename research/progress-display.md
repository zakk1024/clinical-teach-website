# Research — 進度顯示區塊重設計（run 5 grill，2026-09-09）

問題（使用者提出）：全局印章牆把六門課的模組拍平成一排圓圈，三個「01」連發，學員不知道哪顆是哪門課的。

## 來源

1. **URL**: https://blog.duolingo.com/new-duolingo-home-screen-design/ — **tier: primary**
   **論證**: Duolingo 官方：新版把技能樹改成單一路徑，一個圓圈＝一個技能的一級——圓圈編號可讀是因為**路徑本身就是單課程線性序**。本站把六門課的模組拍平進同一排，等於把六條路徑疊成一條——編號衝突是結構性的，不是樣式問題。支援「進度歸課程、不拍平」。
2. **URL**: https://forum.duome.eu/viewtopic.php?t=29574 — **tier: secondary（轉述）**
   **論證**: 社群投訴 /progress 與主頁 crown 數不一致——兩個地方顯示同一個進度就會漂移。支援「進度只畫在一個地方」，反對「全局牆＋課程卡進度條」並存。
3. **URL**: https://tryhackme.com/resources/blog/new-end-user-assignments/ — **tier: primary**
   **論證**: TryHackMe 自己的管理頁用**狀態標籤**（Not Started／In Progress／Complete）掛在每個項目上，不是靠一排抽象圓點。Q2 锁了 TryHackMe 互動範式——它本家的進度呈現其實是 per-item 狀態，圆點牆不是它最強的部分。
4. **Searched-and-absent**: 「multi-course progress indicator per-course grouping design」在設計部落格圈無專門論證文章（Duolingo 改版的社群反彈是最接近的證據，見 #2）。

## 落點（供逼問）

編號衝突的根因是結構（六條課內序號拍平共筆），三個方向：進度歸課程層（每課一行）、進度只留一處（砍全局牆）、或給圓圈加課程前綴（表面_patch_）。Streak 連擊的存廢是另一刀——取決於學員回訪頻率（Feynman 已點破：一課一學的站，連擊大概率永遠只有兩個亮點）。
