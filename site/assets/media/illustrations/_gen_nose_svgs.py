#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Generator for nose_F*.svg - schematic line-art figures for the nose thread lift course.
# Files: F1-F6, F8-F10, F12 (F7/F11 are CC-BY photo slots, skipped).
import os, math
import xml.etree.ElementTree as ET

OUT = os.path.dirname(os.path.abspath(__file__))

LIGHT = "#e8e8e8"   # base line-art stroke (dark-background friendly)
SOFT = "#9a9a9a"    # secondary labels
ARTERY = "#ff6b6b"  # arteries
THREAD = "#4ecdc4"  # thread path / safe plane
FONT = "'Noto Sans TC','PingFang TC','Microsoft JhengHei',sans-serif"

HEAD = '<?xml version="1.0" encoding="UTF-8"?>\n<!-- {src} -->\n'

def svg(source_comment, body, caption, w=880, h=660):
    # split caption into up to two lines at the schematic/source marker
    marker = "schematic／示意"
    if marker in caption:
        head, tail = caption.split(marker, 1)
        lines = [head.strip(), marker + tail]
    else:
        lines = [caption]
    cap = ""
    for i, line in enumerate(lines):
        cap += (f'<text x="20" y="{h-56+i*26}" font-family="{FONT}" font-size="15" '
                f'fill="{LIGHT}">{line}</text>\n  ')
    return HEAD.format(src=source_comment) + (
        f'<svg xmlns="http://www.w3.org/2000/svg" version="1.1" '
        f'viewBox="0 0 {w} {h}" role="img">\n'
        f'  <g>{body}</g>\n  {cap.rstrip()}\n</svg>\n')

def t(x, y, s, fill=LIGHT, size=17, anchor="start", weight="normal"):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}">{s}</text>')

def p(d, stroke=LIGHT, wdt=2.2, dash=None, fill="none", cap="round"):
    dstr = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{wdt}" '
            f'stroke-linecap="{cap}" stroke-linejoin="round"{dstr}/>')

def ln(x1, y1, x2, y2, stroke=LIGHT, wdt=2, dash=None):
    dstr = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{wdt}" stroke-linecap="round"{dstr}/>')

def c(cx, cy, r, stroke=LIGHT, wdt=2.2, fill="none", dash=None):
    dstr = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{wdt}"{dstr}/>')

DEFS = (f'<defs><marker id="arw" viewBox="0 0 10 10" refX="9" refY="5" '
        f'orient="auto" markerWidth="9" markerHeight="9">'
        f'<path d="M0,1 L10,5 L0,9 z" fill="{LIGHT}"/></marker>'
        f'<marker id="arwT" viewBox="0 0 10 10" refX="9" refY="5" '
        f'orient="auto" markerWidth="9" markerHeight="9">'
        f'<path d="M0,1 L10,5 L0,9 z" fill="{THREAD}"/></marker></defs>')

def arrow(x1, y1, x2, y2, stroke=LIGHT):
    m = "arwT" if stroke == THREAD else "arw"
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="2.4" marker-end="url(#{m})"/>')

def thread_path(d, color=THREAD):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="3.4" stroke-linecap="round"/>'

def barbs_along(p0, p1, n=8, color=THREAD, flip=False):
    """Barb ticks perpendicular-ish along a straight thread segment p0->p1."""
    out = ""
    for i in range(1, n):
        tt = i / n
        x = p0[0] + (p1[0]-p0[0])*tt
        y = p0[1] + (p1[1]-p0[1])*tt
        ang = math.atan2(p1[1]-p0[1], p1[0]-p0[0]) + math.pi/2
        if flip: ang += math.pi
        bx, by = x + 13*math.cos(ang), y + 13*math.sin(ang)
        out += (f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{bx:.0f}" y2="{by:.0f}" '
                f'stroke="{color}" stroke-width="2.2" stroke-linecap="round"/>')
    return out

