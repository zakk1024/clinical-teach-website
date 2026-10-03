# 派工單 A — landing 搬入（frontend-developer）

開單時間：2026-10-01（預登檔 PRE-REGISTRATION-run9.md 執行鏈 #2）
預判觸碰：2–4（中——搬移＋佔位改寫＋雙向核）。跑完對帳，中場不蓋章。

## 交付物（一句話）
把 MrBeast workspace 的 promo-191 landing 整包搬入本 repo `site/landing/tmias191/`，佔位改寫，其餘內容零改動。

## 來源
`/Users/zakk/Desktop/MrBeast/SEO/.scratch/promo-191/deliverable-landing/`（index.html＋assets/＋spec.md；四閘已過、DATA PENDING 已清、OG 已生成）

## 驗收標準（能打回的才叫標準）
1. `site/landing/tmias191/index.html`＋`assets/` 全部檔存在，檔數＝來源檔數（雙向核：A−B 與 B−A 皆空）。
2. 佔位改寫：canonical、og:url、og:image 三者全部＝`https://qqhairdoctor.com/landing/tmias191/`（assets 路徑相對；grep 可驗：`vesuyan.com` 零出現）。
3. Event JSON-LD parse 不破（python json.loads 過）。
4. 單檔規格不破：零外部 JS、零外部字體鏈結（promo-191 spec 規格，搬入前後 grep 計數一致——只數真標籤，不數註解）。
5. 框架層零改動：git diff 範圍只允許 `site/landing/` 新增；courses.yml、site.js、現有頁檔零 diff。

## 边界
- 不動 qcc 佔位、不動 SurveyCake 連結（上線後的事）。
- 不動 spec.md 以外的來源檔內容；搬＝複製＋改佔位字串，其他一字不動。
