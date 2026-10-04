# Cloudflare Registrar 註冊 .com 研究（workspace: 2026-11-15 北區醫美工作坊・qqhairdoctor.com）

開放決策代號：
- **(c)** Cloudflare Registrar 註冊 .com 的實際成本價（現價與 2026-11 起調價）
- **(d)** WHOIS privacy 預設行為
- **(e)** auto-renew 預設行為（dashboard 與 API 路徑預設不同）
- **(f)** registrar lock（registrar lock 預設狀態與解锁流程）

條目為 append-only；每條 = URL / tier / argument（一句）。Tier 定義：primary = 廠商官方文件／官方條款、經本輪直接抓取驗證的頁面本體；secondary = 博客、轉述、廠商自述案例。所有 URL 均於 2026-10-04 實際抓取或經搜尋快取確認存在且內容如所述。

---

## 條目

### Decision (c) — .com 成本價

- **URL**: https://www.cloudflare.com/domains/
  **tier**: primary（Cloudflare 官方 Registrar 產品頁，經搜尋快取確認標題與摘述相符）
  **argument**: (c) 官方承諾「at cost——註冊、轉移、續費永遠 ≤ 註冊局＋ICANN 收我們的價」，註冊費＝成本價零加價，所以 .com 的價格完全由 Verisign 批發價＋ICANN 交易費決定，選 Cloudflare 等於鎖定了「市場最低可能價」。

- **URL**: https://www.cloudflare.com/learning/dns/how-much-does-a-domain-name-cost/
  **tier**: primary（Cloudflare 官方學習中心頁面，經搜尋快取確認存在且內容如所述）
  **argument**: (c) 官方明言對標準與 premium 域名提供「透明、at cost 的價格，註冊時與續費時一致」——沒有首年低價、續費跳價的行銷套路，費用可預期性正是本題要的。

- **URL**: https://www.cloudflare.com/application-services/solutions/low-cost-domain-names/
  **tier**: primary（Cloudflare 官方產品頁 FAQ，經搜尋快取確認存在且內容如所述）
  **argument**: (c) FAQ 明文「以成本價出售與續費、無加價無隱藏費」；但注意 Cloudflare 官方**沒有公開價格表**，實際報價以 dashboard／域名搜尋頁即時報價為準——以下具體數字均来自 secondary 來源的實讀值。

- **URL**: https://dev.to/301st/the-com-price-rises-on-1-november-lock-todays-for-up-to-ten-years-2epn
  **tier**: secondary（第三方博客，引用 Verisign 2026-04-23 季報與 ICANN 費表，數字鏈條完整）
  **argument**: (c) 具體數字：現價＝Verisign 批發 $10.26＋ICANN $0.20＝**$10.46/年**（Cloudflare 公開域名搜尋 2026-09-19 實示 $10.46）；Verisign 已公告 2026-11-01 起批發價調至 $10.97（成本 floor → $11.17），且 2027–2029 每年最多再調 7%（合約允許的最後四個調價年）——若預期長期持有 qqhairdoctor.com，現在一次買多年比逐年續費便宜，且 Cloudflare 續費按「續費當時的註冊局價」計價。

- **URL**: https://stackvaluelab.com/com-domain-price-increase-november-2026
  **tier**: secondary（第三方價格分析，交叉對照 Verisign 季報、ICANN 費頁、Porkbun/Namecheap 公開價，2026-09 實讀）
  **argument**: (c) 交叉驗證同一組數字（at-cost floor $10.46 → 2026-11-01 起 $11.17；7%／年調價至 2030），並對照同級競品 Porkbun $11.08、Namecheap 續費 $18.48、GoDaddy $18.99——本專案對 .com 年費的合理預期：現購 $10.46/年，2026-11 起 $11.17/年，逐年上浮到 2030 約 $15/年。

### Decision (d) — WHOIS privacy 預設行為

- **URL**: https://developers.cloudflare.com/registrar/account-options/whois-redaction/
  **tier**: primary（Cloudflare Registrar 官方文件，本輪直接抓取全文）
  **argument**: (d) WHOIS privacy 預設開、免費、無法關（「redacts by default, if permitted by the registry」）：註冊人姓名／email／地址顯示為「Data Redacted」，但州／省與國家兩欄依 ICANN 政策仍公開；官方另有表單代轉訊息給註冊人（rdap.cloudflare.com 為官方查詢入口）。

