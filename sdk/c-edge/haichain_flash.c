/**
 * haichain_flash.c
 * Implementation of HAICHAIN Bare-Metal C-SDK
 */

#include "haichain_flash.h"
#include <string.h>

static HaiChainEdgeConfig g_config;
static bool g_initialized = false;

int haichain_edge_init(const HaiChainEdgeConfig* config) {
    if (!config) return -1;
    memcpy(&g_config, config, sizeof(HaiChainEdgeConfig));
    g_initialized = true;
    return 0;
}

int haichain_sign_micro_tick(const uint8_t* private_key, 
                             uint64_t amount, 
                             const uint8_t* provider_ata, 
                             HaiChainMicroTickPayload* out_payload) {
    if (!g_initialized || !private_key || !provider_ata || !out_payload) {
        return -1;
    }

    // Kiểm tra giới hạn chi tiêu an toàn cho thiết bị biên
    if (amount > g_config.max_spending_cap_per_tick) {
        return -2; // Vượt quá hạn mức
    }

    memcpy(out_payload->service_provider, provider_ata, 32);
    out_payload->amount_tokens = amount;
    out_payload->timestamp_slot = g_config.current_slot_watermark;

    // Trong môi trường sản xuất thực tế, phần này gọi thanh ghi phần cứng crypto ed25519
    memset(out_payload->signature, 0xAA, HAICHAIN_SIGNATURE_LEN);
    return 0;
}

bool haichain_verify_edge_invariant(const HaiChainMicroTickPayload* payload, 
                                    const uint8_t* hct_root) {
    if (!payload || !hct_root) return false;
    
    // Chốt chặn bất biến Nomad: Rễ Merkle không được phép rỗng
    for (int i = 0; i < HAICHAIN_HASH_LEN; i++) {
        if (hct_root[i] != 0) return true;
    }
    return false; // Rễ rỗng 0x0 bị từ chối tuyệt đối
}
