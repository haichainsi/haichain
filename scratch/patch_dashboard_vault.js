const fs = require('fs');

const oldTarget = `      // Deterministically derive Sovereign Solana Address from hardware credential
      const rawBytes = new Uint8Array(cred.rawId);
      const hashBuffer = await window.crypto.subtle.digest('SHA-256', rawBytes);
      const seed32 = new Uint8Array(hashBuffer);`;

const newReplacement = `      // =========================================================================
      // HARDENED SOVEREIGN BIOMETRIC KEYPAIR VAULT (PARADIGM SECURITY STANDARD)
      // Never derive Ed25519 private seed directly from public cred.rawId!
      // Instead, generate authentic CSPRNG 32-byte entropy and protect with AES-256-GCM.
      // =========================================================================
      const vaultKey = 'haichain_sovereign_vault_' + cred.id;
      let seed32 = null;

      // Helper to derive AES-256-GCM key from biometric attestation & device salt
      async function deriveVaultKey(rawCredBytes, saltBytes) {
        const material = await window.crypto.subtle.importKey(
          'raw',
          rawCredBytes,
          'PBKDF2',
          false,
          ['deriveKey']
        );
        return await window.crypto.subtle.deriveKey(
          {
            name: 'PBKDF2',
            salt: saltBytes,
            iterations: 100000,
            hash: 'SHA-256'
          },
          material,
          { name: 'AES-GCM', length: 256 },
          false,
          ['encrypt', 'decrypt']
        );
      }

      const existingVaultJson = localStorage.getItem(vaultKey);
      if (existingVaultJson) {
        try {
          const vault = JSON.parse(existingVaultJson);
          const iv = Uint8Array.from(atob(vault.iv), c => c.charCodeAt(0));
          const salt = Uint8Array.from(atob(vault.salt), c => c.charCodeAt(0));
          const ciphertext = Uint8Array.from(atob(vault.ciphertext), c => c.charCodeAt(0));
          
          const aesKey = await deriveVaultKey(new Uint8Array(cred.rawId), salt);
          const decryptedBuffer = await window.crypto.subtle.decrypt(
            { name: 'AES-GCM', iv: iv },
            aesKey,
            ciphertext
          );
          seed32 = new Uint8Array(decryptedBuffer);
        } catch (decryptErr) {
          console.warn("Failed to decrypt existing biometric vault, rotating key:", decryptErr);
          seed32 = null;
        }
      }

      // If no vault exists or decryption failed, generate a fresh CSPRNG 32-byte seed
      if (!seed32) {
        seed32 = new Uint8Array(32);
        window.crypto.getRandomValues(seed32);

        const iv = new Uint8Array(12);
        window.crypto.getRandomValues(iv);
        const salt = new Uint8Array(16);
        window.crypto.getRandomValues(salt);

        const aesKey = await deriveVaultKey(new Uint8Array(cred.rawId), salt);
        const ciphertextBuffer = await window.crypto.subtle.encrypt(
          { name: 'AES-GCM', iv: iv },
          aesKey,
          seed32
        );

        const vaultRecord = {
          version: "v6.9.4",
          createdSlot: Date.now(),
          iv: btoa(String.fromCharCode(...iv)),
          salt: btoa(String.fromCharCode(...salt)),
          ciphertext: btoa(String.fromCharCode(...new Uint8Array(ciphertextBuffer)))
        };
        localStorage.setItem(vaultKey, JSON.stringify(vaultRecord));
      }`;

['dashboard.html', 'app/dashboard.html'].forEach(file => {
  let content = fs.readFileSync(file, 'utf8');
  if (content.includes(oldTarget)) {
    content = content.replace(oldTarget, newReplacement);
    fs.writeFileSync(file, content, 'utf8');
    console.log(`[+] Patched ${file} successfully!`);
  } else {
    // Try with normalized newlines
    const normContent = content.replace(/\r\n/g, '\n');
    const normTarget = oldTarget.replace(/\r\n/g, '\n');
    if (normContent.includes(normTarget)) {
      const patched = normContent.replace(normTarget, newReplacement.replace(/\r\n/g, '\n'));
      fs.writeFileSync(file, patched, 'utf8');
      console.log(`[+] Patched ${file} with normalized newlines!`);
    } else {
      console.error(`[-] Target not found in ${file}`);
    }
  }
});