- **URL**: https://developers.cloudflare.com/registrar/get-started/register-domain/
  **tier**: primary（Cloudflare Registrar 官方註冊流程文件，本輪直接抓取全文）
  **argument**: (d) 註冊流程確認：聯絡人資料必填（姓名/email/電話/地址全要真實，僅 Organization 選填），送出後「personal information is redacted when permitted by the registry」——隱私保護不影響你要填真實聯絡人（工商登記名與地址會被存在雲側的權威紀錄裡）。

### Decision (e) — auto-renew 預設行為

- **URL**: https://developers.cloudflare.com/registrar/account-options/renew-domains/
  **tier**: primary（Cloudflare Registrar 官方文件，經搜尋快取確認全文；內容與官方 GitHub cloudflare-docs 倉庫同檔核對一致）
  **argument**: (e) Dashboard 路徑預設：**auto-renew 預設開**（「enrolls your domain to auto-renew by default」），到期前約 30 天開始扣款，失敗重試至到期前一天，扣款用帳戶預設付款方式；要退出需在到期前 ≥30 天手動關掉——扣款卡要保持有效，失敗會發 email 通知再試三次。

- **URL**: https://developers.cloudflare.com/registrar/registrar-api/
  **tier**: primary（Cloudflare 官方 Registrar API 文件，經搜尋快取確認內容；與 API reference create-registration 頁一致）
  **argument**: (e) 注意坑：**走 API 註冊時 auto_renew 預設是 false（明確 opt-in）**，與 dashboard 預設相反；privacy_mode 走 API 時預設 redaction（支援時）、locked 為 true——若未來用腳本註冊 qqhairdoctor.com，要手動把 auto_renew 設成 true。

### Decision (f) — registrar lock

- **URL**: https://developers.cloudflare.com/registrar/account-options/transfer-out-from-cloudflare/
  **tier**: primary（Cloudflare Registrar 官方「轉移出」文件，本輪直接抓取全文）
  **argument**: (f) 域名在 Cloudflare 預設上鎖（clientTransferProhibited），要轉出得先在 dashboard 手動 Unlock 才拿得到 auth code；轉出被拒時 Cloudflare 會重新上鎖——預設即防 hijack 狀態，不用額外開。

- **URL**: https://developers.cloudflare.com/registrar/get-started/transfer-domain-to-cloudflare/
  **tier**: primary（Cloudflare Registrar 官方轉入文件，經搜尋快取確認內容）
  **argument**: (f) 反向限制要注意：ICANN 規則下**註冊未滿 60 天的域名不能轉出**，且改動註冊人姓名／組織／email 會觸發 60 天轉出鎖（部分註冊商可 opt-out）；另 Cloudflare Registrar 要求域名必須用 Cloudflare 權威 DNS（full setup），註冊＝綁 DNS，這是選註冊商時就要接受的綁定。

- **URL**: https://developers.cloudflare.com/registrar/account-options/
  **tier**: primary（Cloudflare Registrar 官方總覽頁，經搜尋快取確認標題與摘述相符）
  **argument**: (f)(d)(c) 官方總覽一句話總結：「redacted WHOIS information by default ＋只收註冊局收我們的錢，no markup, no surprise fees」——三個預設行為（privacy 開、at-cost）在同一官方頁得到確認。

---

## 搜了但沒有（searched-and-absent）

- **Query**: Cloudflare Registrar 官方是否有公開的 .com 價格表頁（pricing table／pricing page）; **searched via**: web search（cloudflare.com/application-services/pricing 及官方 docs 域名，後者直接抓取回 404）; **result**: 官方只有「at cost 無加價」的政策性聲明頁，無公開價格表；具體價格只存在於 dashboard／域名搜尋即時報價與第三方實讀記錄——本檔的具體數字據此全部標 secondary。
- **Query**: Cloudflare Registrar 官方文件中「registrar lock 預設開」的直接陳述句; **searched via**: web search（developers.cloudflare.com/registrar 全站）＋直接抓取 transfer-out-from-cloudflare 全文; **result**: 官方文件只從「轉出流程要先 Unlock／被拒會 reapply the registrar lock」間接坐實預設上鎖，另 API create-registration 回傳例中 locked: true；無單獨的「Domain lock」說明頁（docs 左欄無此頁，舊 URL 已 404）。
