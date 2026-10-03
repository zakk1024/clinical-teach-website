/* ============================================================
   site.js — 全站互動引擎（框架層）
   每個元件都由 data-mid="M<n>" 標記，M-ID 必須存在於
   .scratch/.../deliverables/mapping-tryhackme.md 的映射表行內（反向對帳）。
   純 localStorage＋靜態 JSON，無後端。
   ============================================================ */
"use strict";

const LS_PROGRESS = "mats-progress";   // M1
const LS_BOOKMARKS = "mats-bookmarks"; // M11
const LS_STREAK = "mats-streak";       // M6
const LS_NAME = "mats-name";           // M13

function lsGet(k, d) { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } }
function lsSet(k, v) { localStorage.setItem(k, JSON.stringify(v)); }

/* ---------- M1：進度軌跡（localStorage＋即時重算進度條） ---------- */
function progressRecords() { return lsGet(LS_PROGRESS, []); }
function recordProgress(courseId, moduleId, unitId, checked) {
  const recs = progressRecords();
  const hit = recs.find(r => r.courseId === courseId && r.moduleId === moduleId && r.unitId === unitId);
  if (hit) hit.checked = checked; else recs.push({ courseId, moduleId, unitId, checked, points: 0 });
  lsSet(LS_PROGRESS, recs);
  renderProgress();
  renderLocks();
    renderCertEntryForCourse(courseId);
}
function moduleDone(courseId, moduleId) {
  const bar = document.querySelector(`div[data-mid="M1"][data-module="${moduleId}"][data-total]`);
  const total = bar ? Number(bar.dataset.total) : null;
  const recs = progressRecords().filter(r => r.courseId === courseId && r.moduleId === moduleId);
  const done = recs.filter(r => r.checked).length;
  return total != null ? done >= total : (recs.length > 0 && done === recs.length);
}
function renderProgress() {
  // Q9: 課程層狀態標籤（每課一個 aggregation，進度只畫這一處＋課頁原本的模組卡）
  document.querySelectorAll(".status-badge[data-course]").forEach(badge => {
    const cid = badge.dataset.course;
    const bars = [...document.querySelectorAll(`div[data-mid="M1"][data-course="${cid}"][data-total]`)];
    let doneM = 0, totalM = 0;
    bars.forEach(b => {
      const t = Number(b.dataset.total) || 0;
      const d = progressRecords().filter(r => r.courseId === cid && r.moduleId === b.dataset.module && r.checked).length;
      totalM++; if (t > 0 && d >= t) doneM++;
    });
    badge.textContent = doneM === 0 ? "Not Started" : (doneM >= totalM && totalM > 0 ? "Complete" : "In Progress");
  });
  document.querySelectorAll('div[data-mid="M1"][data-total]').forEach(bar => {
    const { course, module, total } = bar.dataset;
    const recs = progressRecords().filter(r => r.courseId === course && r.moduleId === module);
    const done = recs.filter(r => r.checked).length;
    const pct = total > 0 ? Math.round((done / total) * 100) : 0;
    bar.querySelector(".bar > span").style.width = pct + "%";
    bar.querySelector(".pct").textContent = pct + "%";
    // Q12: 狀態驅動按鈕——有進度才出現，文字帶資訊（五家最大公約：第二元素不複誦標題）
    const nx = document.querySelector(`.next-step[data-next="${course}:${module}"] a`);
    if (nx) {
      if (pct > 0 && pct < 100) { nx.style.display = ""; nx.textContent = `繼續・剩下 ${total - done} 項`; }
      else if (pct >= 100) { nx.style.display = ""; nx.textContent = `已完成・可重溫`; }
      else { nx.style.display = "none"; }
    }
  });
}

/* ---------- M3：模組鏈硬門檻（前一模組全達標才解鎖下一模組） ---------- */
function renderLocks() {
  const order = document.body.dataset.moduleOrder ? document.body.dataset.moduleOrder.split(",") : [];
  const courseId = document.body.dataset.course || "";
  order.forEach((mod, i) => {
    const card = document.querySelector(`.card[data-module="${mod}"]`);
    if (!card) return;
    const prev = order[i - 1];
    const locked = prev ? !moduleDone(courseId, prev) : false;
    card.classList.toggle("locked", locked);
    const note = card.querySelector(".m3-lock-note");
    if (note && locked) {
      // BUG-1 修：pending＝total−done（原實作只數已建立的未勾記錄，零進度時顯示 0 卻鎖著）
      const bar = document.querySelector(`div[data-mid="M1"][data-module="${prev}"][data-total]`);
      const done = progressRecords().filter(r => r.courseId === courseId && r.moduleId === prev && r.checked).length;
      note.querySelector(".m3-pending").textContent = bar ? Number(bar.dataset.total) - done : done;
    }
  });
}

