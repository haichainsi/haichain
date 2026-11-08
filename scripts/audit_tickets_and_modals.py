import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'id=["\']([^"\']*ticket[^"\']*)["\']', text, re.IGNORECASE)
print('Ticket IDs in dashboard.html:', set(matches))

for tid in set(matches):
    in_script = f"'{tid}'" in text or f'"{tid}"' in text
    print(f"  {tid} -> referenced in script: {in_script}")
    if in_script:
        # find where it's used
        pos = 0
        while True:
            idx = text.find(tid, pos)
            if idx == -1: break
            # if inside <script>
            script_start = text.rfind('<script', 0, idx)
            script_end = text.find('</script>', idx)
            if script_start != -1 and script_end != -1 and script_start < idx < script_end:
                print(f"    Inside script at {idx}: {text[idx:idx+150].strip()}")
            pos = idx + len(tid)
