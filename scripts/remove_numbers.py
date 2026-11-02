import re, time

# 1. Update HTML
def patch_html(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    c = c.replace('1. Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí', 'Thanh toán siêu nhỏ (Dưới 1 xu Mỹ) với 0% Phí')
    c = c.replace('2. Cầu dao an toàn 380ms (Chống hack & cạn ví)', 'Cầu dao an toàn 380ms (Chống hack & cạn ví)')
    c = c.replace('3. Cực kỳ đơn giản cho người dùng (Chuẩn MCP Claude)', 'Cực kỳ đơn giản cho người dùng (Chuẩn MCP Claude)')
    c = c.replace('4. Minh bạch 100% trên Blockchain (Không thể gian lận)', 'Minh bạch 100% trên Blockchain (Không thể gian lận)')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Updated HTML: {path}")

patch_html('index.html')
patch_html('app/index.html')

# 2. Update i18n
def patch_i18n(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        for i in range(1, 5):
            prefix = f'"advantages.item{i}Title": "'
            if prefix in line:
                # Remove leading number and dot: "1. ", "2. ", etc.
                idx = line.find(prefix) + len(prefix)
                val_and_rest = line[idx:]
                val_and_rest = re.sub(r'^[0-9]+\.\s*', '', val_and_rest)
                line = line[:idx] + val_and_rest
                break
        new_lines.append(line)

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Updated i18n: {path}")

patch_i18n('i18n.js')
patch_i18n('app/i18n.js')

# 3. Bump cache
ts = int(time.time() * 1000)
new_ver = f"?v=v36_no_numbering_{ts}"

def bump_cache(path):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'i18n\.js(\?v=[a-zA-Z0-9_\.]*)?', f'i18n.js{new_ver}', c)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Bumped cache: {path}")

bump_cache('index.html')
bump_cache('app/index.html')
bump_cache('dashboard.html')
bump_cache('app/dashboard.html')

print("Finished removing numbers and bumping cache!")