/* ---------- M2：即時回饋（提交即場判定；錯→展開 M8 第一級） ---------- */
function gradeQuiz(quizEl) {
  const qid = quizEl.dataset.qid;
  const correct = Number(quizEl.dataset.answer);
  const fb = quizEl.closest(".quiz-q").querySelector(".feedback");
  const chosen = quizEl.querySelector('input[type="radio"]:checked');
  if (!chosen) { fb.textContent = "請先作答"; fb.className = "feedback show"; return; }
  const ok = Number(chosen.value) === correct;
  fb.dataset.result = ok ? "correct" : "wrong";
  if (ok) {
    fb.textContent = "✓ 正確";
    fb.className = "feedback ok show";
    const q = JSON.parse(quizEl.dataset.question || "null");
    if (q) recordProgress(document.body.dataset.course, quizEl.dataset.module, "quiz:" + q.id, true);
  } else {
    fb.textContent = "✗ 不正確——看看提示階梯";
    fb.className = "feedback bad show";
    revealHint(quizEl.closest(".quiz-q"), 1); // M8：答錯展開第一級提示
  }
}

/* ---------- M8：提示階梯（L1 概念回顧→L2 要點改述→L3 揭示答案） ---------- */
function revealHint(qEl, level) {
  const ladder = qEl.querySelector('[data-mid="M8"]');
  if (!ladder) return;
  for (let i = 1; i <= level; i++) {
    const h = ladder.querySelector(`.hint[data-level="${i}"]`);
    if (h) h.classList.add("shown");
    const b = ladder.querySelector(`button[data-level="${i}"]`);
    if (b) b.disabled = true;
  }
  ladder.dataset.opened = level;
}

/* ---------- M9：配對題（拖曳配對，客戶端判定→餵 M2 回饋） ---------- */
function initMatch(quizEl, matchEl, answerMap) {
  let placed = 0, selected = null;
  const place = (zone, right) => {
    const fb = quizEl.querySelector(".feedback");
    const okp = answerMap[zone.dataset.left] === right;
    zone.textContent = right;
    zone.dataset.result = okp ? "correct" : "wrong";
    fb.dataset.result = okp ? "correct" : "wrong";
    fb.textContent = okp ? "✓ 配對正確" : "✗ 配對不正確";
    fb.className = "feedback " + (okp ? "ok" : "bad") + " show";
    if (okp) {
      const chip = matchEl.querySelector(`.drag-chip[data-right="${right}"]`);
      if (chip) chip.classList.add("placed");
      placed++;
      if (placed === Object.keys(answerMap).length)
        recordProgress(document.body.dataset.course, matchEl.closest(".quiz-q").dataset.module, "match:" + matchEl.dataset.mid_id, true);
    }
  };
  matchEl.querySelectorAll(".drag-chip").forEach(chip => {
    chip.draggable = true;
    chip.addEventListener("dragstart", e => e.dataTransfer.setData("text/plain", chip.dataset.right));
    // 點擊選取回退（拖曳之外的等效輸入路徑，供鍵盤/觸控/測試驅動）
    chip.addEventListener("click", () => {
      matchEl.querySelectorAll(".drag-chip").forEach(c => c.classList.toggle("selected", c === chip));
      selected = chip;
    });
  });
  quizEl.querySelectorAll(".drop-zone").forEach(zone => {
    zone.addEventListener("dragover", e => { e.preventDefault(); zone.classList.add("over"); });
    zone.addEventListener("dragleave", () => zone.classList.remove("over"));
    zone.addEventListener("drop", e => { e.preventDefault(); zone.classList.remove("over"); place(zone, e.dataTransfer.getData("text/plain")); });
    zone.addEventListener("click", () => { if (selected) place(zone, selected.dataset.right); });
  });
}

