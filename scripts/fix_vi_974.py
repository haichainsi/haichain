import os, re

for base_dir in ['', 'app']:
    path = os.path.join(base_dir, 'HAICHAIN_WHITEPAPER_V1.0_VI.md') if base_dir else 'HAICHAIN_WHITEPAPER_V1.0_VI.md'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Replace the broken lines 974-978
    old_target = """  3. **Doanh Thu Phí Ròng Giao Thức (Net Protocol Fee Yield):** Đạt tối thiểu **$25,000 USD** (đối ứng chính xác với tỷ lệ phí $\\gamma = 0.05\\%$ trên $$

50.000.000\\text{ USD}$ khối lượng, hoặc

$50,000 USD ở mức phí $0,10\\%$) đã nạp vào Kho bạc Giao thức."""

    new_target = """  3. **Doanh Thu Phí Ròng Giao Thức (Net Protocol Fee Yield):** Đạt tối thiểu **$25.000 USD** (đối ứng chính xác với tỷ lệ phí $\\gamma = 0.05\\%$ trên $50.000.000 USD khối lượng, hoặc $50.000 USD ở mức phí $0.10\\%$) đã nạp vào Kho bạc Giao thức."""

    if old_target in text:
        text = text.replace(old_target, new_target)
        print(f"Fixed broken $$ in {path}")
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
    else:
        print(f"Target not found in {path}")