# ================================================================ F1
# F1: dorsal nasal artery within 1-2 mm of the midline; thread-safe preperiosteal plane.
f1 = []
f1.append(DEFS)
# face profile (side view, facing left)
f1.append(p("M 540,70 C 470,80 400,120 360,180"))                                   # forehead -> brow
f1.append(p("M 360,180 C 336,190 308,196 292,210"))                                  # rhinion dip
f1.append(p("M 292,210 C 268,242 224,292 190,332 C 178,348 182,358 196,360"))        # dorsum -> tip
f1.append(p("M 196,360 C 222,364 244,370 254,384"))                                  # columella
f1.append(p("M 254,384 C 238,394 218,402 210,416 C 224,426 242,430 254,440 C 248,454 244,468 250,484"))  # lips/chin
f1.append(p("M 540,70 C 620,120 672,220 678,340 C 682,420 656,478 622,510", wdt=1.6))  # back of head
# midline along the nasal bones (dashed)
f1.append(p("M 302,202 C 282,234 236,288 202,328", wdt=1.8, dash="7 6"))
f1.append(t(318, 182, "正中線（midline）"))
# 1-2 mm danger band hugging the midline
f1.append(f'<path d="M 296,206 C 276,238 230,290 198,328" fill="none" stroke="{ARTERY}" stroke-width="16" opacity="0.14" stroke-linecap="butt"/>')
f1.append(p("M 296,206 C 278,236 234,288 200,326", stroke=ARTERY, wdt=3.2))
f1.append(arrow(150, 296, 240, 246, ARTERY))
f1.append(t(40, 322, "危險帶：正中線旁 1–2 mm", ARTERY))
f1.append(t(60, 160, "dorsal nasal artery（DNA）", ARTERY))
f1.append(arrow(284, 164, 272, 214, ARTERY))
# layer boundaries
f1.append(p("M 340,170 C 318,204 268,262 228,310 C 212,328 206,340 204,350", wdt=1.4, dash="2 5"))
f1.append(t(360, 296, "皮下脂肪層／SMAS——DNA 行走層（A2）", SOFT, 15))
f1.append(p("M 316,186 C 296,218 250,272 214,320", wdt=1.4, dash="2 5"))
f1.append(p("M 358,158 C 336,192 286,252 246,300 C 232,318 226,332 224,342", stroke=THREAD, wdt=2.6, dash="10 6"))
f1.append(arrow(470, 120, 362, 154, THREAD))
f1.append(t(476, 122, "安全插層：骨膜前層（preperiosteal）", THREAD))
f1_cap = "F1｜鼻背危險區總覽：單條優勢型 DNA 可靠正中線 1–2 mm 內行走；插層須確認骨膜前層才算安全。schematic／示意｜來源：DOI 10.1007/s00266-016-0756-0（A1）"

# ================================================================ F2
# F2: DNA morphology proportions 53/38/8 - three schematic top-view variants.
def topview_nose(x0, y0, s=1.0):
    return (p(f"M {x0},{y0} L {x0-62*s},{y0+150*s} Q {x0-72*s},{y0+174*s} {x0-40*s},{y0+178*s}"
              f" Q {x0-16*s},{y0+162*s} {x0},{y0+150*s}"
              f" Q {x0+16*s},{y0+162*s} {x0+40*s},{y0+178*s}"
              f" Q {x0+72*s},{y0+174*s} {x0+62*s},{y0+150*s} Z")
            + p(f"M {x0},{y0} L {x0},{y0+150*s}", wdt=1.4, dash="6 6"))

