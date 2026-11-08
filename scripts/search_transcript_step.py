import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/Surface/.gemini/antigravity/brain/e7e45538-f714-40c0-a595-0a358d20c5bb/.system_generated/logs/transcript.jsonl', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if 'chưa thấy thay đổi gì' in line:
            obj = json.loads(line)
            print("Step:", obj.get("step_index"), obj.get("type"), obj.get("content", "")[:100])