/* ---------- M11：書籤（細線圖標→localStorage） ---------- */
function initBookmarks() {
  const saved = lsGet(LS_BOOKMARKS, []);
  document.querySelectorAll('[data-mid="M11"]').forEach(btn => {
    const mod = btn.dataset.module;
    btn.classList.toggle("saved", saved.includes(mod));
    btn.addEventListener("click", () => {
      const list = lsGet(LS_BOOKMARKS, []);
      const i = list.indexOf(mod);
      i >= 0 ? list.splice(i, 1) : list.push(mod);
      lsSet(LS_BOOKMARKS, list);
      btn.classList.toggle("saved", list.includes(mod));
      renderBookmarksOnHome();
    });
  });
}
function renderBookmarksOnHome() {
  const zone = document.getElementById("m11-bookmark-shelf");
  if (!zone) return;
  const saved = lsGet(LS_BOOKMARKS, []);
  zone.querySelectorAll("li").forEach(li => li.classList.toggle("empty", !saved.includes(li.dataset.module)));
}

/* ---------- M6：連擊（每日活躍日＋7 格圓點日曆，無懲罰無火焰） ---------- */
/* Q10 裁決：連擊日曆砍除——回訪假設不可觀測（localStorage 無後端）；initStreak 死碼移除 */

/* ---------- M12：捲動進度線（2px --accent 細線）＋章節單次淡入 ---------- */
function initScrollProgress() {
  const bar = document.getElementById("m12-scroll-progress");
  if (!bar) return;
  addEventListener("scroll", () => {
    const max = document.documentElement.scrollHeight - innerHeight;
    bar.style.width = (max > 0 ? (scrollY / max) * 100 : 0) + "%";
  }, { passive: true });
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add("revealed"); io.unobserve(e.target); } }); // 單次播放
  }, { threshold: 0.02 }); // 修正：0.18 對高於視窗的卡片永不觸發（內容渲染了但 opacity:0＝視覺全白）
  window.__observeReveals = (root) => (root || document).querySelectorAll(".reveal:not(.revealed)").forEach(el => io.observe(el)); // BUG-1 fix：渲染器注入的內容也要被觀察
  window.__observeReveals();
}

/* M5 印章牆：Q9 裁決砍除——進度只畫一處（課程層 status-badge） */

/* ---------- 內容渲染器（JSON → DOM；框架只認 data-mid，不認內容） ---------- */
async function loadCourse(courseId) {
  const res = await fetch(`/content/courses/${courseId}.json`);
  return res.json();
}

