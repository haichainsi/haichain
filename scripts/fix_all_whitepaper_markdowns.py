import os, sys, re, glob, shutil

WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
APP_DIR = os.path.join(WORKSPACE_DIR, "app")

def fix_en():
    path = os.path.join(WORKSPACE_DIR, "HAICHAIN_WHITEPAPER_V1.0_EN.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Fix the duplicate blockquote inside ```python
    py_pattern = r'```python\s*import openai.*?> \[!NOTE\].*?client = openai\.OpenAI\(\s*base_url="https://gateway\.haichain\.si/v1",.*?api_key="hai_live_99f8d\.\.\."\s*\)\s*```'
    
    clean_py = '''> [!NOTE]
> **HOW HAICHAIN SETTLES WITH OPENAI, DEEPSEEK & ANTHROPIC:**
> Foundational model labs currently require traditional corporate fiat billing (Stripe / Corporate Cards) and do not natively receive Solana SPL tokens. Haichain resolves this via the **Decentralized Liquidity Relayer Protocol**:
> 1. The user's AI Agent locks micro-USDT into the non-custodial On-Chain Vault PDA on Solana.
> 2. Bonded Relayers (who stake collateral in USDT/SOL to eliminate front-running and default risks) maintain high-tier enterprise billing agreements with OpenAI, Anthropic, and DeepSeek.
> 3. The Relayer streams LLM inference responses to the agent in sub-second timeframes via HTTP/SSE while netting micro-USDT from the agent's signed voucher tickets.
> 4. This delivers a seamless, non-custodial fiat-to-crypto bridge: developers enjoy pure on-chain pay-as-you-go micro-escrow without managing credit cards, while foundational AI labs receive their required fiat settlement.

```python
import openai

# REPLACING VULNERABLE DIRECT KEYS & EXPENSIVE STRIPE BILLING:
# client = openai.OpenAI(api_key="sk-proj-xxxx")

# INSTANT HAICHAIN ACTIVATION (EXACTLY 1 LINE REPLACEMENT):
client = openai.OpenAI(
    base_url="https://gateway.haichain.si/v1",  # <-- 1-Line Drop-in Gateway!
    api_key="hai_live_99f8d..."                 # Haichain Vault Security Key
)
```'''
    text = re.sub(py_pattern, clean_py, text, flags=re.DOTALL)

    # 2. Fix line 181 in EN comparison matrix (make it 102 chars wide)
    # Line 181 was: |  Minimum Practical Fee  $0.30 fixed fee floor     $0.02 - $0.50 gas spike    $0.000001 (1,000:1 Compressed Netting / $0.001 Base)   |
    old_row1 = r'\|\s*Minimum Practical Fee\s*\$0\.30 fixed fee floor\s*\$0\.02 - \$0\.50 gas spike\s*\$0\.000001 \(1,000:1 Compressed Netting / \$0\.001 Base\)\s*\|'
    new_row1 = '|  Minimum Practical Fee  $0.30 fixed fee floor     $0.02 - $0.50 gas spike    $0.000001 (Netting)   |'
    text = re.sub(old_row1, new_row1, text)

    # 3. Fix line 285 in EN (format within 117 chars)
    old_row2 = r'\|\s*Legacy Web2 Rails\s*\$0\.30 \+ 2\.9% fixed fee floor \(150,000% fee\s*Pure micro-utility \(\$0\.000001 via 1,000:1 batch compression / \$0\.001 base\);\|'
    new_row2 = '| Legacy Web2 Rails     $0.30 + 2.9% fixed fee floor (150,000% fee      Pure micro-utility ($0.000001 netted / $0.001 base);|'
    text = re.sub(old_row2, new_row2, text)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Fixed EN markdown.")

def fix_vi():
    path = os.path.join(WORKSPACE_DIR, "HAICHAIN_WHITEPAPER_V1.0_VI.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Fix duplicate blockquote inside ```python
    py_pattern = r'```python\s*import openai.*?> \[!NOTE\].*?client = openai\.OpenAI\(\s*base_url="https://gateway\.haichain\.si/v1",.*?api_key="hai_live_99f8d\.\.\."\s*\)\s*```'
    clean_py = '''> [!NOTE]
> **CƠ CHẾ TẤT TOÁN VỚI OPENAI, DEEPSEEK & ANTHROPIC:**
> Các phòng nghiên cứu mô hình nền tảng hiện tại chỉ chấp nhận thanh toán thẻ tín dụng doanh nghiệp truyền thống (Stripe / Corporate Cards) và chưa trực tiếp nhận token Solana SPL. Haichain giải quyết triệt để rào cản này thông qua **Giao Thức Relayer Thanh Khoản Phân Tán**:
> 1. Tác tử AI của người dùng khóa micro-USDT vào Kho Quỹ Vault PDA tự quản trên Solana L1.
> 2. Các Relayer được cấp phép (phải ký quỹ bảo chứng bằng USDT/SOL để triệt tiêu rủi ro không thực hiện) duy trì thỏa thuận thanh toán doanh nghiệp trực tiếp với OpenAI, Anthropic, DeepSeek.
> 3. Relayer truyền luồng suy luận AI (SSE stream) về cho Agent với độ trễ nano-giây, đồng thời cấn trừ micro-USDT từ vé chi tiêu đã ký của Agent.
> 4. Mô hình này thiết lập một cây cầu thanh khoản hai chiều minh bạch: lập trình viên AI hưởng trọn cơ chế thanh toán tức thì theo nhu cầu (pay-as-you-go) mà không cần thẻ tín dụng, trong khi các lab AI vẫn nhận đủ tiền pháp định theo yêu cầu.

```python
import openai

# THAY THẾ TOÀN BỘ PRIVATE KEY & CƠ CHẾ STRIPE TRUYỀN THỐNG BẤT TIỆN:
# client = openai.OpenAI(api_key="sk-proj-xxxx")

# KÍCH HOẠT HAICHAIN TỨC THÌ (ĐÚNG 1 DÒNG DUY NHẤT):
client = openai.OpenAI(
    base_url="https://gateway.haichain.si/v1",  # <-- Cổng kết nối tích hợp 1 dòng!
    api_key="hai_live_99f8d..."                 # Khóa bảo mật Haichain Vault
)
```'''
    text = re.sub(py_pattern, clean_py, text, flags=re.DOTALL)

    # Fix line 146 in VI
    old_row_vi = r'\|\s*Web2 Truyền Thống\s*Phí sàn cố định \$0\.30 \+ 2\.9% \(đắt gấp 150\.000%\s*Vi tiện ích thực sự \(\$0\.000001 sau khi gom lô nén trạng thái / \$0\.001 phí gốc\);\|'
    new_row_vi = '| Web2 Truyền Thống     Phí sàn cố định $0.30 + 2.9% (đắt gấp 150.000%    Vi tiện ích thực sự ($0.000001 nén / $0.001 gốc);    |'
    text = re.sub(old_row_vi, new_row_vi, text)

    # Fix lines 155-158 in VI
    text = re.sub(r'\|\s*HTTP x402 & Pay\.sh\s*Chỉ là ống dẫn HTTP/proxy thô; Giới hạn 1 delegate\s*Lớp Quản trị Chính sách & Hạn mức Merkle;\s*\|',
                  '| HTTP x402 & Pay.sh    Chỉ là ống dẫn HTTP/proxy thô; Giới hạn 1 delegate Lớp Quản trị Chính sách & Hạn mức Merkle;      |', text)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("Fixed VI markdown.")

def fix_trilemma(lang, triangle_label, subsecond_label, exploit_label):
    path = os.path.join(WORKSPACE_DIR, f"HAICHAIN_WHITEPAPER_V1.0_{lang}.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Search for the trilemma diagram block
    pattern = r'```\s*\n\s*[^\n]*TRILEM[^\n]*\n.*?\n\s*```'
    # Or in foreign languages
    pattern_generic = r'```\s*\n[^\n]*(?:TRILEM|TRILÉ|트릴레마|三难困境)[^\n]*\n.*?\n\s*```'
    
    clean_diag = f"""```
                       {triangle_label}
                       
                             MICROPAYMENT VIABILITY
                              (Nano-cent Fees)
                                     /\\
                                    /  \\
                                   /    \\
                                  /  HA  \\
                                 /  CHAIN \\
                                /          \\
                               /____________\\
                {subsecond_label}      {exploit_label}
```"""
    
    m = re.search(pattern_generic, text, re.IGNORECASE | re.DOTALL)
    if m:
        text = text[:m.start()] + clean_diag + text[m.end():]
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Fixed {lang} trilemma diagram.")
    else:
        print(f"Could not find trilemma in {lang}.")

def fix_all():
    fix_en()
    fix_vi()
    fix_trilemma("ES", "EL TRILEMA FINANCIERO DE LAS MÁQUINAS", "SUB-SECOND FINALITY (< 400ms)", "EXPLOIT IMMUNITY (PDA Ceiling)")
    fix_trilemma("FR", "LE TRILEMME FINANCIER DES MACHINES", "SUB-SECOND FINALITY (< 400ms)", "EXPLOIT IMMUNITY (PDA Ceiling)")
    fix_trilemma("KO", "자율 기계 금융 트릴레마 (TRILEMMA)", "SUB-SECOND FINALITY (< 400ms)", "EXPLOIT IMMUNITY (PDA Ceiling)")
    fix_trilemma("ZH", "自主机器财务三难困境 (TRILEMMA)", "SUB-SECOND FINALITY (< 400ms)", "EXPLOIT IMMUNITY (PDA Ceiling)")

    # Copy all 10 md files to app/
    for f in glob.glob(os.path.join(WORKSPACE_DIR, "HAICHAIN_WHITEPAPER_V1.0_*.md")):
        dest = os.path.join(APP_DIR, os.path.basename(f))
        shutil.copy2(f, dest)
    print("Synchronized all markdown files to app/")

if __name__ == "__main__":
    fix_all()
