with open('programs/haichain-core/src/lib.rs', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix 1: ProviderBondAccount missing closing brace
target1 = "    pub bump: u8,\n\n\n// ============================================================================"
replace1 = "    pub bump: u8,\n}\n\n// ============================================================================"

if target1 not in text:
    # check CRLF
    target1 = target1.replace('\n', '\r\n')
    replace1 = replace1.replace('\n', '\r\n')

if target1 in text:
    text = text.replace(target1, replace1)
    print("Fixed ProviderBondAccount closing brace.")
else:
    print("Warning: target1 not found.")

# Fix 2: stray comma on line 779
target2 = "    InvalidNonceSequence,\n,"
replace2 = "    InvalidNonceSequence,"

if target2 not in text:
    target2 = target2.replace('\n', '\r\n')
    replace2 = replace2.replace('\n', '\r\n')

if target2 in text:
    text = text.replace(target2, replace2)
    print("Fixed stray comma in enum.")
else:
    print("Warning: target2 not found.")

with open('programs/haichain-core/src/lib.rs', 'w', encoding='utf-8') as f:
    f.write(text)
print("Finished patching lib.rs")