f2 = [DEFS]
f2.append(topview_nose(160, 90))
f2.append(p("M 128,112 C 118,158 112,190 108,216", stroke=ARTERY, wdt=3))
f2.append(p("M 192,112 C 202,158 208,190 212,216", stroke=ARTERY, wdt=3))
f2.append(t(160, 62, "雙側型 53%", LIGHT, 19, "middle"))
f2.append(t(160, 316, "兩條側支，正中無主幹", SOFT, 15, "middle"))
f2.append(topview_nose(440, 90))
f2.append(p("M 408,112 C 400,150 424,160 414,200", stroke=ARTERY, wdt=2.6))
f2.append(p("M 472,112 C 480,150 452,162 464,202", stroke=ARTERY, wdt=2.6))
f2.append(p("M 414,200 C 432,178 450,192 464,202", stroke=ARTERY, wdt=2.4))
f2.append(p("M 420,142 C 440,152 458,138 470,144", stroke=ARTERY, wdt=2))
f2.append(p("M 418,172 C 436,162 452,174 466,170", stroke=ARTERY, wdt=2))
f2.append(t(440, 62, "叢狀型 38%", LIGHT, 19, "middle"))
f2.append(t(440, 316, "正中區血管叢狀交錯", SOFT, 15, "middle"))
f2.append(topview_nose(720, 90))
f2.append(p("M 720,110 C 720,150 718,182 718,216", stroke=ARTERY, wdt=3.6))
f2.append(c(719, 162, 30, stroke=ARTERY, wdt=2, dash="6 5"))
f2.append(t(720, 62, "單條正中型 8%", ARTERY, 19, "middle"))
f2.append(arrow(720, 336, 720, 200, ARTERY))
f2.append(t(720, 366, "⚠ 正中按壓減壓法在此族群失效", ARTERY, 17, "middle"))
f2_cap = "F2｜DNA 形態比例：雙側 53%／叢狀 38%／單條正中 8%——臨床上常用的正中按壓減壓法在單條優勢型會失效。schematic／示意｜來源：PMC8594662（A2）"

# ================================================================ F3
# F3: midline arterial crossing-rate heatmap concept (<12%), rhinion single entry point.
f3 = [DEFS]
f3.append(p("M 440,72 L 302,412 Q 282,452 340,462 Q 410,448 440,414"
            " Q 470,448 540,462 Q 598,452 578,412 L 440,72 Z"))
f3.append(ln(440, 72, 440, 414, dash="7 6"))
f3.append(t(300, 84, "鼻骨正中線", SOFT, 15, "end"))
f3.append(arrow(312, 90, 424, 96))
cells = [(88, 0.05), (128, 0.07), (168, 0.09), (208, 0.12),
         (248, 0.10), (288, 0.08), (328, 0.06), (368, 0.05)]
for (y, op) in cells:
    f3.append(f'<rect x="428" y="{y}" width="24" height="36" fill="{ARTERY}" opacity="{op}" stroke="{SOFT}" stroke-width="0.8"/>')
f3.append(arrow(660, 210, 464, 122, LIGHT))
f3.append(t(560, 234, "跨越率 &lt;12%（postmortem CT 實測）"))
f3.append(c(440, 96, 16, stroke=THREAD, wdt=2.6))
f3.append(c(440, 96, 4.5, stroke=THREAD, wdt=1.5, fill=THREAD))
f3.append(arrow(260, 150, 424, 104, THREAD))
f3.append(t(254, 154, "rhinion 深層單點鈍針進針", THREAD, 17, "end"))
f3.append(t(210, 356, "熱區刻度：顏色越深＝跨越率越高；全線上限 &lt;12%", SOFT, 15))
for i, op in enumerate([0.04, 0.06, 0.08, 0.10, 0.12]):
    f3.append(f'<rect x="{210+i*30}" y="{372}" width="28" height="12" fill="{ARTERY}" opacity="{op}" stroke="none"/>')
f3.append(t(210, 412, "0", SOFT, 14))
f3.append(t(210+5*30-2, 412, "&lt;12%", SOFT, 14, "end"))
f3.append(t(210, 448, "策略：rhinion 深層單點鈍針＋其餘 sub-SMAS 逐點進針", THREAD))
f3_cap = "F3｜鼻骨正中線動脈跨越率熱區圖（&lt;12%）：rhinion 深層單點鈍針、其餘 sub-SMAS 逐點進針有數據支持。schematic／示意｜來源：DOI 10.1093/asj/sjab432（A3）"