function renderModuleCard(course, mod, isFirst) {
  const card = document.createElement("section");
  card.className = "card reveal";
  card.dataset.module = mod.id;
  const totalUnits = mod.units.length + mod.questions.length + (mod.match ? 1 : 0);
  card.innerHTML = `
    <button class="m11-bookmark" id="m11-bookmark-${mod.id}" data-mid="M11" data-module="${mod.id}" title="書籤" aria-label="書籤">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M6 3h12v18l-6-4-6 4z"/></svg>
    </button>
    <div class="m1-progress" id="m1-progress-${mod.id}" data-mid="M1" data-course="${course.id}" data-module="${mod.id}" data-total="${totalUnits}">
      <div class="bar"><span></span></div><div class="pct">0%</div>
    </div>
    <h3>${mod.title}</h3>
    <div class="m3-lock-note" id="m3-lock-${mod.id}" data-mid="M3" data-module="${mod.id}">
      <svg class="lock-svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>
      先完成前一模組剩餘 <span class="m3-pending">0</span> 項
    </div>`;
  // 單元內容（含錨點）＋ M1 標記完成核取框（單元＋測驗題都計入）
  mod.units.forEach(u => card.appendChild(unitSection(course, mod, u)));
  mod.questions.forEach(q => card.appendChild(quizBlock(course, mod, q)));
  if (mod.match) card.appendChild(matchBlock(course, mod, mod.match));
  return card;
}
function mdLite(s){return s.replace(/\*\*([^*]+)\*\*/g,"<strong>$1</strong>");}
function unitSection(course, mod, u) {
  const sec = document.createElement("section");
  sec.className = "unit reveal";
  if (u.anchors && u.anchors[0]) sec.id = u.anchors[0];
  sec.innerHTML = `<h3 id="unit-${u.id}">${u.title}</h3>${(u.body || []).map(p => `<p>${mdLite(p)}</p>`).join("")}`;
  (u.media || []).forEach(m => sec.appendChild(mediaBlock(m)));
  sec.appendChild(checkRow(course, mod, u.id, "讀完此單元"));
  return sec;
}
/* ---------- M14：媒體渲染（media[] → DOM；tier 標示渲染，非存取控制——靜態站誠實標示） ---------- */
const TIER_LABEL = { regulatory: "證照層", "literature-extrapolated": "文獻層（外推）", "clinical-experience": "臨床經驗層" };
const TIER_BADGE = { free: "免費層", paid: "付費層（標示）" };
function mediaBlock(m) {
  const fig = document.createElement("figure");
  fig.className = "media-block"; fig.dataset.mid = "M14"; fig.dataset.tier = m.tier || m.audience_tier || "";
  const src = m.site_path || m.src || m.file || "";
  let inner = "";
  if (m.note === "cc-by-pending-file") {
    /* 授權佔位槽：真圖檔尚未入庫——渲染佔位框（caption+出處），不渲染 broken img */
    inner = `<div class="media-pending">素材待補（CC-BY 原文圖，入庫後替換）<br>出處：${m.source_doi || ""}</div>`;
  } else if (m.type === "before-after") {
    const parts = (m.images || [m.site_path, m.src_before, m.src_after].filter(Boolean));
    inner = `<div class="ba-pair">${parts.map(s => `<img src="${s}" loading="lazy" alt="before/after">`).join('<span class="ba-sep">→</span>')}</div>`;
  } else if (m.type === "video") {
    inner = `<video src="${src}" controls preload="metadata" playsinline></video>`;
  } else {
    inner = `<img src="${src}" loading="lazy" alt="${m.alt || "illustration"}">`;
  }
  fig.innerHTML = `${inner}<figcaption><span class="tier-badge tier-${(m.tier||"").replace(/[^a-z-]/g,"")}">${TIER_LABEL[m.tier] || m.tier || ""}</span><span class="aud-badge">${TIER_BADGE[m.audience_tier === "paid" ? "paid" : "free"]}</span>${m.consent_flag === "verbal-pending" ? '<span class="consent-badge">同意書待補</span>' : ""}</figcaption>`;
  return fig;
}
function checkRow(course, mod, unitId, title) {
  const row = document.createElement("label");
  row.className = "m1-check";
  const rec = progressRecords().find(r => r.courseId === course.id && r.moduleId === mod.id && r.unitId === unitId);
  row.innerHTML = `<span data-mid="M1" data-check-for="${unitId}"><input type="checkbox" id="m1-check-${unitId}" ${rec?.checked ? "checked" : ""}></span><span>${title}（標記完成）</span>`;
  row.querySelector("input").addEventListener("change", e =>
    recordProgress(course.id, mod.id, unitId, e.target.checked));
  return row;
}
function quizBlock(course, mod, q) {
  const el = document.createElement("div");
  el.className = "quiz-q";
  const name = `${mod.id}-${q.id}`;
  el.innerHTML = `<p><strong>${q.prompt}</strong></p>
    <div class="opts" id="m2-input-${name}" data-mid="M2" data-role="input" data-quiz="${name}" data-answer="${q.answer}" data-question='${JSON.stringify(q).replace(/'/g, "&#39;")}' data-module="${mod.id}">
      ${q.options.map((o, i) => `<label class="opt"><input type="radio" name="${name}" value="${i}"><span>${o}</span></label>`).join("")}
    </div>
    <button class="btn" id="m2-submit-${name}" data-mid="M2" data-quiz="${name}">提交</button>
    <div class="feedback" data-feedback-for="${name}"></div>
    <div class="hint-ladder" id="m8-ladder-${name}" data-mid="M8" data-for="${name}">
      ${q.hints.map((h, i) => `<button id="m8-hint-${name}-l${i + 1}" data-level="${i + 1}">提示 ${["一（概念回顧）", "二（要點改述）", "三（揭示答案）"][i]}</button><div class="hint" data-level="${i + 1}" ${i === 0 && q.hints[0].includes("#") ? `data-anchor="${q.hints[0].match(/#([\w-]+)/)[1]}"` : ""}>${h}</div>`).join("")}
    </div>`;
  el.querySelector('[data-mid="M2"]').addEventListener("click", () => gradeQuiz(el.querySelector(".opts")));
  el.querySelectorAll(".hint-ladder button").forEach(b => b.addEventListener("click", () => revealHint(el, Number(b.dataset.level))));
  return el;
}
function matchBlock(course, mod, match) {
  const el = document.createElement("div");
  el.className = "quiz-q";
  el.dataset.module = mod.id;
  const answerMap = {};
  match.pairs.forEach(p => answerMap[p.left] = p.right);
  const shuffled = [...match.pairs].sort(() => Math.random() - 0.5);
  el.innerHTML = `<p><strong>配對題（拖曳配對）</strong></p>
    ${match.pairs.map((p, i) => `<div class="match-row"><div class="match-left">${p.left}</div><div class="drop-zone" id="m9-drop-${match.id}-${i}" data-mid="M9" data-mid_id="${match.id}" data-left="${p.left}">拖到這裡</div></div>`).join("")}
    <div id="m9-tray-${match.id}" data-mid="M9" data-mid_id="${match.id}" class="chips">${shuffled.map(p => `<span class="drag-chip" draggable="true" data-right="${p.right}">${p.right}</span>`).join("")}</div>
    <div class="feedback" data-feedback-for="match-${match.id}"></div>`;
  initMatch(el, el.querySelector(`#m9-tray-${match.id}`), answerMap);
  return el;
}

