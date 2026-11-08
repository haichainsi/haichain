import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Surface\.gemini\antigravity\brain\58372994-a438-41fa-b706-7e60c217e51b\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        content = data.get('content', '')
        if 'metamask' in content.lower():
            step = data.get('step_index')
            source = data.get('source')
            print(f'=== STEP {step} ({source}) ===')
            # print excerpt
            for l in content.splitlines():
                if 'metamask' in l.lower():
                    print('  ', l.strip()[:140])