# ================================================================ F4
# F4: figure-of-eight arterial ring around tip/ala (lateral nasal + subalar).
f4 = [DEFS]
f4.append(p("M 440,60 C 400,140 360,220 330,290 C 310,330 322,362 362,372"
            " C 400,380 424,376 440,368 C 456,376 480,380 518,372"
            " C 558,362 570,330 550,290 C 520,220 480,140 440,60 Z"))
f4.append(p("M 362,330 C 372,344 392,352 412,346", wdt=1.8))
f4.append(p("M 518,330 C 508,344 488,352 468,346", wdt=1.8))
f4.append(p("M 440,300 C 380,270 320,300 318,332 C 316,366 368,388 414,362"
            " C 432,352 440,336 440,318", stroke=ARTERY, wdt=3.2))
f4.append(p("M 440,318 C 440,336 448,352 466,362 C 512,388 564,366 562,332"
            " C 560,300 500,270 440,300", stroke=ARTERY, wdt=3.2))
f4.append(arrow(220, 236, 334, 300))
f4.append(t(60, 232, "lateral nasal artery"))
f4.append(arrow(660, 236, 548, 300))
f4.append(t(560, 232, "subalar artery"))
f4.append(p("M 440,60 C 436,140 436,220 438,286", stroke=THREAD, wdt=3, dash="9 6"))
f4.append(c(439, 302, 10, stroke=THREAD, wdt=2.4))
f4.append(arrow(560, 470, 456, 328, THREAD))
f4.append(t(574, 476, "tip／retension 線路徑——預設跨環", THREAD))
f4_cap = "F4｜下鼻 8 字形雙動脈環：lateral nasal＋subalar 繞鼻尖／鼻翼——鼻尖任何路徑（含 retension 線）預設會跨過這個環。schematic／示意｜來源：DOI 10.1097/PRS.0000000000009649（A4）"

# ================================================================ F5
# F5: superior labial artery deep septal branch ascending into columella (90%).
f5 = [DEFS]
f5.append(p("M 330,60 C 290,120 250,200 220,270 C 208,296 212,312 228,318"      # dorsum -> tip
            " C 254,322 276,330 286,346"                                          # columella
            " C 270,356 248,364 242,378 C 258,390 282,394 298,404"                # upper lip
            " C 288,420 282,436 288,452"))
f5.append(p("M 330,60 C 390,110 440,200 460,300 C 470,360 462,420 440,470", wdt=1.6))
f5.append(p("M 140,436 C 210,420 290,412 360,406 C 430,400 500,398 570,402", stroke=ARTERY, wdt=3.4))
f5.append(t(140, 470, "superior labial artery（上唇動脈）", ARTERY))
f5.append(p("M 330,408 C 316,382 300,354 290,334 C 284,322 280,314 278,304", stroke=ARTERY, wdt=3.2))
f5.append(arrow(380, 380, 306, 344, ARTERY))
f5.append(t(390, 384, "深隔支：90% 上行進入 columella", ARTERY))
f5.append(p("M 150,300 C 196,306 240,310 268,306", stroke=THREAD, wdt=3, dash="9 6"))
f5.append(c(272, 306, 10, stroke=THREAD, wdt=2.4))
f5.append(arrow(150, 262, 252, 298, THREAD))
f5.append(t(60, 254, "columella 線路徑＝動脈深度——不是「安全空隙」", THREAD))
f5_cap = "F5｜superior labial artery 的深隔支 90% 上行進入 columella：走 columella 的 retension 線路徑，這個深度就是動脈深度。schematic／示意｜來源：DOI 10.1007/s00276-025-03659-z（A5）"

