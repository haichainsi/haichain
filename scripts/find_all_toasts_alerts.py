with open('dashboard.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

toast_and_alerts = []
for idx, l in enumerate(lines, 1):
    if any(k in l for k in ['showToast(', 'alert(', 'confirm(']):
        toast_and_alerts.append((idx, l.strip()))

print(f"Total toast and alerts in dashboard.html: {len(toast_and_alerts)}")
with open('scripts/all_toasts_and_alerts.txt', 'w', encoding='utf-8') as out:
    for idx, l in toast_and_alerts:
        out.write(f"L{idx}: {l}\n")
        print(f"L{idx}: {l[:120]}")
