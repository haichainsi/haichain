import sys, shutil
sys.stdout.reconfigure(encoding='utf-8')

with open('dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

target = '<span class="ml-auto px-1.5 py-0.5 rounded-full text-[9px] bg-neutral-200 dark:bg-neutral-800 text-neutral-800 dark:text-neutral-200 border border-neutral-300 dark:border-neutral-700 font-mono font-bold">5-MIN</span>'

if target in content:
    content = content.replace(target, '')
    print('Successfully removed 5-MIN badge from dashboard.html!')
else:
    print('Error: target 5-MIN badge not found in dashboard.html')

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Copy to app/dashboard.html
shutil.copy2('dashboard.html', 'app/dashboard.html')
print('Copied dashboard.html -> app/dashboard.html')
