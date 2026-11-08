def clean_last_two(file_path):
    print(f"Cleaning last two in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # Line 1458
    old_1 = 'alert(isVi ? "Vui lòng kết nối ví Web3 (MetaMask, Phantom hoặc Solflare) để thực hiện thanh toán SAFT!" : "Please connect a Web3 wallet (MetaMask, Phantom, or Solflare) to proceed with SAFT payment!");'
    new_1 = "alert(getI18nText('connectWeb3Required'));"
    if old_1 in content:
        content = content.replace(old_1, new_1)
        print("  Replaced alert connectWeb3Required")
    else:
        print("  WARN: old_1 not found")

    # Line 1525
    old_2 = "cancelText: isVi ? 'Huỷ Bỏ' : 'Cancel'"
    new_2 = "cancelText: getI18nText('cancelBtn')"
    if old_2 in content:
        content = content.replace(old_2, new_2)
        print("  Replaced cancelText")
    else:
        print("  WARN: old_2 not found")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

clean_last_two('sale-controller.js')
clean_last_two('app/sale-controller.js')