# ================================================================ F6 (CORE)
# F6: two-layer overlay - thread layer (superficial fat/SMAS) vs vessel layer (DNA on SMAS surface fat).
f6 = [DEFS]
# section stack (side view slice through the nose dorsum)
f6.append(p("M 60,150 C 240,132 480,138 820,150"))                                   # skin surface
f6.append(p("M 60,214 C 240,196 480,202 820,214", wdt=1.6, dash="2 5"))              # fat/SMAS upper boundary
f6.append(p("M 60,300 C 240,282 480,288 820,300", wdt=1.6, dash="2 5"))              # SMAS deep boundary
f6.append(p("M 60,368 C 240,350 480,356 820,368", wdt=1.8))                           # periosteum
f6.append(p("M 60,430 C 240,412 480,418 820,430"))                                   # bone
f6.append(f'<rect x="60" y="430" width="760" height="66" fill="{SOFT}" opacity="0.10"/>')
f6.append(f'<rect x="150" y="200" width="440" height="102" fill="{ARTERY}" opacity="0.10"/>')  # overlap zone
f6.append(t(64, 132, "皮膚（skin）", SOFT, 15))
f6.append(t(182, 188, "superficial fat／SMAS ＝ 線層＝血管層 → 重疊紅區", ARTERY, 16))
f6.append(t(64, 336, "深脂肪層", SOFT, 15))
f6.append(t(64, 360, "骨膜前層（preperiosteal）", SOFT, 15))
f6.append(t(64, 470, "骨", SOFT, 15))
# thread running inside the SMAS layer (barbed)
f6.append(thread_path("M 120,258 C 300,244 520,246 780,256"))
for x in range(160, 760, 60):
    y = 258 - 13*math.sin(math.pi*(x-120)/660)
    f6.append(f'<line x1="{x}" y1="{y:.0f}" x2="{x-12}" y2="{y-13:.0f}" stroke="{THREAD}" stroke-width="2.2" stroke-linecap="round"/>')
f6.append(arrow(120, 116, 180, 244, THREAD))
f6.append(t(60, 108, "線的目標層（面部層位數據，A6）", THREAD))
# artery cross-sections sitting in the same layer
for (cx, cy, r) in [(310, 248, 11), (470, 242, 9), (630, 248, 12)]:
    f6.append(c(cx, cy, r, stroke=ARTERY, wdt=3, fill=ARTERY))
f6.append(arrow(470, 120, 470, 228, ARTERY))
f6.append(t(478, 114, "DNA 行於 SMAS 表面脂肪層（A2）", ARTERY))
# safe deep path
f6.append(thread_path("M 120,396 C 300,384 520,386 780,394", color=THREAD))
f6.append(f'<path d="M 120,396 C 300,384 520,386 780,394" fill="none" stroke="{THREAD}" stroke-width="2.6" stroke-dasharray="10 6"/>')
f6.append(arrow(300, 470, 300, 402, THREAD))
f6.append(t(308, 486, "深層安全路徑：壓到骨膜前層才乾淨", THREAD))
f6.append(t(430, 336, "「面部通則的安全層」＝血管層＝重疊區", ARTERY, 15))
f6_cap = "F6｜核心圖・兩層位疊圖：線抓的層（superficial fat／SMAS）與血管走的層在鼻背重疊（紅區）——抓得深、卻不能抓到血管層。schematic／示意｜來源：A6（DOI 10.3389/fmed.2026.1581406）＋A2（PMC8594662）"

# ================================================================ F8
# F8: blind-insertion overlay skeleton - facial region skin/fat thickness data map (A7 skeleton).
f8 = [DEFS]
# face top view
f8.append(p("M 440,60 C 300,70 210,190 200,330 C 192,450 300,520 440,524"
            " C 580,520 688,450 680,330 C 670,190 580,70 440,60 Z"))
