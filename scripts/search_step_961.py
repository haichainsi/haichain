import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

with open('C:/Users/Surface/.gemini/antigravity/brain/e7e45538-f714-40c0-a595-0a358d20c5bb/.system_generated/logs/transcript.jsonl', encoding='utf-8', errors='ignore') as f:
    for line in f:
        obj = json.loads(line)
        idx = obj.get("step_index")
        if idx and 991 <= idx <= 1010:
            print(f"Step {idx} [{obj.get('source')} - {obj.get('type')}]:")
            if obj.get("tool_calls"):
                for tc in obj["tool_calls"]:
                    print("  Tool call:", tc["name"], tc.get("args", {}).get("CommandLine", ""))
            elif obj.get("content"):
                print("  Content:", obj["content"][:200])
