## What to remember

- **The threat is to public-key cryptography.** Shor's algorithm breaks RSA, Diffie-Hellman and elliptic curves in polynomial time. Grover search needs $\frac{\pi}{4}2^{k/2}$ serial steps on a $k$-bit key; with circuit depth limited to MAXDEPTH it costs $(\frac{\pi}{4})^2 d g \cdot 2^k/\text{MAXDEPTH}$ gates, so AES-128 still meets NIST category 1.
- **Data is at risk before the computer exists.** If data must stay secret for $x$ years, migration takes $y$ years and a quantum computer is $z$ years away, [Mosca's inequality](/harvest-now-decrypt-later/) $x + y > z$ says recorded traffic will be read. Key exchange moves first; signatures are not exposed to this threat.
- **LWE and SIS carry the lattice family.** Regev's reduction from worst-case GapSVP and SIVP within $\tilde O(n/\alpha)$ to LWE, for $\alpha q > 2\sqrt n$, is quantum; the classical ones need an exponential $q$ or a smaller dimension. The reduction for SIS is classical. Ring and module forms have their own reductions, for ideal and module lattices; no reduction from LWE to Ring-LWE is known.
- **Parameters come from attacks.** Core-SVP charges one SVP call in the BKZ block size $b$: $2^{0.292b}$ classically and $2^{0.265b}$ quantumly, 118 and 107 bits for Kyber512. Arora-Ge solves LWE with error width $n^\varepsilon$ in time $2^{\tilde O(n^{2\varepsilon})}$; BKW solves LPN in $2^{O(n/\log n)}$.
- **The two lattice standards.** ML-KEM is IND-CCA2 under decision Module-LWE in the ROM and the QROM, with $q = 3329$ and $n = 256$. ML-DSA is Fiat-Shamir with aborts, secure in the QROM under Module-LWE, Module-SIS and SelfTargetMSIS; its loop runs 3.85 to 5.1 times on average. Falcon is hash-and-sign over NTRU lattices and is safe only because its preimages follow a Gaussian that does not depend on the secret basis.
- **Code-based security is about decoding.** Prange's algorithm needs $\binom{n}{w}/\binom{n-k}{w}$ rounds on average. At full Gilbert-Varshamov distance the best exponents fall only from 0.1207 (Prange) to 0.0966 (May-Ozerov), and a quantum computer roughly halves them.
- **Breaks were classical and sudden.** Rainbow fell to Beullens in 2022 (a level-1 key in about 53 hours on a laptop), SIKE to Castryck and Decru in 2022 (SIKEp434 in about ten minutes on one core), HFE and GeMSS to algebraic attacks. UOV with $v \ge 2o$ and CSIDH are unbroken.

## The families side by side

| Family | Example | Assumption | Public key | Ciphertext or signature | Category | Status |
|---|---|---|---|---|---|---|
| Lattice | [ML-KEM-768](/crystals-kyber/) | Module-LWE | 1184 | 1088 | 3 | FIPS 203 |
| Lattice | [FrodoKEM-640](/frodokem/) | LWE | 9616 | 9720 | 1 | alternate, not selected |
| Lattice | [ntruhps2048509](/ntru-encrypt/) | NTRU | 699 | 699 | 1 | finalist, not selected |
| Lattice | [ML-DSA-65](/crystals-dilithium/) | Module-LWE, Module-SIS | 1952 | 3309 | 3 | FIPS 204 |
| Lattice | [Falcon-512](/falcon/) | NTRU, SIS over NTRU lattices | 897 | 666 | 1 | planned as FIPS 206 |
| Code | mceliece348864 | syndrome decoding, Goppa codes | 261120 | 96 | 1 | round 4, under ISO consideration |
| Code | [BIKE](/bike/) L1 | quasi-cyclic syndrome decoding | 1541 | 1573 | 1 | round 4, not selected |
| Code | hqc-128 | quasi-cyclic syndrome decoding | 2249 | 4497 | 1 | selected in 2025 |
| Hash | [SLH-DSA-128s](/sphincs-plus/) | hash function properties | 32 | 7856 | 1 | FIPS 205 |
| Multivariate | [UOV](/unbalanced-oil-and-vinegar/) | MQ, hidden oil space | over 200 KB | 96 | 1 | round 3, extra call |
| Multivariate | [Rainbow](/rainbow-signature/) | MQ, layered oil space | | | | broken (2022) |
| Isogeny | [SIKEp434](/sidh/) | SIDH with torsion images | 330 | 346 | 1 | broken (2022) |
| Isogeny | [CSIDH-512](/csidh/) | class group action | 64 | (key exchange) | | unbroken, not submitted |

: Sizes in bytes. "Alternate" and "finalist" refer to round 3 of the NIST process; UOV is in round 3 of the later call for additional signatures, and its public key is the expanded form. Subexponential quantum attacks put CSIDH-512 below category 1.

## Choosing a scheme

Use the standards and their named parameter sets. Every parameter set small enough to work by hand is a toy.

- For key exchange, use ML-KEM-768 in a [hybrid](/hybrid-key-exchange/) with X25519, as TLS and OpenSSH now do. The key stays secret if either part holds, and [crypto agility](/crypto-agility/) lets you swap parts later.
- For a KEM that does not rest on structured lattices, choose HQC, selected as a backup to ML-KEM, or FrodoKEM, which some European agencies recommend. Classic McEliece suits long-lived static keys when a key of hundreds of kilobytes is acceptable.
- For signatures, use ML-DSA by default. Falcon has the smallest lattice signatures, but its signer needs exact 53-bit floating point arithmetic. SLH-DSA rests only on hash functions, at the price of signatures of 7.8 to 50 kilobytes and slow signing.
- Do not use broken schemes: knapsack schemes, NTRUSign, HFE and GeMSS, Rainbow, and SIDH or SIKE.
