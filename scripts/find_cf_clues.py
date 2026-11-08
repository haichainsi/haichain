import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/Surface/.gemini/antigravity/brain/e7e45538-f714-40c0-a595-0a358d20c5bb/.system_generated/logs/transcript.jsonl', encoding='utf-8', errors='ignore') as f:
    for line in f:
        obj = json.loads(line)
        content = obj.get('content', '')
        if ('Cloudflare' in content or 'deploy' in content or 'Pages' in content) and obj.get('type') == 'PLANNER_RESPONSE':
            # print only recent steps (e.g. > 5000)
            idx = obj.get('step_index', 0)
            if idx > 5500:
                print(f"Step {idx}: {content[:160]}...")
