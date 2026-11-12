## What to remember

- The standard goal is **EUF-CMA**: given the public key and signatures on messages of its choice, the adversary cannot sign a new message. [SUF-CMA](/strong-unforgeability/) also forbids a new signature on a signed message. Unique signatures (RSA with a range check, BLS) get it for free; ECDSA does not have it, since $(r, n - s)$ also verifies.
- A security claim names the adversary, the notion, the assumption and the model. [RSA-FDH](/rsa-fdh/), [RSA-PSS](/rsa-pss/), [Schnorr](/schnorr-signature/), [Ed25519](/ed25519/) and [BLS](/bls-signature/) are proved in the [random oracle model](/random-oracle-model/). [DSA](/dsa/) has no proof from discrete log alone, and [ECDSA](/ecdsa/) only in the generic group model or with an idealized conversion function.
- **Tightness counts.** RSA-FDH loses about $\mathrm{e} \cdot q_s$ (Coron), and no proof can do much better for unique signatures. PSS is tight. The [forking lemma](/forking-lemma/) proof of Schnorr turns a forger with success $\varepsilon$ into a discrete log solver with success about $\varepsilon^2/q_h$, and Seurin showed that algebraic reductions cannot avoid the loss if one-more discrete log is hard.
- **Hash-and-sign** signs $H(m)$, so a collision of $H$ moves a signature to a second message. MD5 collisions gave a rogue CA certificate in 2008.
- **The nonce is the weak spot** of ElGamal, DSA, ECDSA and Schnorr. One repeated nonce gives the key by two divisions; a few leaked binary digits of many nonces give it by a lattice attack. [RFC 6979](/deterministic-nonce-generation/) and EdDSA derive the nonce from the key and the message; hedged signers add fresh randomness against faults.
- **Linearity** of Schnorr and BLS gives [batch verification](/batch-verification/), [aggregation](/aggregate-signature/), [MuSig](/musig/) and [threshold signatures](/threshold-signature/). A naive sum of keys falls to a rogue key; MuSig coefficients or proofs of possession stop it.
- **Hash-based signatures** need only properties of a hash function, and the known quantum attacks only take a square root off their cost. A Merkle tree certifies $2^h$ one-time keys. [LMS](/leighton-micali-signature/) and [XMSS](/xmss/) must never reuse a leaf, and [SLH-DSA](/sphincs-plus/) pays for having no state with signatures of 7,856 to 49,856 bytes.

## The main schemes side by side

| Scheme | Assumption | Notion | Model | Signing | Signature size |
|---|---|---|---|---|---|
| [RSA PKCS #1 v1.5](/rsa-signature/) | RSA-type | EUF-CMA (2018 proof) | ROM | deterministic, unique | 256 bytes (2048-bit $N$) |
| RSA-PSS | RSA | EUF-CMA, tight | ROM | randomized | 256 bytes (2048-bit $N$) |
| DSA | discrete log | no proof from DL alone | — | randomized or RFC 6979 | 64 bytes at (2048, 256) |
| ECDSA | EC discrete log | EUF-CMA, not SUF | generic group, or idealized $x(\cdot) \bmod n$ | randomized or RFC 6979 | 64 bytes raw (P-256) |
| Schnorr, BIP 340 | discrete log | EUF-CMA (loose), strongly unforgeable | ROM | nonce from key, message and fresh bytes | 64 bytes |
| Ed25519 | discrete log | SUF-CMA with the check $S < L$ | ROM | deterministic | 64 bytes |
| BLS | CDH (co-CDH) | EUF-CMA, unique so SUF | ROM | deterministic, unique | 48 bytes (BLS12-381) |
| [Lamport](/lamport-signature/), $n = 256$ | one-way, collision-resistant hash | EUF-1-CMA | standard | deterministic, one-time | 8,192 bytes |
| XMSS, $h = 10$ | second preimage resistance, PRF | EUF-CMA | standard for the tree hashes | stateful | 2,500 bytes |
| SLH-DSA-128s | multi-target hash properties | EUF-CMA, up to $2^{64}$ signatures | see caption | stateless | 7,856 bytes |

: The main signature schemes as their entries give them. "Unique" means one valid signature per key and message. The PKCS #1 v1.5 proof is by Jager, Kakvi and May, with conditions that their paper states. The SLH-DSA proof needs properties of its tweakable hashes, not collision resistance. All the reductions are classical; Shor's algorithm breaks the RSA, discrete log and pairing assumptions.

## Choosing a method

For a new design with no outside constraint, use Ed25519: short keys and no nonce to get wrong. Use ECDSA on P-256 or secp256k1 when a standard or a peer requires it, with RFC 6979 or hedged nonces, and with the low-s rule where signature bytes act as an identifier. Use RSA-PSS when RSA is required; RFC 8017 requires PSS for new applications and keeps PKCS #1 v1.5 for compatibility. Use BLS to shrink many signatures into one, and MuSig2 or FROST when several parties make one Schnorr signature.

Against a future quantum computer, the conservative choice is hash-based: LMS or XMSS where a hardware module keeps the counter safe, as in firmware signing, and SLH-DSA where state cannot be trusted. In every case, use a maintained library such as libsodium, libsecp256k1 or a FIPS 140 validated module; the code in the entries is for study only.
