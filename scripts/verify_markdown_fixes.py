import glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\Surface\Documents\8. HAICHAIN"

files = glob.glob(os.path.join(WORKSPACE_DIR, "HAICHAIN_WHITEPAPER_V1.0_*.md"))

all_ok = True
for fpath in sorted(files):
    fname = os.path.basename(fpath)
    with open(fpath, "r", encoding="utf-8") as f:
        c = f.read()

    has_old = "THE AUTONOMOUS MACHINE FINANCIAL & SETTLEMENT OPERATING SYSTEM" in c
    has_new = "The Economic Bedrock for the Symbiotic Superintelligence Era AI²" in c
    # check backticks around OP_402_PAY in TOC (first 10000 chars)
    has_tick = "`OP_402_PAY`" in c[:10000]
    # check 6.4 duplication
    count_64 = c[:10000].count("6.4.")

    status = "OK" if (not has_old and has_new and not has_tick and count_64 <= 1) else "FAIL"
    if status == "FAIL":
        all_ok = False
    print(f"[{status}] {fname}: old_banner={has_old}, new_banner={has_new}, tick_in_toc={has_tick}, count_6.4={count_64}")

if all_ok:
    print("\nALL 10 MARKDOWN FILES PASSED VERIFICATION 100%!")
else:
    print("\nSOME FILES FAILED VERIFICATION!")
