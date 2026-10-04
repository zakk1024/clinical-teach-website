# 第 10 跑（域名註冊＋DNS＋GSC＋Pages 部署——browser 執行輪）事前登記（2026-10-03 開跑前寫死）

## 閘門裁決
- 執行模型檔位：本機槽（runtime 層 model＝qwen38-uncensored @127.0.0.1:8085，本機唯一有實測數據檔位）＝甜區直通組隊。
- 任務軸：多步驟＋要先研究再執行（註冊→DNS→GSC→部署→收錄）→ 組隊增益大。過閘。
- browser 控制權限：使用者明確授權（2026-10-03）；密碼/驗證碼/付款＝使用者手（vault／UI），specialist 不得代猜密碼。

## 分診（交付物→崗位，綁得上才留）
| specialist | 交付物 | 驗收標準（能打回） |
|---|---|---|
| devops-automator | ①qqhairdoctor.com 註冊完成（Cloudflare Registrar）＋nameserver 生效（dig NS 回 cloudflare）；②Pages 專案上線（production URL 可達，200） | ①dig +trace/whois 截圖 ②curl -w 200＋截圖 |
| seo-specialist | GSC 域名資源驗證通過（TXT）＋sitemap 提交＋landing URL 手動請求收錄 | 三張截圖落 .scratch/run10-（驗證綠＋sitemap 已提交＋inspection requested） |
- 出局記錄：marketing 部其餘崗位無交付物可綁；frontend-developer 交付物已由 run9 派工單 A 結帳。

## 研究閘（一道開放決策一道委派，append-only，三欄格式）
- R1 research/cloudflare-pages-git-integration.md：免費層支援 private GitHub repo Git integration？Direct Upload 限額？（決定部署路徑的證據）
- R2 research/cloudflare-registrar-com.md：.com 成本價、WHOIS privacy 預設、auto-renew、registrar lock（決定註冊流程與續費假設的證據）
- R3 research/gsc-domain-property.md：Domain property vs URL-prefix property——域名驗證涵蓋全子網域／協定變體（決定 GSC 資源類型的證據）
- R4 不新派：corollary from existing research/hosting-and-deployment.md（GitHub Pages 商業排除＝Pages 託管的條款，GitHub 當 source repo＋Cloudflare 當主機不觸發之）——引用已抓過全文的 primary，論證欄寫明是推論。

## 預測（跑前寫死，落空不改寫）
1. 三道研究委派觸碰各＝1（返工＝0；基線：新斷言首跑必紅——任一道返工即兌現）。
2. 返工迴路是否真的打回過東西（未測格結果變數）：預測＝沒有（三交付物皆機械可驗、人對口）。
3. 註冊費用落在 US$9–12/年成本價區間（Cloudflare at-cost 宣稱；whois 註冊商欄最終為準——若註冊商非 Cloudflare 即落空）。

## 研究閘對帳（2026-10-04，三委派首跑完成後讀數）
- 預測 1（觸碰各＝1；基線＝首寫含未驗證 URL 即兌現）：觸碰各 1 兌現；基線落空（三檔抽驗無 unverified 條目）——照規矩不改寫。
- 預測 2（返工迴路打回過東西）：預測＝沒有；實測＝零打回——**落空**，照規矩不改寫。
- 預測 3（US$9–12/年）：**中**——實測現價 $10.46（Verisign 批發 $10.26＋ICANN $0.20，secondary 多源一致）；**新事實：2026-11-01 起 Verisign 調至 $11.17，合約允許 2027–2029 每年最多 +7%**。
- 研究帶回的行動級發現：①R1＝免費層支援 private repo Git integration（Q1 已鎖 Public，路徑不受限）＋**Direct Upload 專案不能事後切 Git integration（單向門）**。②R2＝Cloudflare 註冊域名必須用 Cloudflare 權威 DNS（綁定，本案無成本——本來就選了 CF）；API 註冊 auto-renew 預設 off（dashboard 路徑預設 on——我們走 dashboard，用戶已拍 auto-renew 開）。③R3＝Domain property 涵蓋全子網域＋協定變體、TXT 加 apex、驗證後記錄不能刪；Cloudflare Pages 不自動產 sitemap——sitemap.xml 要自己進 repo；≤500 頁站可直接 request index，正路仍是 sitemap＋提交。
- 執行鏈更新：seo-specialist 交付物加 sitemap.xml（＋robots.txt）進 repo 根；執行鏈 #4 的「push」語義＝Git integration（GitHub public repo 建 remote → Pages 連 GitHub → push 即部署）。


