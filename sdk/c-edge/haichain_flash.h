/**
 * haichain_flash.h
 * HAICHAIN Zero-RTT Bare-Metal C-SDK for Robotics & IoT Edge Devices
 * Target: ANSI C99, RAM < 200KB, ed25519 hardware accelerator support
 */

#ifndef HAICHAIN_FLASH_H
#define HAICHAIN_FLASH_H

#include <stdint.h>
#include <stdbool.h>

#define HAICHAIN_MAX_PROOF_DEPTH 16
#define HAICHAIN_HASH_LEN 32
#define HAICHAIN_SIGNATURE_LEN 64

typedef struct {
    uint8_t master_owner[32];
    uint8_t dedicated_vault_pda[32];
    uint64_t max_spending_cap_per_tick;
    uint64_t current_slot_watermark;
} HaiChainEdgeConfig;

typedef struct {
    uint8_t service_provider[32];
    uint64_t amount_tokens;
    uint64_t timestamp_slot;
    uint8_t leaf_capability[HAICHAIN_HASH_LEN];
    uint8_t merkle_proof[HAICHAIN_MAX_PROOF_DEPTH][HAICHAIN_HASH_LEN];
    uint8_t proof_depth;
    uint8_t signature[HAICHAIN_SIGNATURE_LEN];
} HaiChainMicroTickPayload;

// API Signatures
int haichain_edge_init(const HaiChainEdgeConfig* config);
int haichain_sign_micro_tick(const uint8_t* private_key, 
                             uint64_t amount, 
                             const uint8_t* provider_ata, 
                             HaiChainMicroTickPayload* out_payload);
bool haichain_verify_edge_invariant(const HaiChainMicroTickPayload* payload, 
                                    const uint8_t* hct_root);

#endif // HAICHAIN_FLASH_H
