# RAPPORT DE DILIGENCE RAISONNABLE DES RISQUES INSTITUTIONNELS HAICHAIN
## Preuves Mathématiques, Modélisation des Menaces et Matrice de Vérification Red-Team
**Destinataires :** Fonds de Capital-Risque Tier-1 (a16z crypto, Paradigm, Sequoia), Dépositaires Institutionnels et Cabinets d'Audit de Premier Rang (OtterSec, Neodyme, Kudelski Security)  
**Version du Protocole :** HAICHAIN Kernel v1.1 / CapLeaf v1 (Schéma Wire 223 Octets)  
**Norme Technique :** Anchor Framework (Solana L1) + Sui Move (`AgentCap`) + Solveur d'Intention Tron Rail

---

## 1. RÉSUMÉ EXÉCUTIF ET PARADIGME DE SÉCURITÉ

Les agents d'IA autonomes exécutant des micro-transactions financières introduisent des surfaces d'attaque fondamentalement différentes de la DeFi humaine :
1. **Zéro Latence Humaine :** Un agent IA exécutant des appels d'outils peut être manipulé par Injection Indirecte de Prompt pour émettre des milliers de bons de paiement illégitimes en quelques secondes.
2. **Vulnérabilité d'Exfiltration de Clés :** L'exécution d'instances d'agents sur des nœuds distribués (Cloudflare Workers, MCP locaux, serverless) accroît considérablement le risque d'exfiltration des clés privées.
3. **Prolifération de Commerçants Sybil :** Dans un réseau M2M ouvert, des commerçants malveillants peuvent enregistrer une infinité de domaines jetables pour contourner les limitations de débit.

Pour résoudre ce défi sans compromettre la rapidité à la milliseconde, **HAICHAIN dissocie entièrement l'exécution financière de la garde des fonds** :
- **Autorité Souveraine Suprême :** La Passkey biométrique matérielle WebAuthn FIDO2 (P-256) conserve 100 % de la propriété inaliénable du coffre.
- **Autorité Isolée des Sous-Agents :** Les paires de clés Ed25519 éphémères sont strictement confinées dans un Moteur de Règles (Policy Engine) hors-processus sans accès à la phrase secrète du portefeuille maître.
- **Ancrage Merkle On-Chain :** Le schéma de feuille de 223 octets applique 9 invariants mathématiques inaltérables ($I_1 \dots I_9$).

---

## 2. MODÈLE FORMEL DE MENACES ET FORMULES DE LIMITE DE PERTE

### 2.1. Taxonomie de la Surface d'Attaque

| Classe de Menace | Scénario d'Attaque | Risque Web3 Conventionnel | Plafond Pire Cas HAICHAIN |
| :--- | :--- | :--- | :--- |
| **$T_1$ (Injection Indirecte)** | LLM forcé à payer un marchand non approuvé | Portefeuille vidé ($100 000+) | **$E_{\text{theft}} = 0$** (Bloqué par la whitelist Merkle) |
| **$T_2$ (Collusion Marchande)** | Marchand légitime tentant une double réclamation | Double prélèvement de compte | **$E_{\text{theft}} = 0$** (Contrainte Anchor $P_i \le \min(C_i, R_i)$) |
| **$T_3$ (Attaque Domaine Probation)** | Sous-agent tentant de vider les fonds sur une nouvelle API | Épuisement cumulatif du coffre | **$E_{\text{theft}} \le M_{\text{tpl}}$** (Plafonné au budget du modèle parent) |
| **$T_4$ (Compromission Totale)** | Clé privée compromise + marchand complice | Coffre entièrement vidé sur-le-champ | **$E_{\text{theft}}(\tau) \le \min(B, K, W_p \cdot n(\tau, \omega_p))$** |

---

### 2.2. Théorème 6.1 : Borne Supérieure du Vol dans le Pire des Cas ($T_4$)

Soit $\tau$ le temps de réponse total du protocole entre l'émission d'une transaction illicite et l'inscription sur la blockchain du gel d'urgence (Panic Freeze) :
$$\tau = t_{\text{detect}} + t_{\text{owner}} + t_{\text{land}}$$
où :
- $t_{\text{detect}} \le 5,0\text{s}$ (seuil de détection des anomalies télémétriques)
- $t_{\text{owner}} \le 2,0\text{s}$ (confirmation biométrique Passkey en 1 clic)
- $t_{\text{land}} \le 5,0\text{s}$ (confirmation haute priorité sur Solana L1)

Même dans l'éventualité la plus grave de compromission intégrale de la clé Ed25519 de l'agent et de collusion active avec un marchand validé dans l'arbre de Merkle, le vol cumulé maximal $E_{\text{theft}}(\tau)$ est strictement borné par :

$$E_{\text{theft}}(\tau) \le \min\left(B,\; K,\; W_p \cdot n(\tau, \omega_p),\; \sum_{i:\, m_i \in \mathcal{A}} E_i(\tau)\right)$$

Où :
- $B$ : Solde total du coffre (`pot.balance`).
- $K$ : Plafond cumulé de la feuille active (`leaf.max_spend`).
- $W_p$ : Vélocité maximale par fenêtre glissante (`leaf.window_cap`).
- $\omega_p$ : Durée de la fenêtre (typiquement $3\,600\text{s}$ = 1 heure).
- $n(\tau, \omega_p) = \lceil \tau / \omega_p \rceil$ : Nombre de fenêtres traversées pendant $\tau$. Pour $\tau = 12\text{s} \ll 3600\text{s}$, $n = 1$.
- $\sum E_i$ : Somme des montants mis sous séquestre pour les marchands complices.