ln(440, 60, 440, 300, dash="7 6")
f8.append(ln(440, 60, 440, 306, dash="7 6"))
# nose top view
f8.append(p("M 440,104 L 404,296 Q 392,326 424,332 Q 440,322 440,306 Q 440,322 456,332 Q 488,326 476,296 Z"))
# region bars = qualitative relative thickness from the A7 topography data (no invented numbers)
regions = [(330, 220, 0.55, "頰外側"), (550, 220, 0.55, "頰外側"),
           (296, 350, 0.75, "頰"), (584, 350, 0.75, "頰"),
           (424, 200, 0.30, "鼻背"), (426, 260, 0.35, "鼻背"),
           (432, 316, 0.22, "鼻尖")]
for (x, y, th, lab) in regions:
    h = int(34*th)
    f8.append(f'<rect x="{x-4}" y="{y-h}" width="8" height="{h}" fill="{THREAD}" opacity="0.85"/>')
    f8.append(t(x, y+24, lab, SOFT, 14, "middle"))
f8.append(arrow(180, 470, 288, 366, THREAD))
f8.append(t(90, 496, "條長＝相對 skin／脂肪厚度——盲插進針深度依區域厚度數據（數值見 A7）", THREAD, 15))
f8.append(t(600, 462, "目標層：superficial fat／SMAS", THREAD, 15, "end"))
f8_cap = "F8｜盲插投影片骨架：面部各區 skin／脂肪厚度數據圖（目標層 superficial fat／SMAS；柱長為數據相對示意）。schematic／示意｜來源：DOI 10.1002/ca.23726（A7）"

# ================================================================ F9
# F9: insertion angle x grab layer -> mechanics outcome (cog ~190.7 g vs mono ~22.4 g).
f9 = [DEFS]
f9.append(p("M 60,230 L 560,230", wdt=1.6, dash="2 5"))
f9.append(p("M 60,370 L 560,370", wdt=1.6, dash="2 5"))
f9.append(t(64, 218, "skin", SOFT, 15))
f9.append(t(64, 256, "抓取層（superficial fat／SMAS）", SOFT, 15))
f9.append(t(64, 400, "深層", SOFT, 15))
# shallow-angle barbed thread grabbing the layer
f9.append(thread_path("M 110,352 L 420,262"))
f9.append(barbs_along((110,352), (420,262), n=8, flip=True))
# steep-angle barbed thread
f9.append(thread_path("M 110,470 L 420,250"))
f9.append(barbs_along((110,470), (420,250), n=9, flip=True))
f9.append(arrow(430, 262, 512, 262))
f9.append(arrow(430, 250, 512, 212))
f9.append(t(120, 508, "插入角：淺角 vs 深角——抓層力學結果不同（split-face cadaveric）"))
f9.append(t(524, 216, "深抓層：抓持上限高（cog ≈190.7 g）"))
f9.append(t(524, 268, "抓持低（mono ≈22.4 g）"))
f9.append(t(524, 316, "「抓得深、卻不能抓到血管層」", THREAD, 15))
f9.append(t(524, 340, "＝此圖的量化理由", THREAD, 15))
f9_cap = "F9｜插入角 × 抓層 → 力學結果對照：倒鉤線效果取決於抓哪一層＋插入角（cog 抓持約 190.7 g vs mono 約 22.4 g）。schematic／示意｜來源：DOI 10.1055/s-0040-1712469（A8）＋T2（DOI 10.1097/DSS.0000000000002146）"

