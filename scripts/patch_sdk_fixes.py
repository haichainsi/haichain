import os

# 1. Patch sdk/typescript/src/index.ts
p1 = "sdk/typescript/src/index.ts"
with open(p1, "r", encoding="utf-8") as f:
    c1 = f.read()

c1_norm = c1.replace("\r\n", "\n")
old_req = """export interface UsdtDepositSessionRequest {
  userUid: string;
  amountUsdt: number;
  sourceNetwork?: SupportedCrossChainNetwork;
  preferredRail?: SupportedPaymentRail;
}"""
new_req = """export interface UsdtDepositSessionRequest {
  userUid: string;
  amountUsdt: number;
  sourceNetwork?: SupportedCrossChainNetwork;
  preferredRail?: SupportedPaymentRail;
  agentVaultOwner?: string;
}"""

if old_req in c1_norm:
    c1_norm = c1_norm.replace(old_req, new_req)
    with open(p1, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(c1_norm)
    print("index.ts updated!")
else:
    print("index.ts target not found")

# 2. Patch sdk/typescript/src/capleaf.ts
p2 = "sdk/typescript/src/capleaf.ts"
with open(p2, "r", encoding="utf-8") as f:
    c2 = f.read()

c2_norm = c2.replace("\r\n", "\n")
old_node = "public static computeMerkleNode(left: Buffer, right: Buffer): Buffer {"
new_node = "public static computeMerkleNode(left: Uint8Array, right: Uint8Array): Buffer {"
c2_norm = c2_norm.replace(old_node, new_node)

with open(p2, "w", encoding="utf-8", newline="\r\n") as f:
    f.write(c2_norm)
print("capleaf.ts updated!")
