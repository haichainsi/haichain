import subprocess, difflib

head_content = subprocess.check_output(['git', 'show', 'HEAD:dashboard.html'], encoding='utf-8')
with open('dashboard.html', 'r', encoding='utf-8') as f:
    work_content = f.read()

print(f"HEAD length: {len(head_content)}")
print(f"Work length: {len(work_content)}")

if head_content == work_content:
    print("Files are identical!")
else:
    print("Files are DIFFERENT! Sample diff:")
    diff = list(difflib.unified_diff(
        head_content.splitlines(keepends=True),
        work_content.splitlines(keepends=True),
        fromfile='HEAD',
        tofile='WORK',
        n=2
    ))
    for l in diff[:40]:
        print(l, end='')
