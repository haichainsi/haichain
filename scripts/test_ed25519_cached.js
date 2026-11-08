const crypto = require('crypto');
const nacl = require('tweetnacl');
const { performance } = require('perf_hooks');

const keypair = nacl.sign.keyPair();
const msg = Buffer.from("HAICHAIN-VOUCHER-V1:TEST");
const sig = nacl.sign.detached(msg, keypair.secretKey);

const pubKeyCache = new Map();

function verifyEd25519Cached(rawPubkey, message, signature) {
  try {
    const pubKeyBase58 = rawPubkey.toString('hex');
    let pubKeyObj = pubKeyCache.get(pubKeyBase58);
    if (!pubKeyObj) {
      const DER_PREFIX = Buffer.from('302a300506032b6570032100', 'hex');
      const spkiBuf = Buffer.concat([DER_PREFIX, rawPubkey]);
      pubKeyObj = crypto.createPublicKey({
        key: spkiBuf,
        format: 'der',
        type: 'spki'
      });
      pubKeyCache.set(pubKeyBase58, pubKeyObj);
    }
    return crypto.verify(null, message, pubKeyObj, signature);
  } catch (err) {
    return nacl.sign.detached.verify(message, signature, rawPubkey);
  }
}

// Benchmark 10,000 iterations with cache
const t0 = performance.now();
for (let i = 0; i < 10000; i++) {
  const verified = verifyEd25519Cached(Buffer.from(keypair.publicKey), msg, sig);
  if (!verified) throw new Error("Failed");
}
const t1 = performance.now();
const avg = (t1 - t0) / 10000;
console.log(`Memoized OpenSSL Ed25519 latency: ${avg.toFixed(4)} ms (${(1000/avg).toFixed(0)} ops/sec)`);
