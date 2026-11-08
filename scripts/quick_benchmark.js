const nacl = require('tweetnacl');
const crypto = require('crypto');
const { performance } = require('perf_hooks');

console.log("==========================================================");
console.log("   HAICHAIN OFF-CHAIN ED25519 STATE CHANNEL BENCHMARK    ");
console.log("==========================================================");

// 1. TweetNaCl benchmark
const keypair = nacl.sign.keyPair();
const msg = Buffer.from("HAICHAIN-VOUCHER-V1:TEST-POT:TEST-MERCHANT:CHAN42:AMOUNT50000:NONCE1");
const msgHash = crypto.createHash('sha256').update(msg).digest();
const sig = nacl.sign.detached(msgHash, keypair.secretKey);

const naclIters = 1000;
const t0 = performance.now();
for (let i = 0; i < naclIters; i++) {
  nacl.sign.detached.verify(msgHash, sig, keypair.publicKey);
}
const t1 = performance.now();
const naclAvg = (t1 - t0) / naclIters;
console.log(`[TweetNaCl Pure JS] ${naclIters} verifications: ${naclAvg.toFixed(4)} ms/op (${(1000/naclAvg).toFixed(0)} ops/sec)`);

// 2. Node.js Native crypto (OpenSSL Ed25519 C++ implementation)
const { publicKey, privateKey } = crypto.generateKeyPairSync('ed25519');
const nativeSig = crypto.sign(null, msg, privateKey);

const nativeIters = 5000;
const t2 = performance.now();
for (let i = 0; i < nativeIters; i++) {
  crypto.verify(null, msg, publicKey, nativeSig);
}
const t3 = performance.now();
const nativeAvg = (t3 - t2) / nativeIters;
console.log(`[Node Native Ed25519 (OpenSSL)] ${nativeIters} verifications: ${nativeAvg.toFixed(4)} ms/op (${(1000/nativeAvg).toFixed(0)} ops/sec)`);

console.log("\nComparison to Blockchain L1 block times:");
console.log(`- Bittensor (TAO) Block Time:    12,000 ms  (Haichain is ${(12000 / naclAvg).toFixed(0)}x faster)`);
console.log(`- Solana L1 Slot Time:           400 ms     (Haichain is ${(400 / naclAvg).toFixed(0)}x faster)`);
console.log(`- Traditional L1s (Ethereum):    12,000 ms  (Haichain is ${(12000 / naclAvg).toFixed(0)}x faster)`);
console.log("==========================================================");
