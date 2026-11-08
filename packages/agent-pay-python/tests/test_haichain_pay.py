"""
Comprehensive Unit Tests for HAICHAIN Python SDK (haichain-agent-pay)
Covers cryptographic voucher hashing, sub-millisecond Ed25519 verification,
nullifier replay prevention, FastAPI @haichain_paywall decorator, and ASGI middleware.
"""

import base64
import json
import time
import unittest
from fastapi import FastAPI, Request
from starlette.testclient import TestClient

from haichain_pay import (
    HaichainPaywall,
    haichain_paywall,
    HaichainClient,
    b58decode,
    b58encode,
    compute_voucher_hash,
    verify_ed25519_signature,
)

MERCHANT_PUBKEY = "FiArjiLPRvU5wMEXeGwKTQfVSQiSTcxhmQwsEe2SzFRR"
POT_PUBKEY = "7owJKWDhT7qimkTf4qc6fuDtgk65LzsWad7EVuYZHYMd"


class TestHaichainPay(unittest.TestCase):

    def test_base58_roundtrip(self):
        test_bytes = b"\x00\x01\x02\x03\x04" * 6 + b"\x05\x06"
        encoded = b58encode(test_bytes)
        decoded = b58decode(encoded)
        self.assertEqual(decoded, test_bytes)

    def test_voucher_hash_calculation(self):
        h1 = compute_voucher_hash(POT_PUBKEY, MERCHANT_PUBKEY, 1, 1000, 123)
        self.assertEqual(len(h1), 32)
        # Deterministic
        h2 = compute_voucher_hash(POT_PUBKEY, MERCHANT_PUBKEY, 1, 1000, 123)
        self.assertEqual(h1, h2)
        # Different nonce produces different digest
        h3 = compute_voucher_hash(POT_PUBKEY, MERCHANT_PUBKEY, 1, 1000, 124)
        self.assertNotEqual(h1, h3)

    def test_fast_path_verification_under_2ms(self):
        client = HaichainClient(pot_pubkey=POT_PUBKEY)
        paywall = HaichainPaywall(recipient=MERCHANT_PUBKEY, price_usdt=0.005)

        # Warm-up call
        warmup_voucher = client.create_voucher(merchant_pubkey=MERCHANT_PUBKEY, amount_microunit=1000, channel_id=1)
        paywall.verify_payment(f"X402 {base64.b64encode(json.dumps(warmup_voucher).encode()).decode()}")

        # Timed call
        voucher = client.create_voucher(merchant_pubkey=MERCHANT_PUBKEY, amount_microunit=5000, channel_id=1)
        auth_header = f"X402 {base64.b64encode(json.dumps(voucher).encode()).decode()}"

        start = time.perf_counter()
        res = paywall.verify_payment(auth_header)
        elapsed_ms = (time.perf_counter() - start) * 1000

        self.assertTrue(res["valid"])
        self.assertEqual(res["mode"], "fast-path-voucher")
        self.assertLess(elapsed_ms, 2.0, f"Verification took {elapsed_ms:.2f}ms, expected < 2.0ms")

    def test_tampered_signature_rejected(self):
        client = HaichainClient(pot_pubkey=POT_PUBKEY)
        paywall = HaichainPaywall(recipient=MERCHANT_PUBKEY, price_usdt=0.005)

        voucher = client.create_voucher(merchant_pubkey=MERCHANT_PUBKEY, amount_microunit=5000, channel_id=1)
        
        # Tamper with the amount
        voucher["cumulativeAmount"] = "9999999"
        auth_header = f"X402 {base64.b64encode(json.dumps(voucher).encode()).decode()}"

        res = paywall.verify_payment(auth_header)
        self.assertFalse(res["valid"])
        self.assertIn("Invalid Ed25519 signature", res["reason"])

    def test_nullifier_store_replay_attack_prevention(self):
        client = HaichainClient(pot_pubkey=POT_PUBKEY)
        paywall = HaichainPaywall(recipient=MERCHANT_PUBKEY, price_usdt=0.005)

        voucher = client.create_voucher(merchant_pubkey=MERCHANT_PUBKEY, amount_microunit=5000, channel_id=1)
        auth_header = f"X402 {base64.b64encode(json.dumps(voucher).encode()).decode()}"

        # First attempt: SUCCESS
        res1 = paywall.verify_payment(auth_header)
        self.assertTrue(res1["valid"])

        # Replay attempt: REJECTED
        res2 = paywall.verify_payment(auth_header)
        self.assertFalse(res2["valid"])
        self.assertIn("Replay Attack Rejected", res2["reason"])

    def test_stale_voucher_rejection(self):
        client = HaichainClient(pot_pubkey=POT_PUBKEY)
        paywall = HaichainPaywall(recipient=MERCHANT_PUBKEY, max_age_seconds=10)

        voucher = client.create_voucher(merchant_pubkey=MERCHANT_PUBKEY, amount_microunit=1000)
        # Set timestamp to 50 seconds in the past
        voucher["timestamp"] = int(time.time()) - 50

        auth_header = f"X402 {base64.b64encode(json.dumps(voucher).encode()).decode()}"
        res = paywall.verify_payment(auth_header)
        self.assertFalse(res["valid"])
        self.assertIn("Stale Voucher Rejected", res["reason"])

    def test_fastapi_decorator_integration(self):
        app = FastAPI()

        @app.post("/test/mcp")
        @haichain_paywall(recipient=MERCHANT_PUBKEY, price_usdt=0.002, service_name="Test MCP API")
        async def mcp_endpoint(request: Request):
            payment = getattr(request.state, "haichain_payment", {})
            return {"status": "ok", "paid": payment.get("verified", False)}

        client = TestClient(app)

        # 1. No Authorization header -> 402 Payment Required
        resp_no_auth = client.post("/test/mcp")
        self.assertEqual(resp_no_auth.status_code, 402)
        self.assertEqual(resp_no_auth.headers.get("X-Payment-Required"), "true")
        self.assertIn("X402", resp_no_auth.headers.get("WWW-Authenticate", ""))
        self.assertEqual(resp_no_auth.json()["error"], "Payment Required")

        # 2. Valid Authorization header -> 200 OK
        agent_client = HaichainClient(pot_pubkey=POT_PUBKEY)
        auth_header = agent_client.build_auth_header(
            merchant_pubkey=MERCHANT_PUBKEY,
            amount_microunit=2000,
            channel_id=10
        )

        resp_valid = client.post("/test/mcp", headers={"Authorization": auth_header})
        self.assertEqual(resp_valid.status_code, 200)
        self.assertEqual(resp_valid.json()["status"], "ok")
        self.assertTrue(resp_valid.json()["paid"])

        # 3. Replay attack on FastAPI endpoint -> 402 Replay Attack Rejected
        resp_replay = client.post("/test/mcp", headers={"Authorization": auth_header})
        self.assertEqual(resp_replay.status_code, 402)
        self.assertIn("Replay Attack Rejected", resp_replay.json().get("verificationError", ""))

    def test_alias_package_haichain_agent_pay(self):
        import haichain_agent_pay
        self.assertTrue(hasattr(haichain_agent_pay, "haichain_paywall"))
        self.assertTrue(hasattr(haichain_agent_pay, "HaichainClient"))
        self.assertTrue(hasattr(haichain_agent_pay, "AgentResponse"))

    def test_call_paid_agent_flow(self):
        # Test auto-negotiation with unittest.mock
        from unittest.mock import patch, MagicMock
        import urllib.error
        import io

        calls = []

        def mock_urlopen(req, timeout=30.0):
            calls.append(req)
            auth = req.headers.get("Authorization") or req.headers.get("authorization")
            if not auth:
                # First call: return 402 challenge
                challenge_data = json.dumps({
                    "error": "Payment Required",
                    "recipient": MERCHANT_PUBKEY,
                    "price": 0.005,
                    "amount": 5000,
                    "service": "Test Agent API"
                }).encode("utf-8")
                headers = {
                    "Content-Type": "application/json",
                    "X-Payment-Required": "true",
                    "WWW-Authenticate": f'X402 recipient="{MERCHANT_PUBKEY}", amount="5000"'
                }
                fp = io.BytesIO(challenge_data)
                raise urllib.error.HTTPError(req.full_url, 402, "Payment Required", headers, fp)
            else:
                # Second call: voucher provided -> return 200 OK
                resp_mock = MagicMock()
                resp_mock.status = 200
                resp_mock.read.return_value = json.dumps({"result": "inference complete", "agent": "paid-agent"}).encode("utf-8")
                resp_mock.headers = {"Content-Type": "application/json"}
                resp_mock.__enter__.return_value = resp_mock
                return resp_mock

        with patch("urllib.request.urlopen", side_effect=mock_urlopen):
            client = HaichainClient(pot_pubkey=POT_PUBKEY, cluster="devnet")
            resp = client.call_paid_agent("http://127.0.0.1:8000/api/v1/inference", json={"prompt": "hello agent"})
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json()["result"], "inference complete")
            self.assertEqual(len(calls), 2)
            self.assertIn("X402", calls[1].headers.get("Authorization", ""))


if __name__ == "__main__":
    unittest.main()
