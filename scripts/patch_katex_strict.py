with open('scripts/render_math_cli.js', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('{ displayMode: true, throwOnError: false }', '{ displayMode: true, throwOnError: false, strict: "ignore" }')
text = text.replace('{ displayMode: false, throwOnError: false }', '{ displayMode: false, throwOnError: false, strict: "ignore" }')

with open('scripts/render_math_cli.js', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated render_math_cli.js successfully!')
