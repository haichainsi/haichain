const crypto = require('crypto');
const nacl = require('tweetnacl');
const { performance } = require('perf_hooks');

const keypair = nacl.sign.keyPair();
const msg = Buffer.from("HAICHAIN-VOUCHER-V1:TEST");
const sig = nacl.sign.detached(msg, keypair.secretKey);

function verifyEd25519Fast(rawPubkey, message, signature) {
  try {
    // Wrap raw 32 bytes in DER SPKI prefix
    const DER_PREFIX = Buffer.from('302a300506032b6570032100', 'hex');
    const spkiBuf = Buffer.concat([DER_PREFIX, rawPubkey]);
    const pubKeyObj = crypto.createPublicKey({
      key: spkiBuf,
      format: 'der',
      type: 'spki'
    });
    return crypto.verify(null, message, pubKeyObj, signature);
  } catch (err) {
    // Fallback to tweetnacl if DER fails
    return nacl.sign.detached.verify(message, signature, rawPubkey);
  }
}

// Test correctness
const ok = verifyEd25519Fast(keypair.publicKey, msg, sig);
console.log("Correctness check:", ok);

// Benchmark 5000 iterations
const t0 = performance.now();
for (let i = 0; i < 5000; i++) {
  const verified = verifyEd25519Fast(keypair.publicKey, msg, sig);
  if (!verified) throw new Error("Failed");
}
const t1 = performance.now();
const avg = (t1 - t0) / 5000;
console.log(`Average latency with fast-path: ${avg.toFixed(4)} ms (${(1000/avg).toFixed(0)} ops/sec)`);
