import sys

# Clean EN
with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = None
end = None
for i, l in enumerate(lines):
    if l.startswith('```python') and i < 235:
        start = i
    if start is not None and l.startswith('```') and i > start:
        end = i
        break

print(f'EN python block: {start+1} to {end+1}')
clean_en_lines = [
    '> [!NOTE]\n',
    '> **HOW HAICHAIN SETTLES WITH OPENAI, DEEPSEEK & ANTHROPIC:**\n',
    '> Foundational model labs currently require traditional corporate fiat billing (Stripe / Corporate Cards) and do not natively receive Solana SPL tokens. Haichain resolves this via the **Decentralized Liquidity Relayer Protocol**:\n',
    '> 1. The user\'s AI Agent locks micro-USDT into the non-custodial On-Chain Vault PDA on Solana.\n',
    '> 2. Bonded Relayers (who stake collateral in USDT/SOL to eliminate front-running and default risks) maintain high-tier enterprise billing agreements with OpenAI, Anthropic, and DeepSeek.\n',
    '> 3. The Relayer streams LLM inference responses to the agent in sub-second timeframes via HTTP/SSE while netting micro-USDT from the agent\'s signed voucher tickets.\n',
    '> 4. This delivers a seamless, non-custodial fiat-to-crypto bridge: developers enjoy pure on-chain pay-as-you-go micro-escrow without managing credit cards, while foundational AI labs receive their required fiat settlement.\n',
    '\n',
    '```python\n',
    'import openai\n',
    '\n',
    '# REPLACING VULNERABLE DIRECT KEYS & EXPENSIVE STRIPE BILLING:\n',
    '# client = openai.OpenAI(api_key="sk-proj-xxxx")\n',
    '\n',
    '# INSTANT HAICHAIN ACTIVATION (EXACTLY 1 LINE REPLACEMENT):\n',
    'client = openai.OpenAI(\n',
    '    base_url="https://gateway.haichain.si/v1",  # <-- 1-Line Drop-in Gateway!\n',
    '    api_key="hai_live_99f8d..."                 # Haichain Vault Security Key\n',
    ')\n',
    '```\n'
]
lines[start:end+1] = clean_en_lines
with open('HAICHAIN_WHITEPAPER_V1.0_EN.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed EN successfully.')

# Clean VI
with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = None
end = None
for i, l in enumerate(lines):
    if l.startswith('```python') and i < 220:
        start = i
    if start is not None and l.startswith('```') and i > start:
        end = i
        break

print(f'VI python block: {start+1} to {end+1}')
clean_vi_lines = [
    '> [!NOTE]\n',
    '> **CƠ CHẾ TẤT TOÁN VỚI OPENAI, DEEPSEEK & ANTHROPIC:**\n',
    '> Các phòng nghiên cứu mô hình nền tảng hiện tại chỉ chấp nhận thanh toán thẻ tín dụng doanh nghiệp truyền thống (Stripe / Corporate Cards) và chưa trực tiếp nhận token Solana SPL. Haichain giải quyết triệt để rào cản này thông qua **Giao Thức Relayer Thanh Khoản Phân Tán**:\n',
    '> 1. Tác tử AI của người dùng khóa micro-USDT vào Kho Quỹ Vault PDA tự quản trên Solana L1.\n',
    '> 2. Các Relayer được cấp phép (phải ký quỹ bảo chứng bằng USDT/SOL để triệt tiêu rủi ro không thực hiện) duy trì thỏa thuận thanh toán doanh nghiệp trực tiếp với OpenAI, Anthropic, DeepSeek.\n',
    '> 3. Relayer truyền luồng suy luận AI (SSE stream) về cho Agent với độ trễ nano-giây, đồng thời cấn trừ micro-USDT từ vé chi tiêu đã ký của Agent.\n',
    '> 4. Mô hình này thiết lập một cây cầu thanh khoản hai chiều minh bạch: lập trình viên AI hưởng trọn cơ chế thanh toán tức thì theo nhu cầu (pay-as-you-go) mà không cần thẻ tín dụng, trong khi các lab AI vẫn nhận đủ tiền pháp định theo yêu cầu.\n',
    '\n',
    '```python\n',
    'import openai\n',
    '\n',
    '# THAY THẾ TOÀN BỘ PRIVATE KEY & CƠ CHẾ STRIPE TRUYỀN THỐNG BẤT TIỆN:\n',
    '# client = openai.OpenAI(api_key="sk-proj-xxxx")\n',
    '\n',
    '# KÍCH HOẠT HAICHAIN TỨC THÌ (ĐÚNG 1 DÒNG DUY NHẤT):\n',
    'client = openai.OpenAI(\n',
    '    base_url="https://gateway.haichain.si/v1",  # <-- Cổng kết nối tích hợp 1 dòng!\n',
    '    api_key="hai_live_99f8d..."                 # Khóa bảo mật Haichain Vault\n',
    ')\n',
    '```\n'
]
lines[start:end+1] = clean_vi_lines
with open('HAICHAIN_WHITEPAPER_V1.0_VI.md', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Fixed VI successfully.')