/* ---------- M13：完成證書入口（達標才出現；頁內 #m13-cert-entry） ---------- */
let CURRENT_COURSE = null;
function renderCertEntryForCourse(courseId) {
  const course = CURRENT_COURSE && CURRENT_COURSE.id === courseId ? CURRENT_COURSE : null;
  const entry = document.getElementById("m13-cert-entry");
  if (!entry || !course) return;
  const allDone = course.modules.every(m => moduleDone(course.id, m.id));
  entry.style.display = allDone ? "block" : "none";
  entry.dataset.ready = allDone ? "1" : "0";
  if (allDone) {
    const nameInput = entry.querySelector("input");
    nameInput.value = lsGet(LS_NAME, "");
    nameInput.oninput = () => lsSet(LS_NAME, nameInput.value);
  }
}

/* ---------- 啟動：依頁面角色接線 ---------- */
async function bootCoursePage() {
  const params = new URLSearchParams(location.search);
  const courseId = params.get("course") || (await loadRegistry())[0]?.id;
  const course = await (await fetch(`/content/courses/${courseId}.json`)).json();
  CURRENT_COURSE = course;
  document.body.dataset.course = courseId;
  document.body.dataset.moduleOrder = course.modules.map(m => m.id).join(",");
  document.getElementById("course-title").textContent = course.title;
  const zone = document.getElementById("module-zone");
  course.modules.forEach(mod => zone.appendChild(renderModuleCard(course, mod)));
  window.__observeReveals(); // BUG-1 fix: observe injected .reveal elements (async boot — observer must run AFTER injection)
  initBookmarks(); renderProgress(); renderLocks(); renderCertEntryForCourse(courseId);
}
async function bootHomePage() {
  await renderHome();
  window.__observeReveals(); // BUG-1 fix: observe injected .reveal elements
}
document.addEventListener("DOMContentLoaded", () => {
  initScrollProgress();
  (document.body.dataset.page === "course" ? bootCoursePage : bootHomePage)();
});

/* ---------- 課程註冊表（/courses.yml＝索引；新增一門課＝/content/courses/ 加一檔＋此索引加一行，框架層零改動） ---------- */
async function loadRegistry() {
  const txt = await (await fetch("/courses.yml")).text();
  const courses = [];
  const groups = [];
  let inGroups = false;
  for (const line of txt.split("\n")) {
    if (/^groups:\s*$/.test(line)) { inGroups = true; continue; }
    if (/^courses:\s*$/.test(line)) { inGroups = false; continue; }
    if (inGroups) {
      const g = line.match(/^\s*-\s*id:\s*(\S+)\s*$/);
      const t = line.match(/^\s*title_zh:\s*(.+?)\s*$/);
      if (g) groups.push({ id: g[1], title: t ? t[1] : g[1] });
      else if (t && groups.length) groups[groups.length - 1].title = t[1];
      continue;
    }
    const m = line.match(/^\s*-\s*id:\s*(\S+)\s*$/);
    const f = line.match(/^\s*file:\s*(\S+)\s*$/);
    const g2 = line.match(/^\s*group:\s*(\S+)\s*$/);
    if (m) courses.push({ id: m[1], file: null, group: null });
    else if (f && courses.length) courses[courses.length - 1].file = f[1];
    else if (g2 && courses.length) courses[courses.length - 1].group = g2[1];
  }
  return { courses, groups };
}

