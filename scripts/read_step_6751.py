import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/Surface/.gemini/antigravity/brain/e7e45538-f714-40c0-a595-0a358d20c5bb/.system_generated/logs/transcript_full.jsonl', encoding='utf-8', errors='ignore') as f:
    for line in f:
        obj = json.loads(line)
        if obj.get('step_index') == 6751:
            print(obj.get('content'))
