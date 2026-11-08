const nacl = require('tweetnacl');
const crypto = require('crypto');
const { performance } = require('perf_hooks');

// Generate test keypair
const keypair = nacl.sign.keyPair();

// Prepare canonical voucher message
const msg = Buffer.from("HAICHAIN-VOUCHER-V1:TEST-POT:TEST-MERCHANT:CHAN42:AMOUNT50000:NONCE1");
const msgHash = crypto.createHash('sha256').update(msg).digest();

// Sign
const sig = nacl.sign.detached(msgHash, keypair.secretKey);

// Benchmark verification latency
const ITERATIONS = 10000;

// Warmup
for (let i = 0; i < 500; i++) {
  nacl.sign.detached.verify(msgHash, sig, keypair.publicKey);
}

const start = performance.now();
for (let i = 0; i < ITERATIONS; i++) {
  const ok = nacl.sign.detached.verify(msgHash, sig, keypair.publicKey);
  if (!ok) throw new Error("Verification failed");
}
const end = performance.now();

const totalTimeMs = end - start;
const avgLatencyMs = totalTimeMs / ITERATIONS;
const opsPerSec = (ITERATIONS / (totalTimeMs / 1000)).toFixed(0);

console.log("==========================================================");
console.log("   HAICHAIN OFF-CHAIN ED25519 STATE CHANNEL BENCHMARK    ");
console.log("==========================================================");
console.log(`Total iterations verified: ${ITERATIONS}`);
console.log(`Total elapsed time:        ${totalTimeMs.toFixed(2)} ms`);
console.log(`Average latency per tick:  ${avgLatencyMs.toFixed(4)} ms (${(avgLatencyMs * 1000).toFixed(1)} microseconds)`);
console.log(`Verification throughput:   ${opsPerSec} ops/second`);
console.log(`Matches < 0.3ms claim?     ${avgLatencyMs < 0.3 ? '✅ YES (< 0.3ms)' : '❌ NO'}`);
console.log("==========================================================");