# ================================================================ F10
# F10: blunt cannula vs sharp needle at a vessel - push aside vs penetrate.
f10 = [DEFS]
f10.append(ln(460, 100, 460, 430, dash="6 8"))
# left panel: blunt cannula deflects the vessel
f10.append(t(230, 110, "鈍針／cannula：推開", THREAD, 19, "middle"))
f10.append(p("M 100,340 L 286,272", stroke=LIGHT, wdt=6, cap="butt"))
f10.append(c(296, 268, 10, stroke=LIGHT, wdt=3))
f10.append(p("M 90,230 C 190,214 250,196 292,190 C 330,186 360,196 430,214", stroke=ARTERY, wdt=4))
f10.append(arrow(316, 240, 302, 210, ARTERY))
f10.append(t(230, 170, "血管壁被推開——不破", ARTERY, 15, "middle"))
# right panel: sharp needle pierces the vessel
f10.append(t(660, 110, "尖針 sharp needle：穿入", ARTERY, 19, "middle"))
f10.append(p("M 520,340 L 700,236", stroke=LIGHT, wdt=6, cap="butt"))
f10.append(p("M 700,236 L 726,222", stroke=LIGHT, wdt=2.4))
f10.append(p("M 490,214 C 570,206 660,222 730,244 C 770,256 800,262 830,264", stroke=ARTERY, wdt=4))
f10.append(c(712, 230, 12, stroke=ARTERY, wdt=2.2, dash="4 4"))
f10.append(arrow(760, 300, 726, 244, ARTERY))
f10.append(t(700, 330, "血管壁被穿刺／切入", ARTERY, 15, "middle"))
f10.append(t(60, 450, "引用界線：thread 用鈍針／cannula，機轉不同（推開而非切開血管）——", SOFT, 15))
f10.append(t(60, 476, "不能把 filler 的失明風險數字直接搬給 thread 用，只能借解剖地圖（A12 裁決）。", SOFT, 15))
f10_cap = "F10｜鈍針 vs 尖針通過血管的機轉對照：推開 vs 穿入。schematic／示意｜來源：DOI 10.1111/jocd.13743（A9，secondary）"

# ================================================================ F12
# F12: assembly map - facial layer data (A6/A7) x nasal artery map (A1-A5), whole-nose danger zones.
f12 = [DEFS]
# front view nose
f12.append(p("M 440,60 C 420,120 404,180 392,240 C 376,300 350,340 336,368"
             " C 322,394 336,414 372,420 C 402,424 426,418 440,410"
             " C 454,418 478,424 508,420 C 544,414 558,394 544,368"
             " C 530,340 504,300 488,240 C 476,180 460,120 440,60 Z"))
f12.append(ln(440, 60, 440, 300, dash="7 6"))
f12.append(p("M 366,378 C 378,392 396,398 414,392", wdt=1.8))
f12.append(p("M 514,378 C 502,392 484,398 466,392", wdt=1.8))
# D1 dorsum band
f12.append(f'<rect x="428" y="88" width="24" height="184" fill="{ARTERY}" opacity="0.16" stroke="none"/>')
f12.append(p("M 438,94 C 436,150 436,212 438,268", stroke=ARTERY, wdt=3))
f12.append(arrow(620, 130, 462, 138))
f12.append(t(628, 134, "D1｜正中線 1–2 mm 帶（DNA）", LIGHT, 15))
# D2 figure-of-eight
f12.append(p("M 440,330 C 396,310 352,334 350,360 C 348,388 388,406 424,386"
             " C 434,380 440,368 440,354", stroke=ARTERY, wdt=3))
f12.append(p("M 440,354 C 440,368 446,380 456,386 C 492,406 532,388 530,360"
             " C 528,334 484,310 440,330", stroke=ARTERY, wdt=3))