## Round 2 鎖定（2026-10-04，使用者答覆）
- **Q9 重開後維持原案：註冊 1 年＋auto-renew**——R2 證據（2026-11-01 起 Verisign $10.46→$11.17、2027–2029 可逐年 +7%）打到「多年預付無折扣」前提，多年可鎖價；使用者知情後仍選 1 年（保轉出自由度，差價認了）。修正已傳播：預登預測 3 讀數不變。
- **Q10 登帳＝vault 流程**：agent 發起，密碼/驗證碼/付款在隱藏式提示由使用者輸入，密碼不過對話。
- **Q11 收尾歸執行方**：specialist 跑（GSC TXT 驗證、Pages 建專案、sitemap 提交、請求收錄、截圖憑證落檔）；使用者的手只出現在登入/付款/驗證碼步驟。
- 研究判死題（非推薦，無剩餘 trade-off）：部署路徑＝Git integration（Direct Upload 不能事後切回——單向門）；GSC＝Domain property（TXT 加 apex，涵蓋全子網域，驗證後記錄不可刪）。
## 執行鏈（研究閘關門＋Round 2 答完已開跑）

- **GitHub repo 能見度＝Public**（課程站骨架＋落地頁都會在公開 repo；GitHub Pages 商業排除條款不適用——GitHub 只當 source repo，主機＝Cloudflare Pages，推論依據＝既有 research 檔 GitHub Pages 條款條目）。
- **註冊年限＝1 年＋auto-renew 開**（成本價無預付折扣，隨時可轉出）。
- 登入方式：使用者跳過未答——預設路徑＝使用者自己在瀏覽器登好 Cloudflare＋Google，登完說一聲（vault 流程為備援）。
- 部署路徑（Git integration vs Direct Upload）：等 R1 研究落盤後 Round 2 拍。

1. （使用者手）Cloudflare 帳號＋註冊付款；（使用者手）GSC Google 帳號登入。
2. devops-automator：註冊表單填寫＋DNS（登機口＝使用者付完款）。
3. seo-specialist：GSC TXT 驗證＋sitemap＋請求收錄。
4. devops-automator：Pages 專案（部署路徑等 Round 1 拍）。
5. 執行官覆核：dig/curl 獨立覆核（不採自報）＋截圖三張落 .scratch/run10-。


## 執行結果（2026-10-04 收單）
- **註冊**：qqhairdoctor.com ACTIVE、auto-renew ON、到期 2027-10-04（使用者付款）。
- **部署**：GitHub `zakk1024/clinical-teach-website`（Public）→ Cloudflare Pages Git integration（production=main、build 空、output=site）→ custom domain `qqhairdoctor.com` **Active＋SSL**（Cloudflare dashboard 截圖為證）。
- **獨立覆核（不採自報）**：`dig TXT` 1.1.1.1/8.8.8.8 雙 resolver 一致＝Google 經 Domain Connect 親手寫入的 `google-site-verification=zcRJ0f8w…`；`curl` 落地頁/sitemap/robots 全 200。
- **GSC**：Domain property `sc-domain:qqhairdoctor.com` 驗證通過（GSC 介面解鎖完整功能、顯示「資料處理中，請等約一天」）。
- **Sitemap 提交**：`https://qqhairdoctor.com/sitemap.xml` →「已成功提交 Sitemap」toast＋列表列出現（狀態列初始顯示「無法擷取 0/0」——新提交常態，等 Google 排程抓取）。
- **手動請求收錄**：landing URL 網址審查 →「已要求建立索引，已將網址加入優先檢索佇列」。
- **截圖憑證**：screenshots/2026-10-04_live-landing-qqhairdoctor.png（落地頁本體）、gsc-pending-txt-live.png、gsc-sitemap-submitted.png、gsc-index-requested.png（四張，多一張不罰）。
- **預測對帳**：R2 價格預測命中（$10.46 落在 $9–12 區間）；返工預測落空（GSC 驗證對話框重跑 3 次才算數——但最終全靠 Domain Connect＋背景驗證，手動流程是繞路）。