**Corollaire :** Pour un coffre institutionnel doté de $10\,000\text{ USDT}$, avec un budget par feuille de $50\text{ USDT}$ et une limite de vélocité de $10\text{ USDT / heure}$, un pirate s'emparant de la clé de l'agent **ne pourra en aucun cas dérober plus de $10\text{ USDT}$** avant le gel complet, préservant ainsi **$9\,990\text{ USDT}$ (99,9 %)** des capitaux.

---

## 3. PÉNÉTRATION RED-TEAM ET MATRICE DE RENFORCEMENT

Cinq vecteurs d'attaque critiques ont été rigoureusement testés et verrouillés dans le noyau :

```
+---------------------------------------------------------------------------------------------------+
|                                 HAICHAIN MATRICE DE RENFORCEMENT EN 5 POINTS                       |
+---+----------------------------+----------------------------------+-------------------------------+
| # | Vecteur d'Attaque          | Mécanisme de Vulnérabilité       | Invariant On-Chain Renforcé   |
+---+----------------------------+----------------------------------+-------------------------------+
| 1 | Double Réclamation Escrow  | Soumission de multiples reçus    | Règlement Monotone Non-Réversible: |
|   |                            | pour dépasser la réserve         | P_i <= min(C_i, R_i)          |
+---+----------------------------+----------------------------------+-------------------------------+
| 2 | Détournement Compte ATA    | Redirection du compte receveur   | Liaison Stricte ATA Canonique |
|   |                            | vers un tiers non approuvé       | Validation rigide sur Solana L1|
+---+----------------------------+----------------------------------+-------------------------------+
| 3 | Contournement Gel Panic    | Les anciens canaux réclament     | Isolation d'Époque Instantanée|
|   |                            | après activation du Panic Freeze | Invalidation immédiate ($I_6$) |
+---+----------------------------+----------------------------------+-------------------------------+
| 4 | Drainage Lamport Loyer     | Vol des lamports lors de la      | Restitution Canonique du Loyer|
|   |                            | fermeture d'un canal             | Retour automatique à grant_pot|
+---+----------------------------+----------------------------------+-------------------------------+
| 5 | Attaque Sybil Micro-Boucle | Création de 1 000 sous-feuilles  | Brûlage du Budget Modèle      |
|   |                            | pour drainer des micro-réserves  | activate_child déduit du père |
+---+----------------------------+----------------------------------+-------------------------------+
```

---

## 4. RAPPORT D'AUDIT DES 9 INVARIANTS MATHÉMATIQUES ($I_1 \dots I_9$)

Toutes les instructions de `programs/haichain-core/src/lib.rs` respectent scrupuleusement les 9 invariants mathématiques :
1. **$I_1$ (Conservation du Capital) :** Solde ATA + Escrows + Paiements + Remboursements $\equiv$ Dépôts Nets.
2. **$I_2$ (Sécurité du Bénéficiaire Canonique) :** Adresse ATA rigoureusement vérifiée sur Solana L1.
3. **$I_3$ (Plafond Budgétaire Inviolable) :** Consommation toujours inférieure ou égale au budget alloué.
4. **$I_4$ (Limitation de Vélocité Autonome) :** Dépenses strictement plafonnées par fenêtre glissante.
5. **$I_5$ (Rétrécissement Monotone PDA) :** Les sous-instances ne peuvent jamais élargir leurs droits.
6. **$I_6$ (Isolation d'Époque et Gel Immédiat) :** Désactivation instantanée de tous les bons en circulation.
7. **$I_7$ (Expiration de Session Heartbeat) :** Arrêt des réservations dès expiration du délai.
8. **$I_8$ (Règlement Unique et Monotone) :** Aucune possibilité de double dépense.
9. **$I_9$ (Isolation de Compte Anti-Sybil) :** Relation 1:1 stricte entre feuille et compte PDA.

---

## 5. MODÈLE ÉCONOMIQUE ET CONFORMITÉ RÉGLEMENTAIRE

### 5.1. Standard d'Utilité Pure Sans Dividende (Immunité Howey & MiCA)
- **Zéro Rendement Passif ni Staking :** Élimination totale de toute promesse de profit dépendant d'efforts tiers.
- **50 % Rachat & Destruction (Buyback & Burn) :** 50 % des frais de protocole sont utilisés pour racheter des $HAISI sur le marché libre et les brûler définitivement.
- **50 % Fonds de Réserve (CHGB) :** 50 % des frais alimentent une réserve de sécurité décentralisée.

### 5.2. Règlement Multi-Chaînes
- **Solana L1 Anchor Kernel :** Finalité en 400 ms avec schéma 223 octets.
- **Sui Move Linear Object Model (`AgentCap`) :** Capacités linéaires sans primitives `copy` ou `drop`.
- **Tron TRC20 Rail Solver :** Règlements à coût quasi-nul pour les marchés émergents.

---

## 6. RECOMMANDATIONS D'AUDIT EXTERNE ET DATA ROOM

Documents d'audit disponibles :
- `/programs/haichain-core/src/lib.rs` (Anchor Rust Kernel v1.1)
- `/programs/haichain-sui/sources/capleaf.move` (Module Sui Move)
- `/sdk/typescript/src/capleaf.ts` (Schéma 223 Octets et Arbre de Merkle)
- `/sdk/typescript/src/policy-engine.ts` (Bac à sable d'isolation à divulgation nulle)
- `/tests/` (72 tests automatisés de fuzzing et d'invariants réussis)

**Conclusion :** HAICHAIN v1.1 fournit la première couche de paiement mathématiquement prouvée et isolée matériellement pour agents IA, établissant la référence de sécurité institutionnelle.
