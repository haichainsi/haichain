import time
from cryptography.hazmat.primitives.asymmetric import ed25519

private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()
msg = b"HAICHAIN-VOUCHER-V1:TEST-POT:TEST-MERCHANT:CHAN42:AMOUNT50000:NONCE1"
sig = private_key.sign(msg)

iters = 10000
# Warmup
for _ in range(500):
    public_key.verify(sig, msg)

t0 = time.perf_counter()
for _ in range(iters):
    public_key.verify(sig, msg)
t1 = time.perf_counter()

avg_ms = ((t1 - t0) / iters) * 1000
print(f"[Python OpenSSL Ed25519] {iters} verifications: {avg_ms:.4f} ms/op ({(1000/avg_ms):.0f} ops/sec)")
print(f"Meets < 0.3ms specification? {'YES' if avg_ms < 0.3 else 'NO'}")
