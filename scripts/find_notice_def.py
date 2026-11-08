import sys
sys.stdout.reconfigure(encoding='utf-8')
dash = open('dashboard.html', encoding='utf-8').read()
idx = 0
while True:
    idx = dash.find('fiatSandboxNotice', idx)
    if idx == -1:
        break
    print(dash[max(0, idx-100):min(len(dash), idx+200)])
    print("="*40)
    idx += len('fiatSandboxNotice')
