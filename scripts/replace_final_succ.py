def replace_final_succ(file_path):
    print(f"Replacing final succ in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    old_block = """        alert(isVi
          ? `🎉 GIAO DỊCH VÀ ĐĂNG KÝ SAFT THÀNH CÔNG!

Ví của bạn (${wallet.slice(0, 6)}...${wallet.slice(-4)}) đã chính thức sở hữu ${totalHaiNum.toLocaleString()} $HAISI.

🛡️ BẢO CHỨNG CHUYỂN ĐỔI MAINNET:
Toàn bộ ${totalHaiNum.toLocaleString()} $HAISI đã được bảo lưu bất biến theo Hợp đồng SAFT. Ngay khi HAICHAIN chính thức kích hoạt mạng Mainnet (Sự kiện TGE), hợp đồng thông minh Solana Token-2022 sẽ tự động giải ngân và chuyển đổi 100% số token này thành Token Thật on-chain về đúng địa chỉ ví này của bạn mà không cần thủ tục nào khác.

Hệ thống đang chuyển bạn đến Két sắt Vesting để kiểm tra số dư và chứng nhận phân bổ.`
          : `🎉 TRANSACTION CONFIRMED & SAFT ALLOCATION RECORDED!

Your wallet (${wallet.slice(0, 6)}...${wallet.slice(-4)}) now officially holds ${totalHaiNum.toLocaleString()} $HAISI.

🛡️ OFFICIAL MAINNET GUARANTEE:
All ${totalHaiNum.toLocaleString()} $HAISI are immutably bound under the SAFT contract. Upon HAICHAIN Mainnet TGE, the Solana Token-2022 smart contract will automatically disburse 100% real tokens directly to this wallet address without manual intervention.

Redirecting to your Vesting Vault tab.`);"""

    new_block = """        alert(getI18nText('saftSuccessAlert')
          .replace('{shortWallet}', `${wallet.slice(0, 6)}...${wallet.slice(-4)}`)
          .replace(/{tokens}/g, totalHaiNum.toLocaleString()));"""

    if old_block in content:
        content = content.replace(old_block, new_block)
        print("  Replaced success alert block successfully")
    else:
        print("  WARN: old_block not found")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

replace_final_succ('sale-controller.js')
replace_final_succ('app/sale-controller.js')
