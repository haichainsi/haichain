import hashlib
import json

methods = [
    'initialize_agent_vault',
    'deposit_funds',
    'execute_master_payment',
    'trigger_emergency_panic',
    'reclaim_expired_nullifier',
    'advance_min_valid_nonce',
    'update_composite_root',
    'register_provider_bond',
    'report_and_slash_faulty_provider',
    'verify_dynamic_spot_ticket'
]

results = {}
for m in methods:
    h = hashlib.sha256(f'global:{m}'.encode('utf-8')).digest()[:8]
    results[m] = {
        'bytes': list(h),
        'hex': '0x' + h.hex()
    }

print(json.dumps(results, indent=2))
