## What to remember

- [Perfect secrecy](/perfect-secrecy/) against an unbounded passive adversary needs $|\mathcal{K}| \ge |\mathcal{M}|$ and $H(K) \ge H(M)$, by [Shannon's theorem](/shannon-perfect-secrecy-theorem/), so the [one-time pad](/one-time-pad/) is optimal, for one message per key. Practical ciphers aim at IND-CPA in the standard model, and a stateless deterministic scheme is never IND-CPA: one oracle query tells $m_0$ from $m_1$.
- A $k$-bit key falls to [exhaustive key search](/exhaustive-key-search/) in $2^k$ trials, $(2^k + 1)/2$ on average, and $\lceil k/n \rceil + 1$ known pairs fix the key. Grover search cuts this to about $2^{k/2}$ quantum evaluations. Double encryption falls to meet-in-the-middle in about $2 \cdot 2^k$ time and $2^k$ memory, which is why [Triple DES](/triple-des/) uses three stages.
- The [switching lemma](/prp-prf-switching-lemma/) costs $q(q-1)/2^{n+1}$, and the modes inherit a birthday term of order $\sigma^2/2^n$ for $\sigma$ blocks. With $n = 64$ that is about $2^{32}$ blocks per key, the Sweet32 limit; with $n = 128$ it is far away.
- By the [Luby-Rackoff theorem](/luby-rackoff-theorem/), a Feistel network with independent PRF rounds on $h$-bit halves is a PRP after 3 rounds and a strong PRP after 4, with a loss of order $q^2/2^h$. Two rounds are not a PRP, and 3 rounds are not a strong PRP.
- An [S-box](/s-box/) is judged by its DDT and LAT. The AES S-box has differential uniformity 4 and nonlinearity 112; the MixColumns branch number 5 forces at least 25 active S-boxes in any 4-round trail, so a differential trail over 4 rounds has probability at most $(2^{-6})^{25} = 2^{-150}$.
- IND-CPA plus INT-CTXT implies IND-CCA (Bellare and Namprempre), and encrypt-then-MAC with a strongly unforgeable MAC gives both. Encryption alone is malleable: a CTR bit flip passes straight through.
- A repeated nonce under one key turns [CTR](/ctr-mode/), [OFB](/ofb-mode/) and stream ciphers into a two-time pad, gives the GHASH key $H$ in [GCM](/gcm-mode/), and reveals $r$ and $s$ of a [Poly1305](/poly1305/) key. Random 96-bit nonces collide with probability at most $q(q-1)/2^{97}$.
- DES fell to key search in 1998; its best analytic attacks need $2^{47}$ chosen or $2^{43}$ known plaintexts. The biclique attack on full AES-128 costs $2^{126.1}$, a small factor below search.

## Modes side by side

| Mode | Secrecy (adversary model) | Integrity | Extra input | Padding | Parallel encryption |
|---|---|---|---|---|---|
| [ECB](/ecb-mode/) | none: deterministic, not IND-CPA | no | none | yes | yes |
| [CBC](/cbc-mode/) | IND-CPA up to about $\sigma^2/2^n$ | no | random, unpredictable IV | yes | no (decryption yes) |
| [CFB](/cfb-mode/) | IND-CPA (real-or-random) | no | unpredictable IV | no | no (decryption yes) |
| [OFB](/ofb-mode/) | IND-CPA if keystreams do not overlap | no | unique IV | no | no (keystream precomputable) |
| [CTR](/ctr-mode/) | IND-CPA up to about $\sigma^2/2^n$ | no | distinct counter blocks | no | yes |
| [XTS](/xts-mode/) | deterministic per sector and position | no | sector number as tweak | no (ciphertext stealing) | yes |
| [GCM](/gcm-mode/) | nonce-based AEAD, nonce-respecting, AES a PRP | yes | unique IV, 96 bits usual | no | yes |
| [CCM](/ccm-mode/) | nonce-based AEAD, nonce-respecting, $E$ a PRP | yes | unique nonce | no | no (CBC-MAC is serial) |
| [OCB3](/ocb-mode/) | nonce-based AEAD, $E$ a strong PRP | yes | unique nonce | no | yes |
| [ChaCha20-Poly1305](/chacha20-poly1305/) | IND-CPA and INT-CTXT, ChaCha20 block a PRF | yes | unique 96-bit nonce | no | yes |

: Modes of operation and AEAD schemes. $\sigma$ counts blocks under one key and $n$ is the block length. All bounds are in the standard model.

## Choosing a method

For new work, use an AEAD scheme and nothing less. Take AES-GCM where the processor has AES instructions and ChaCha20-Poly1305 where it does not; both are in TLS 1.3. Give every message a unique nonce, from a counter if you can. If nonces may be random, keep the number of messages per key well under the birthday bound of the nonce length: SP 800-38D allows $2^{32}$ messages for random 96-bit IVs in GCM.

Use [CCM](/ccm-mode/) where a standard requires it, as WPA2 does, and [EAX](/eax-mode/) or [OCB3](/ocb-mode/) when you need an on-line or one-pass mode. On very small hardware, use [Ascon](/ascon/), the NIST choice for [lightweight cryptography](/lightweight-cryptography/).

Encrypt disks with [XTS](/xts-mode/), knowing that it gives no integrity and reveals which blocks changed between two snapshots. Use [CMAC](/cmac/) or [HMAC](/hmac/) when you need a MAC alone, and never plain [CBC-MAC](/cbc-mac/) on messages of varying length.

Avoid ECB, RC4, A5/1, single DES and 64-bit block ciphers such as Triple DES, Blowfish and IDEA for new data. Choose AES-256 for data that must stay secret for decades, since quantum key search would halve the effective key length.
