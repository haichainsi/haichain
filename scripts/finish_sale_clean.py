import re

def finish_sale_clean(file_path):
    print(f"Finishing sale clean in {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().replace('\r\n', '\n')

    # 1. Replace confirmMsg
    pattern_cmsg = r'const confirmMsg = isVi\s*\?\s*`XÁC NHẬN THANH TOÁN MUA \$HAISI[\s\S]*?Your \$\{provName\} wallet will open for cryptographic authorization\.`;'
    r_cmsg = """const confirmMsg = getI18nText('confirmMsgInvestment')
          .replace(/{provider}/g, provName)
          .replace('{amount}', amount.toLocaleString())
          .replace('{tokens}', totalHaiNum.toLocaleString())
          .replace('{wallet}', wallet);"""
    content = re.sub(pattern_cmsg, r_cmsg, content)

    # 2. Lines 1723-1725 solSignErr
    old_sol_cancel = "alert(isVi ? 'Bạn đã hủy yêu cầu ký duyệt trên ví.' : 'Transaction was cancelled in your wallet.');"
    new_sol_cancel = "alert(getI18nText('solanaTxCancelled'));"
    content = content.replace(old_sol_cancel, new_sol_cancel)

    old_sol_err = "alert(isVi ? ('Lỗi ví: ' + (solSignErr.message || solSignErr)) : ('Wallet error: ' + (solSignErr.message || solSignErr)));"
    new_sol_err = "alert(getI18nText('solanaErrorPrefix') + ' ' + (solSignErr.message || solSignErr));"
    content = content.replace(old_sol_err, new_sol_err)

    # 3. Success alert
    pattern_succ = r'alert\(isVi\s*\?\s*`🎉 GIAO DỊCH VÀ ĐĂNG KÝ SAFT THÀNH CÔNG![\s\S]*?Redirecting to your dedicated Vesting Vault tab\.`\);'
    r_succ = """alert(getI18nText('saftSuccessAlert')
              .replace('{shortWallet}', `${wallet.slice(0, 6)}...${wallet.slice(-4)}`)
              .replace(/{tokens}/g, totalHaiNum.toLocaleString()));"""
    content = re.sub(pattern_succ, r_succ, content)

    # Also remove any unused `const isVi = getActiveLang() === 'vi';`
    content = re.sub(r'^\s*const isVi = getActiveLang\(\) === \'vi\';\s*\n', '', content, flags=re.MULTILINE)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {file_path}")

finish_sale_clean('sale-controller.js')
finish_sale_clean('app/sale-controller.js')
