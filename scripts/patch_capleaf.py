p = "sdk/typescript/src/capleaf.ts"
with open(p, "r", encoding="utf-8") as f:
    c = f.read().replace("\r\n", "\n")

old_fn = """  public static verifyProof(
    leafHash: Buffer,
    proof: Buffer[],
    leafIndex: number,
    expectedRoot: Buffer
  ): boolean {
    let currentHash = Buffer.from(leafHash);
    let index = leafIndex;

    for (let i = 0; i < proof.length; i++) {
      const sibling = proof[i];
      const isRightSibling = (index & 1) === 0;

      if (isRightSibling) {
        currentHash = this.computeMerkleNode(currentHash, sibling);
      } else {
        currentHash = this.computeMerkleNode(sibling, currentHash);
      }
      index = index >> 1;
    }

    return currentHash.equals(expectedRoot);
  }"""

new_fn = """  public static verifyProof(
    leafHash: Buffer,
    proof: Buffer[],
    leafIndex: number,
    expectedRoot: Buffer
  ): boolean {
    let currentHash: Uint8Array = leafHash;
    let index = leafIndex;

    for (let i = 0; i < proof.length; i++) {
      const sibling = proof[i];
      const isRightSibling = (index & 1) === 0;

      if (isRightSibling) {
        currentHash = this.computeMerkleNode(currentHash, sibling);
      } else {
        currentHash = this.computeMerkleNode(sibling, currentHash);
      }
      index = index >> 1;
    }

    return Buffer.from(currentHash).equals(expectedRoot);
  }"""

if old_fn in c:
    c = c.replace(old_fn, new_fn)
    with open(p, "w", encoding="utf-8", newline="\r\n") as f:
        f.write(c)
    print("capleaf verifyProof fixed!")
else:
    print("capleaf target not found")
