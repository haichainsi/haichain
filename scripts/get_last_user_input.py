import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\Surface\.gemini\antigravity\brain\58372994-a438-41fa-b706-7e60c217e51b\.system_generated\logs\transcript.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data.get('type') == 'USER_INPUT':
            last_user = data

print('Last USER_INPUT step_index:', last_user.get('step_index'))
print('Content:', last_user.get('content'))
print('Media:', last_user.get('media'))
