import re

for fpath in ['sale-controller.js', 'app/sale-controller.js']:
    with open(fpath, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Patch payNowBtn allocation
    code = code.replace(
        "paymentMethod: isEVM ? 'MetaMask Web3 Pay' : `${savedWallet.provider || 'Solana'} Web3 Pay`,\n            mainnetGuarantee: true",
        "paymentMethod: isEVM ? 'MetaMask Devnet Test' : `${savedWallet.provider || 'Solana'} Devnet Test`,\n            mainnetGuarantee: false,\n            isDevnetPrototype: true,\n            status: 'devnet_test_deposit'"
    )

    # 2. Patch submitBtn reservation
    code = code.replace(
        'txSignature: "4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU",\n            paymentMethod: isEvmAddr ? \'MetaMask Web3 SAFT\' : \'Solana Web3 SAFT\',\n            mainnetGuarantee: true',
        'txSignature: null,\n            paymentMethod: isEvmAddr ? \'MetaMask Devnet Interest\' : \'Solana Devnet Interest\',\n            mainnetGuarantee: false,\n            isDevnetPrototype: true,\n            status: \'devnet_waitlist_pending_legal_audit\''
    )

    # 3. Remove fake txSignature from referral ledger
    code = code.replace(
        'txSignature: "4MqTEpY6WCBE71PZ4jmH4dZWZQ5dmvQtK7i1A7ma3hMJknrkD6w297g8bTV6KKGRERmAwyrpQkh14eHMjHHWB2oU",',
        'txSignature: null,'
    )

    # 4. Patch alert msg
    old_msg_pat = re.compile(r"const msg = `\$\{getI18nText\('saftAlertTitle'\)\}.*?alert\(msg\);", re.DOTALL)
    new_msg_code = """const isVi = (typeof getActiveLang === 'function' ? getActiveLang() : 'vi') === 'vi';
        const msg = isVi
          ? `⚠️ ĐĂNG KÝ NGUYỆN VỌNG DEVNET (NON-BINDING WAITLIST)\\n\\nNhà đầu tư: ${name}\\nLượng token dự kiến: ${totalHai} $HAISI (@ $0.007)\\nNgân sách quan tâm: $${amount} USDT\\nĐịa chỉ ví: ${wallet}\\n\\nTHÔNG BÁO MINH BẠCH & PHÁP LÝ:\\n- Haichain hiện đang là phiên bản thử nghiệm công nghệ (Devnet Prototype v0.1.0) và đang hoàn thiện kiểm toán bảo mật độc lập.\\n- KHÔNG CÓ BẤT KỲ GIAO DỊCH BÁN TOKEN HOẶC THU TIỀN THẬT NÀO ĐƯỢC XỬ LÝ TRÊN MAINNET.\\n- Tuyệt đối KHÔNG gửi tiền thật vào bất kỳ địa chỉ ví nào.\\n- Mọi thông tin phân bổ chỉ có tính chất danh sách chờ kỹ thuật (non-binding waitlist) cho đến khi dự án hoàn tất thủ tục pháp lý và kiểm toán độc lập.`
          : `⚠️ DEVNET STRATEGIC INTEREST WAITLIST REGISTERED\\n\\nSignatory: ${name}\\nProposed Allocation: ${totalHai} $HAISI (@ $0.007)\\nTarget Budget: $${amount} USDT\\nWallet Address: ${wallet}\\n\\nLEGAL & SECURITY DISCLOSURE:\\n- Haichain is currently in Devnet Prototype (v0.1.0) phase undergoing technical hardening and independent audit preparation.\\n- NO REAL TOKEN SALE OR FUNDRAISING TRANSACTION HAS OCCURRED ON MAINNET.\\n- Do NOT send real funds to any cryptocurrency address.\\n- All submitted expressions of interest are strictly non-binding technical reservations until formal legal structure and independent audit completion.`;
        alert(msg);"""
    code = old_msg_pat.sub(new_msg_code, code)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f'[OK] Patched token sale in {fpath}')