f12.append(arrow(628, 300, 526, 342))
f12.append(t(634, 302, "D2｜8 字雙動脈環", LIGHT, 15))
# D3 columella
f12.append(p("M 470,488 C 456,462 442,440 436,420", stroke=ARTERY, wdt=2.8))
f12.append(arrow(600, 500, 478, 482, ARTERY))
f12.append(t(608, 504, "D3｜深隔支上行入 columella（90%）", ARTERY, 15))
# thread paths (the assembly overlay)
f12.append(thread_path("M 448,76 C 446,140 444,204 444,262", color=THREAD))
f12.append(p("M 300,500 C 356,482 408,458 432,424", stroke=THREAD, wdt=2.8, dash="9 6"))
f12.append(arrow(230, 512, 312, 498, THREAD))
f12.append(t(60, 528, "thread 線路徑（dorsal shuttle＋columella 進線）", THREAD, 15))
f12.append(t(60, 562, "拼圖免責：面部層位數據（A6/A7）× 鼻動脈地圖（A1–A5）——", SOFT, 15))
f12.append(t(60, 586, "兩張圖的坐標系沒有被任何單篇研究同時驗證過。", SOFT, 15))
f12_cap = "F12｜拼裝總圖：面部層位 × 鼻動脈——全鼻三大危險區＋插線層總覽（彙編圖，非單一來源）。schematic／示意｜來源：A1–A7 彙編（無單一 DOI）"

FILES = {
    "nose_F1.svg":  ("Source: DOI 10.1007/s00266-016-0756-0 (A1, Tansatit et al., Aesthet Plast Surg 2017 - latex-perfused cadaveric dissection, 50 cadavers)", f1, f1_cap),
    "nose_F2.svg":  ("Source: PMC8594662 (A2, Anatomical Study of the Dorsal Nasal Artery, PRS Global Open 2021 - layer anatomy, 60 cadavers)", f2, f2_cap),
    "nose_F3.svg":  ("Source: DOI 10.1093/asj/sjab432 (A3, Cong LY et al., 3D Arterial Distribution Over Midline of Nasal Bone, ASJ 2022 - postmortem CT)", f3, f3_cap),
    "nose_F4.svg":  ("Source: DOI 10.1097/PRS.0000000000009649 (A4, Tansatit et al., Lower Nose Arterial Plexus and Safe Filler Injections, PRS 2022 - modified Sihler perfusion, 40 cadavers)", f4, f4_cap),
    "nose_F5.svg":  ("Source: DOI 10.1007/s00276-025-03659-z (A5, Park HJ & Hur MS, Septal branches of superior labial artery, Surg Radiol Anat 2025 - Yonsei, 40 cadavers)", f5, f5_cap),
    "nose_F6.svg":  ("Sources: A6 DOI 10.3389/fmed.2026.1581406 (Yonsei micro-CT/US layer ground truth) + A2 PMC8594662 (DNA on SMAS surface fat) - module CORE figure", f6, f6_cap),
    "nose_F8.svg":  ("Source: DOI 10.1002/ca.23726 (A7, Lee KW et al., 3D topography of facial soft tissues for threading, Clin Anat 2021)", f8, f8_cap),
    "nose_F9.svg":  ("Sources: A8 DOI 10.1055/s-0040-1712469 (Braun M et al., Influence of Insertion Angle on Tissue-Mechanics, Facial Plast Surg 2020, split-face cadaveric) + T2 DOI 10.1097/DSS.0000000000002146 (cog ~190.7 g vs mono ~22.4 g)", f9, f9_cap),
    "nose_F10.svg": ("Source: DOI 10.1111/jocd.13743 (A9, Cannula versus needle in medical rhinoplasty, J Cosmet Dermatol 2020, secondary)", f10, f10_cap),
    "nose_F12.svg": ("Compiled figure (not a single source): A1 DOI 10.1007/s00266-016-0756-0; A2 PMC8594662; A3 DOI 10.1093/asj/sjab432; A4 DOI 10.1097/PRS.0000000000009649; A5 DOI 10.1007/s00276-025-03659-z; A6 DOI 10.3389/fmed.2026.1581406; A7 DOI 10.1002/ca.23726", f12, f12_cap),
}

import xml.etree.ElementTree as ET2
for fname, (src, body, cap) in sorted(FILES.items()):
    doc = svg(src, "".join(body), cap)
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)
    ET2.parse(path)
    print("OK", fname)
print("ALL PARSED", len(FILES), "files")
