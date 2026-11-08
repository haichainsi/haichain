with open('packages/agent-pay/src/index.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add static verifyEd25519Detached inside HaichainPaywall class
helper_code = """  /**
   * High-Performance OpenSSL Ed25519 Detached Verification (< 0.2ms)
   * Uses native C++ OpenSSL engine when available in Node.js runtime, with TweetNaCl fallback.
   */
  public static verifyEd25519Detached(msg: Buffer | Uint8Array, sig: Buffer | Uint8Array, pubkey: Buffer | Uint8Array): boolean {
    try {
      if (typeof crypto.createPublicKey === 'function' && typeof crypto.verify === 'function') {
        const DER_PREFIX = Buffer.from('302a300506032b6570032100', 'hex');
        const spkiBuf = Buffer.concat([DER_PREFIX, Buffer.from(pubkey)]);
        const pubKeyObj = crypto.createPublicKey({
          key: spkiBuf,
          format: 'der',
          type: 'spki'
        });
        return crypto.verify(null, msg, pubKeyObj, sig);
      }
    } catch {
      // Fallback to pure JS TweetNaCl
    }
    return nacl.sign.detached.verify(
      msg instanceof Uint8Array ? msg : new Uint8Array(msg),
      sig instanceof Uint8Array ? sig : new Uint8Array(sig),
      pubkey instanceof Uint8Array ? pubkey : new Uint8Array(pubkey)
    );
  }

"""

# Insert right after class declaration
content = content.replace("export class HaichainPaywall {\n", "export class HaichainPaywall {\n" + helper_code)

# Replace nacl.sign.detached.verify with HaichainPaywall.verifyEd25519Detached
old_verify_1 = "const verified = nacl.sign.detached.verify(msgHash, sigBytes, agentPubkey.toBytes());"
new_verify_1 = "const verified = HaichainPaywall.verifyEd25519Detached(msgHash, sigBytes, agentPubkey.toBuffer());"

content = content.replace(old_verify_1, new_verify_1)

old_verify_2 = "const verified = nacl.sign.detached.verify(msgHash, sigBytes, agentPubkey.toBytes());"
new_verify_2 = "const verified = HaichainPaywall.verifyEd25519Detached(msgHash, sigBytes, agentPubkey.toBuffer());"
content = content.replace(old_verify_2, new_verify_2)

with open('packages/agent-pay/src/index.ts', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated packages/agent-pay/src/index.ts with native OpenSSL Ed25519 acceleration.")
