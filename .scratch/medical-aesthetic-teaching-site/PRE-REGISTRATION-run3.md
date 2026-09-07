# 第 3 跑（執行輪）事前登記 — 媒體管線＋schema＋NeoFilera 課（2026-09-07 派工前寫死）

執行官：mentor（schema/渲染器／本輪裁判）＋兩路 leaf 執行官（runtime 同槽 qwen38-uncensored @ 127.0.0.1:8085，憑據同前跑格式）
覆核官：taleb（驗收閘）

## 任務（全部依已鎖決策 Q0b/Q3a/Q4a/Q5a/Q6a/R2/R3a，見 DECISIONS-round2-neofilera.md）
1. 媒體管線：heic 轉檔（sips）、影片重轉 h264 <10MB（僅超標者）、Q5 命名、素材搬入 site/assets/media/、產出 MANIFEST CSV（六欄：source/site/size_MiB/format/consent_flag/tier）。
2. Schema：課程 JSON 加 media[]（type＋三欄门槛：來源路徑/瀏覽器可食格式/授權旗標）＋ evidence_tier ＋ audience_tier（兩欄正交，R3 鎖）。
3. NeoFilera 課 JSON 草稿（grounded in research/neofilera.md＋yujin 03_RETRIEVAL_NOTES）——過使用者審核關才入站。

## 三條預測（跑前寫死）
1. 預測觸碰次數＝**區間 ≤4**（任務難度：中高——首次打破渲染器零改動斷言＋媒體管線是新建物）。分岔：≤4＝工具，6＝官僚機構。
2. 管線會踢出至少一個執行官交付物的**機械判準**：媒體檔案數≠MANIFEST 行數、或 heic 殘留站體、或 size 欄無單位制——任一即踢。
3. 內容草稿會被審核關擋的項：**引用分層標「外推」的宣稱 ≥1 條**（無品牌 RCT，同家族外推是結構性的）。

## 閘
- 機械判準（先寫死）：`site/assets/media/` 檔案數 == MANIFEST 行數；heic 零殘留（轉檔完成）；每檔 <10MB；命名全部符合 `neofilera_(ba|vid|ana)_\d\d`；測試加媒體斷言綠（渲染器渲染 media[]、evidence_tier/audience_tier 分開渲染）。
- 使用者審核關：NeoFilera 內容草稿過目才入站（照老規矩）。
- Consent 閘（聯署令）：before/after 進免費層——使用者已蓋章（雙向門權利人裁決），書面文件本體擋發佈路不擋開發路。

## 範圍裁定（派工單寫死）
- 本課 media 範圍＝yujin manifest 點名的素材：ba 3 張 JPG＋2 HEIC（免費層櫥窗）、影片 3 支（12/13/30s 已達標轉出檔；18/17/35s 舊檔超標者重轉）、解剖圖 2 張 user-owned PNG（IMG_2331/2332）；出版社版權圖（Elsevier/Springer/WK）**只留引用座標、不入站**（R2 已鎖重繪）。

---

## 結帳（2026-09-07 跑後，實測）
- **機械判準**：檔案數 10==MANIFEST 10 行✓｜heic 零殘留✓｜全部 <10MB（最大 1.27 MiB）✓｜命名正則全中✓｜跨 6 把獨立尺零分歧（預測 #2 反面：無踢出）。
- **預測 #1（觸碰 ≤4）**：實際 4——① 渲染器＋CSS（M14）② schema media[] 填充＋audience_tier 正交欄 ③ harness 加媒體斷言 ④ 伺服器重啟。踩線過，工具區間內。
- **預測 #3 落空（誠實記帳）**：預測「外推宣稱 ≥1 條會被審核關擋」——使用者直接全過，零擋案。預測方向對（外推是結構性的，草稿含 6 條 literature-extrapolated），但審核關的門沒踢到人。記：預測的是「會被擋」，不是「存在」——預測落空也算帳。
- **範圍修訂（七把尺收斂後）**：原範圍行「3 支重轉」對的是 intermediate 目錄；派工單指令「統一從原片重轉」直接覆蓋，實際交付 3 支全部從原片重壓（0.93/1.00/1.21 MiB），7 支未動——因為它们在派工單範圍外（只有 manifest 點名的 3 支入站）。改單三項（3→8／17.5 挪組／checksum 欄）：前兩項被「統一重轉」指令架空、無實際影響；checksum 欄已補（第 7 欄 SHA-256）。
- **heic 朝向**：機械判（像素本體 3442×4590 直式）＋人眼判（Feynman）雙綠。
- **Consent**：使用者裁「文件在診所保險櫃，直接過關」——ba 五旗從 verbal-pending 翻回 user-granted（這次是裁決，不是預填）。
- **測試**：runner 16/16（原 14＋M14 媒體斷言×2）＋瀏覽器冷快取視覺核對另記。
