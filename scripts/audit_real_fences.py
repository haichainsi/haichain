import sys, os

sys.stdout.reconfigure(encoding='utf-8')

for lang in ['EN', 'VI', 'ZH', 'KO', 'ES', 'FR', 'RU', 'KK', 'HI', 'HE']:
    f = f'HAICHAIN_WHITEPAPER_V1.0_{lang}.md'
    if not os.path.exists(f):
        continue
    lines = open(f, 'r', encoding='utf-8').readlines()
    
    # Real triple backticks
    real_fences = []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith('```') and len(s) >= 3:
            # make sure it is really 3 backticks
            if s[:3] == '```':
                real_fences.append((i+1, line.strip()))
                
    print(f'=== {lang}: {len(real_fences)} real triple-backtick fences ===')
    if len(real_fences) % 2 != 0:
        print(f'  --> ODD NUMBER OF FENCES! Total = {len(real_fences)}')
        for num, text in real_fences[-5:]:
            print(f'      Line {num}: {repr(text)}')
    
    # Verify pairs
    for i in range(0, len(real_fences) - 1, 2):
        start_line = real_fences[i][0]
        end_line = real_fences[i+1][0]
        # check if it spans across major chapters
        for l_num in range(start_line, end_line-1):
            line_text = lines[l_num]
            if line_text.startswith('## 1') or line_text.startswith('## 2') or line_text.startswith('## 3') or line_text.startswith('## 4') or line_text.startswith('## 5') or line_text.startswith('## 6') or line_text.startswith('## 7') or line_text.startswith('## 8') or line_text.startswith('## 9') or line_text.startswith('## 10') or line_text.startswith('## 11') or line_text.startswith('## 12'):
                print(f'  CRITICAL INVERSION: {real_fences[i]} to {real_fences[i+1]} swallows heading at line {l_num+1}: {repr(line_text.strip())}')
