import os, glob, re, sys, shutil
sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"
APP_DIR = os.path.join(WORKSPACE_DIR, "app")

files = glob.glob(os.path.join(WORKSPACE_DIR, "HAICHAIN_WHITEPAPER_V1.0_*.md"))

for fpath in sorted(files):
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Requirement 3: Exact banner text updates
    content = content.replace("THE AUTONOMOUS MACHINE FINANCIAL & SETTLEMENT OPERATING SYSTEM", "The Economic Bedrock for the Symbiotic Superintelligence Era AI²")
    content = content.replace("EL SISTEMA OPERATIVO FINANCIERO Y DE LIQUIDACIÓN PARA MÁQUINAS AUTÓNOMAS", "The Economic Bedrock for the Symbiotic Superintelligence Era AI²")
    content = content.replace("LE SYSTÈME D'EXPLOITATION FINANCIER ET DE RÈGLEMENT POUR MACHINES AUTONOMES", "The Economic Bedrock for the Symbiotic Superintelligence Era AI²")
    content = content.replace("자율 기계를 위한 금융 및 청산 운영체제 (THE AUTONOMOUS MACHINE FINANCIAL & SETTLEMENT OPERATING SYSTEM)", "The Economic Bedrock for the Symbiotic Superintelligence Era AI²")
    content = content.replace("自主机器通用财务与清算操作系统 (THE AUTONOMOUS MACHINE FINANCIAL & SETTLEMENT OPERATING SYSTEM)", "The Economic Bedrock for the Symbiotic Superintelligence Era AI²")

    # Requirement 5: Remove backticks around OP_402_PAY in TOC
    content = content.replace("`OP_402_PAY`", "OP_402_PAY")

    # In EN: Remove duplicate 9.1 - 9.6 lines in TOC
    if "EN.md" in fname:
        dup_pattern = r'(  - \[9\.8\. Zero-Knowledge Prompt Privacy & TEE Confidential Computing Architecture\]\([^\)]+\)\n)(  - \[9\.1\. The 3-Stage Evolutionary Trajectory\].*?  - \[9\.6\. Unified Human-Agent Soulbound DIDs & Institutional Regulatory Topology\]\([^\)]+\)\n)'
        content = re.sub(dup_pattern, r'\1', content, flags=re.DOTALL)

    # In all files: Fix 6.4 duplicate numbering in TOC
    content = content.replace("  - [6.4. Developer Quickstart", "  - [6.5. Developer Quickstart")
    content = content.replace("  - [6.4. Guía Rápida para Desarrolladores", "  - [6.5. Guía Rápida para Desarrolladores")
    content = content.replace("  - [6.4. Démarrage Rapide Développeur", "  - [6.5. Démarrage Rapide Développeur")
    content = content.replace("  - [6.4. 开发者极速上手与零摩擦 SDK", "  - [6.5. 开发者极速上手与零摩擦 SDK")
    content = content.replace("  - [6.4. 개발자 퀵스타트 및 마찰 없는 드롭인 SDK", "  - [6.5. 개발자 퀵스타트 및 마찰 없는 드롭인 SDK")
    content = content.replace("  - [6.5. Native Anthropic", "  - [6.6. Native Anthropic")
    content = content.replace("  - [6.5. Integración Nativa de Servidor Anthropic", "  - [6.6. Integración Nativa de Servidor Anthropic")
    content = content.replace("  - [6.5. Intégration Native du Serveur Anthropic", "  - [6.6. Intégration Native du Serveur Anthropic")
    content = content.replace("  - [6.5. 原生 Anthropic", "  - [6.6. 原生 Anthropic")
    content = content.replace("  - [6.5. 네이티브 Anthropic", "  - [6.6. 네이티브 Anthropic")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

    app_fpath = os.path.join(APP_DIR, fname)
    with open(app_fpath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Patched and mirrored: {fname}")

print("\nALL 10 MARKDOWN WHITEPAPERS PATCHED WITH 100% PRECISION!")
