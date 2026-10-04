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

## 執行鏈（研究閘關門＋使用者 Round 1 答完才開跑）

## Round 1 鎖定（2026-10-03，使用者答覆）
- **GitHub repo 能見度＝Public**（課程站骨架＋落地頁都會在公開 repo；GitHub Pages 商業排除條款不適用——GitHub 只當 source repo，主機＝Cloudflare Pages，推論依據＝既有 research 檔 GitHub Pages 條款條目）。
- **註冊年限＝1 年＋auto-renew 開**（成本價無預付折扣，隨時可轉出）。
- 登入方式：使用者跳過未答——預設路徑＝使用者自己在瀏覽器登好 Cloudflare＋Google，登完說一聲（vault 流程為備援）。
- 部署路徑（Git integration vs Direct Upload）：等 R1 研究落盤後 Round 2 拍。

1. （使用者手）Cloudflare 帳號＋註冊付款；（使用者手）GSC Google 帳號登入。
2. devops-automator：註冊表單填寫＋DNS（登機口＝使用者付完款）。
3. seo-specialist：GSC TXT 驗證＋sitemap＋請求收錄。
4. devops-automator：Pages 專案（部署路徑等 Round 1 拍）。
5. 執行官覆核：dig/curl 獨立覆核（不採自報）＋截圖三張落 .scratch/run10-。
