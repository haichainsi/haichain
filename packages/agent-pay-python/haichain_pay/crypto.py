"""
HAICHAIN Cryptographic Utilities for Fast-Path Off-Chain Vouchers (< 2ms)
Compatible with Solana Ed25519, HAICHAIN CapLeaf, and Coinbase x402 standards.
"""

import base64
import hashlib
from typing import Union
import nacl.signing
import nacl.exceptions

B58_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def b58decode(v: str) -> bytes:
    """Decode a base58 encoded string (e.g. Solana PublicKey) into raw bytes."""
    v = v.strip()
    num = 0
    for char in v:
        idx = B58_ALPHABET.find(char)
        if idx == -1:
            raise ValueError(f"Invalid Base58 character: '{char}'")
        num = num * 58 + idx
    
    combined = num.to_bytes((num.bit_length() + 7) // 8, "big") if num > 0 else b""
    pad = len(v) - len(v.lstrip("1"))
    return b"\x00" * pad + combined


def b58encode(raw: bytes) -> str:
    """Encode raw bytes into a base58 string."""
    origlen = len(raw)
    raw_stripped = raw.lstrip(b"\x00")
    pad = origlen - len(raw_stripped)
    num = int.from_bytes(raw_stripped, "big")
    res = []
    while num > 0:
        num, rem = divmod(num, 58)
        res.append(B58_ALPHABET[rem])
    return ("1" * pad) + "".join(reversed(res))


def to_32_bytes(key: Union[str, bytes]) -> bytes:
    """Normalize a public key from base58 string or bytes into exact 32 bytes."""
    if isinstance(key, str):
        decoded = b58decode(key)
    elif isinstance(key, (bytes, bytearray)):
        decoded = bytes(key)
    else:
        raise TypeError("Key must be base58 string or bytes")

    if len(decoded) != 32:
        raise ValueError(f"Public key must be exactly 32 bytes, got {len(decoded)}")
    return decoded


def compute_voucher_hash(
    pot_pubkey: Union[str, bytes],
    merchant_pubkey: Union[str, bytes],
    channel_id: int,
    cumulative_amount: int,
    nonce: int = 0,
) -> bytes:
    """
    Computes the canonical SHA-256 voucher digest for HAICHAIN State Channels:
    SHA256(b"HAICHAIN-VOUCHER-V1" + pot_pubkey + merchant_pubkey + channel_id_u64le + amount_u64le + nonce_u64le)
    """
    pot_bytes = to_32_bytes(pot_pubkey)
    merchant_bytes = to_32_bytes(merchant_pubkey)
    channel_buf = int(channel_id).to_bytes(8, byteorder="little", signed=False)
    amount_buf = int(cumulative_amount).to_bytes(8, byteorder="little", signed=False)
    nonce_buf = int(nonce).to_bytes(8, byteorder="little", signed=False)

    hasher = hashlib.sha256()
    hasher.update(b"HAICHAIN-VOUCHER-V1")
    hasher.update(pot_bytes)
    hasher.update(merchant_bytes)
    hasher.update(channel_buf)
    hasher.update(amount_buf)
    hasher.update(nonce_buf)
    return hasher.digest()


def compute_x402_canonical_hash(resource: str, amount: Union[int, float, str], nonce: str) -> bytes:
    """Canonical hash for standard detached x402 challenges."""
    raw = f"{resource}:{amount}:{nonce}".encode("utf-8")
    return hashlib.sha256(raw).digest()


def verify_ed25519_signature(
    public_key: Union[str, bytes],
    message_digest: bytes,
    signature: Union[str, bytes],
) -> bool:
    """
    High-velocity Ed25519 detached signature verification (<0.5ms).
    Returns True if valid, False otherwise.
    """
    try:
        pk_bytes = to_32_bytes(public_key)
        if isinstance(signature, str):
            sig_bytes = base64.b64decode(signature)
        else:
            sig_bytes = bytes(signature)

        if len(sig_bytes) != 64:
            return False

        verify_key = nacl.signing.VerifyKey(pk_bytes)
        verify_key.verify(message_digest, sig_bytes)
        return True
    except (nacl.exceptions.BadSignatureError, Exception):
        return False
