import subprocess

res = subprocess.run(['git', 'show', '3754d72^:dashboard.html'], stdout=subprocess.PIPE, text=True, encoding='utf-8')
content = res.stdout
idx = content.find('id="ai-hub-btn"')
print("Original ai-hub-btn:")
print(content[idx-100:idx+400])
