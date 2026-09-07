import json, subprocess, sys
p = '/Users/zakk/Desktop/Feynman/Clinical teach webside/.scratch/medical-aesthetic-teaching-site/deliverables/neofilera-draft.json'
txt = open(p, encoding='utf-8').read()
# simplified check via opencc if available
try:
    from opencc import OpenCC
    cc = OpenCC('t2s')
except ImportError:
    cc = None
if cc is None:
    print('NO_OPENCC')
    # curated simplified-only chars
    simp = set('证说时实层记认发让许对关们个来为这术医学历产经际证据标么应'
               '么当动义经济观检显设备齐条标准确试验证据关点见观规视'
               '览读误词语谁谢象贝败账货训议记变让认诉护报担快念恐'
               '忧惊情惊懂悬意应'
               '儿两严丽乱争亚从仪们体余佣侦侧价决况净准凭击刘则刚创删剂劳势匀区医县双发变叶号启员问园圆场坏块报坦城塔增壳备处复夹夺妇婴孙学宝实宠审宪宫寻导将尔尘层山岛峡帅帘帮厂厅历厉压参')
    hits = sorted({c for c in txt if c in simp})
    print('curated simplified-char hits:', hits)
else:
    cc = OpenCC('t2s')
    bad = sorted({c for c in txt if cc.convert(c) != c})
    print('opencc t2s-convertible chars (candidates for simplified):', bad)

def count(s):
    n = 0
    for ch in s:
        o = ord(ch)
        if 0x4e00 <= o <= 0x9fff: n += 1
        elif 0x3000 <= o <= 0x303f: n += 1
        elif 0xff01 <= o <= 0xff5e: n += 1
        elif ch in '「」『』—…·': n += 1
    return n

data = json.loads(txt)
total = sum(count(para) for m in data['modules'] for u in m['units'] for para in u['body'])
print('body CJK count:', total)
# count existing course for comparison
d2 = json.load(open('/Users/zakk/Desktop/Feynman/Clinical teach webside/site/content/courses/collagen-stimulator-full-face.json', encoding='utf-8'))
t2 = sum(count(para) for m in d2['modules'] for u in m['units'] for para in u['body'])
print('existing collagen course body count:', t2)
# structural sanity
for m in data['modules']:
    assert 'media' not in m or isinstance(m.get('media'), list)
    for u in m['units']:
        assert isinstance(u['media'], list)
for c in data['claims']:
    assert c['tier'] in ('regulatory','literature-extrapolated','clinical-experience'), c
    assert c['source'] in {s['id'] for s in data['sources']}, c
qs = sum(len(m['questions']) for m in data['modules'])
ms = sum(1 for m in data['modules'] if m.get('match'))
print('interactive points: questions=%d match=%d' % (qs, ms))
print('OK')
