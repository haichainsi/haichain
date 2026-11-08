const path = require('path');
const { HaichainPaywall } = require(path.resolve(__dirname, '../packages/agent-pay/dist/index.js'));
const nacl = require('tweetnacl');
const { performance } = require('perf_hooks');

console.log("==========================================================");
console.log("   TESTING COMPILED @haichainsi/agent-pay ACCELERATION    ");
console.log("==========================================================");

const keypair = nacl.sign.keyPair();
const msg = Buffer.from("HAICHAIN-VOUCHER-V1:TEST");
const sig = nacl.sign.detached(msg, keypair.secretKey);

// Test static method
const ok = HaichainPaywall.verifyEd25519Detached(msg, sig, keypair.publicKey);
console.log("Correctness check:", ok);

// Benchmark 5,000 iterations
const t0 = performance.now();
for (let i = 0; i < 5000; i++) {
  const verified = HaichainPaywall.verifyEd25519Detached(msg, sig, keypair.publicKey);
  if (!verified) throw new Error("Failed");
}
const t1 = performance.now();
const avg = (t1 - t0) / 5000;
console.log(`Average latency per verification: ${avg.toFixed(4)} ms (${(1000/avg).toFixed(0)} ops/sec)`);
console.log(`Meets < 0.3ms specification?       ${avg < 0.3 ? '✅ YES (< 0.3ms)' : '❌ NO'}`);
console.log("==========================================================");
