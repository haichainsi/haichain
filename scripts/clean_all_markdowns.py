import sys, re, os, glob
sys.stdout.reconfigure(encoding='utf-8')

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    orig_text = text

    # 1. Fix corrupted LaTeX sequences first
    text = text.replace('\x07lpha', r'\alpha')
    text = text.replace('\x0cac', r'\frac')
    text = text.replace('\rac', r'\frac')
    text = re.sub(r'(?<![a-zA-Z\\])rac\{', r'\\frac{', text)
    text = re.sub(r'(?<![a-zA-Z\\])ight\)', r'\\right)', text)
    text = re.sub(r'(?<![a-zA-Z\\])ight\]', r'\\right]', text)
    text = re.sub(r'(?<![a-zA-Z\\])ight\\\|', r'\\right\\|', text)
    text = re.sub(r'(?<![a-zA-Z\\])eg\\text', r'\\neg \\text', text)
    text = re.sub(r'(?<![a-zA-Z\\])eg \text', r'\\neg \\text', text)
    text = re.sub(r'2\s*imes', r'2\\times', text)

    # 2. Fix stray backslashes before dollar signs: \$ -> $
    text = text.replace(r'\$', '$')

    # 3. Fix $AI^2$ and variants to AI²
    # Protect math blocks temporarily if needed, but in text and headers replace $AI^2$ -> AI²
    # Replace \mathbf{AI^2} in text: **$\mathbf{AI^2}$ (AI Bình Phương)** -> **AI² (AI Bình Phương)**
    text = re.sub(r'\*\*\$\\mathbf\{AI\^2\}\$\s*\(([^)]+)\)\*\*', r'**AI² (\1)**', text)
    text = re.sub(r'\$\\mathbf\{AI\^2\}\$', r'AI²', text)
    text = re.sub(r'\*\*\$AI\^2\$\*\*', r'**AI²**', text)
    text = re.sub(r'\$AI\^2\$', r'AI²', text)
    text = re.sub(r'AI\^2(?!\w)', r'AI²', text)
    text = re.sub(r'\$A\^2\$', r'AI²', text)

    # Also check if any remaining $AI²$ exists
    text = re.sub(r'\$AI²\$', r'AI²', text)

    # 4. Ensure display math blocks ($$...$$) have blank lines before and after
    # Pattern to find $$...$$ that does not have blank line before or after
    def isolate_display_math(match):
        inner = match.group(1).strip()
        return f"\n\n$${inner}$$\n\n"
    
    # We match $$...$$ across lines
    text = re.sub(r'(?<!\n)\s*\n?(\$\$[\s\S]*?\$\$)\n?\s*(?!\n)', isolate_display_math, text)
    # Clean up excessive blank lines (3+ newlines -> 2 newlines)
    text = re.sub(r'\n{3,}', '\n\n', text)

    if text != orig_text:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"[OK] Updated {filepath}")
    else:
        print(f"[NO CHANGE] {filepath}")

if __name__ == "__main__":
    for fname in sorted(glob.glob("HAICHAIN_WHITEPAPER_V1.0_*.md")):
        clean_file(fname)
        app_fname = os.path.join("app", fname)
        if os.path.exists(app_fname):
            clean_file(app_fname)