/* ---------- 首頁渲染（註冊表驅動：M5 印章槽＋M10 路徑卡＋M6 連擊＋M11 收藏架） ---------- */
async function renderHome() {
  const { courses, groups } = await loadRegistry();
  const zone = document.getElementById("m10-path-cards");
  const shelf = document.getElementById("m11-bookmark-shelf");
  // ADR-0004: 按註冊表 group 分區——註冊表是單一事實源，分組標題由資料長出，不手寫 HTML
  const order = groups.length ? groups : [{ id: null, title: null }];
  for (const g of order) {
    if (zone && g.title) {
      const gh = document.createElement("h2");
      gh.className = "group-header reveal"; gh.dataset.group = g.id; gh.textContent = g.title;
      zone.appendChild(gh);
    }
    for (const entry of courses.filter(c => (g.id || null) === (c.group || null))) await renderCourseEntry(entry);
  }
  renderProgress();
  renderBookmarksOnHome();
  return;
}
async function renderCourseEntry(entry) {
  const registry = [{ id: entry.id, file: entry.file, group: entry.group }];
  const zone = document.getElementById("m10-path-cards");
  const shelf = document.getElementById("m11-bookmark-shelf");
  for (const entry of registry) {
    const course = await (await fetch(entry.file)).json();
    // ADR-0004 層級：區(h2) → 課程(h3 課程標題) → 模組卡。課程標題由課程 JSON 長出，不手寫。
    if (zone) {
      const ch = document.createElement("h3");
      ch.className = "course-header reveal"; ch.dataset.course = course.id;
      ch.innerHTML = `<a href="course.html?course=${course.id}">${course.title}</a>`;
      zone.appendChild(ch);
    }
    // Q9 決定：進度歸課程層——每課一行（课程名已在上）＋本课进度条＋状态标签（TryHackMe End-User Assignments 式）
    if (zone) {
      const row = document.createElement("div");
      row.className = "course-row"; row.dataset.mid = "M16"; row.dataset.course = course.id;
      row.innerHTML = `<span class="status-badge" data-course="${course.id}">Not Started</span><span class="course-progress">${course.modules.length} 個模組</span>`;
      zone.appendChild(row);
    }
    // （M5 全局印章牆已於 Q9 裁決移除——進度只畫一處；M6 連擊 Q10 裁決拿掉）
    // M10：每條 path/模組一張卡＋整體進度條＋下一步按鈕
    course.modules.forEach((mod, i) => {
      if (!zone) return;
      const card = document.createElement("article");
      card.className = "card path-card reveal";
      card.dataset.module = mod.id;
      card.innerHTML = `
        <div class="num">0${i + 1}</div>
        <h3><a href="course.html?course=${course.id}&module=${mod.id}">${mod.title}</a></h3>
        <div class="m1-progress" id="m1-progress-${course.id}-${mod.id}" data-mid="M1" data-course="${course.id}" data-module="${mod.id}" data-total="${mod.units.length + mod.questions.length + (mod.match ? 1 : 0)}">
          <div class="bar"><span></span></div><div class="pct">0%</div>
        </div>
        <div class="next-step" data-next="${course.id}:${mod.id}"><a class="btn ghost" id="next-btn-${course.id}-${mod.id}" href="course.html?course=${course.id}&module=${mod.id}" style="display:none"></a></div>`;
    card.onclick = (e) => { if (!e.target.closest("a")) location.href = `course.html?course=${course.id}&module=${mod.id}`; }; // Q12: 無進度時整卡可點
      zone.appendChild(card);
    });
    // M11 首頁收藏區
    if (shelf) course.modules.forEach(mod => {
      const li = document.createElement("li");
      li.dataset.module = mod.id;
      li.className = "empty";
      li.innerHTML = `<a href="course.html?course=${course.id}&module=${mod.id}">${mod.title}</a>`;
      shelf.appendChild(li);
    });
  }
  renderProgress();
  renderBookmarksOnHome();
}
