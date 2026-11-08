import subprocess, os

test_html = '<p>* <strong>Bất biến $I_8$ (Thanh toán Đơn điệu &amp; Duy nhất):</strong> $\\text{paid}_{\\text{new}} \\le \\min(\\text{voucher.cumulative}, \\text{channel.reserved}) \\;\\land\\; \\text{paid}_{\\text{new}} \\ge \\text{paid}_{\\text{old}}$. Chống lặp và chống double-spending voucher.</p>'

with open('test_in.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

subprocess.run(['node', 'scripts/render_math_cli.js', 'test_in.html', 'test_out.html'], check=True)

with open('test_out.html', 'r', encoding='utf-8') as f:
    res = f.read()

print('Contains katex:', 'katex' in res)
print('Contains raw textpaid:', 'text{paid}' in res)
