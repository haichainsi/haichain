import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('i18n.js', 'r', encoding='utf-8') as f:
    c = f.read()

idx_vi = c.find('vi: {')
idx_next = c.find('zh: {', idx_vi)
vi_dict = c[idx_vi:idx_next]

for k in ['marketplace.badge', 'marketplace.syncRegistriesShort', 'marketplace.devDocsBtn', 'marketplace.title']:
    pos = vi_dict.find(k)
    if pos != -1:
        print(vi_dict[pos-5:pos+100])
