def clean_dash_last_2(file_path):
    print(f"Cleaning last 2 in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Line 3871
    old_1 = "walletBtnText.textContent = getDashNotice('connectingMetaMask') || (isVi ? 'Đang mở MetaMask...' : 'Opening MetaMask...');"
    new_1 = "walletBtnText.textContent = getDashNotice('connectingMetaMask');"
    content = content.replace(old_1, new_1)

    # Line 6129
    old_2 = 'alert(isVi ? "Đang chuyển sang ứng dụng MetaMask để bạn xác nhận giao dịch bằng tiền thật..." : "Redirecting to MetaMask App to approve transaction with real funds...");'
    new_2 = "alert(getDashNotice('redirectMetaMaskRealTx'));"
    content = content.replace(old_2, new_2)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

clean_dash_last_2('dashboard.html')
clean_dash_last_2('app/dashboard.html')
