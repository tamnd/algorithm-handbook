## What to remember

- For a random function with $n$-bit output, a preimage or a second preimage costs about $2^n$ calls and a collision about $2^{n/2}$. After $q$ calls the chance of a collision is at most $q(q-1)/2^{n+1}$, and half the time a collision has appeared by about $1.18 \cdot 2^{n/2}$ calls.
- Collision resistance implies second-preimage resistance. Second-preimage resistance implies preimage resistance only for a hash that compresses: $\mathrm{Adv}^{\mathrm{pre}} \le 2\,\mathrm{Adv}^{\mathrm{sec}} + 2^{n-m}$ for $m$-bit messages (Rogaway and Shrimpton). The other directions fail.
- The [birthday attack](/birthday-attack/) stores about $2^{n/2}$ values; [Pollard's rho](/pollard-rho-collision-search/) needs constant memory. In the quantum query model, the Brassard-Høyer-Tapp algorithm finds collisions in about $2^{n/3}$ queries with $2^{n/3}$ quantum memory, and Grover search finds preimages in about $2^{n/2}$.
- The [Merkle-Damgård theorem](/merkle-damgard-theorem/) is a tight reduction in the standard model: with length padding, a collision of the hash gives a collision of the compression function. It keeps no other generic level: [length extension](/length-extension-attack/) breaks the MAC $H(K \| m)$, Joux finds $2^t$ colliding messages in about $t \cdot 2^{n/2}$ calls, and a target of $2^k$ blocks has a second preimage in about $k \cdot 2^{n/2+1} + 2^{n-k+1}$.
- In the ideal cipher model, [Davies-Meyer](/davies-meyer-construction/) $f(h, m) = E_m(h) \oplus h$ needs about $2^{n/2}$ queries for a collision, with the bound $q(q+1)/2^n$ (Black, Rogaway and Shrimpton). Every block has the fixed point $E_m^{-1}(0^n)$.
- A [sponge](/sponge-construction/) with capacity $c$ over a random permutation is indifferentiable from a random oracle up to about $2^{c/2}$ calls. A $d$-bit output gives collisions at about $\min(2^{d/2}, 2^{c/2})$ and preimages at about $\min(2^d, 2^{c/2})$; SHA3-256 has $c = 512$ and SHAKE128 has $c = 256$.
- [HMAC](/hmac/) is $H((K' \oplus \mathrm{opad}) \,\|\, H((K' \oplus \mathrm{ipad}) \,\|\, m))$. In the standard model it is a PRF if the compression function is a PRF, with a related-key condition for the two derived keys (Bellare 2006); collision resistance of $H$ is not needed.
- A random salt per password defeats precomputation, such as Hellman's tradeoff $T M^2 = N^2$ and rainbow tables. An iteration count $c$ adds only $\log_2 c$ bits, and memory hardness makes each guess cost memory as well as time.

| Function | Construction | Digest bits | Generic collision / preimage | Best known collision result | Length extension |
|---|---|---|---|---|---|
| MD5 | Merkle-Damgård | 128 | $2^{64}$ / $2^{128}$ | practical (Wang and Yu 2005); chosen-prefix (2007) | yes |
| SHA-1 | Merkle-Damgård | 160 | $2^{80}$ / $2^{160}$ | $2^{63.1}$ (2017); chosen-prefix $2^{63.4}$ (2020) | yes |
| RIPEMD-160 | Merkle-Damgård, two lines | 160 | $2^{80}$ / $2^{160}$ | reduced steps only | yes |
| SHA-256 | Merkle-Damgård | 256 | $2^{128}$ / $2^{256}$ | 31 of 64 steps | yes |
| SHA-512/256 | Merkle-Damgård, 512-bit state cut to 256 | 256 | $2^{128}$ / $2^{256}$ | 31 of 80 steps of SHA-512 | no |
| SHA3-256 | sponge, $c = 512$ | 256 | $2^{128}$ / $2^{256}$ | 5 of 24 rounds | no |
| SHAKE128 | sponge, $c = 256$ | any $d$ | $\min(2^{d/2}, 2^{128})$ / $\min(2^d, 2^{128})$ | same permutation as SHA3-256 | no |
| BLAKE2b | HAIFA iteration | up to 512 | $2^{256}$ / $2^{512}$ at 512 bits | reduced rounds only | no |

: Named hash functions. Generic costs are for an ideal function of the same size and capacity. No collision of the full SHA-2, SHA-3 or BLAKE2 is known; their security is a conjecture backed by cryptanalysis, not a proof.

## Choosing a hash function

For a plain hash, use SHA-256, or SHA-512/256 on 64-bit machines. Use SHA3-256 where a design unlike SHA-2 is wanted or where length extension must be ruled out by construction. BLAKE2 and BLAKE3 are faster in software but are not FIPS functions. A 160-bit digest gives only 80-bit collision resistance.

Do not use MD5 or SHA-1 where an attacker can influence the input, as in signatures, certificates and content addressing.

For a MAC, use HMAC with SHA-256, [KMAC](/kmac/), or keyed BLAKE2. Never use $H(K \| m)$ with a Merkle-Damgård hash. When you need output of any length, use an [extendable-output function](/extendable-output-function/) such as SHAKE256, and separate its uses by domain: a shorter output is a prefix of a longer one.

For passwords, never use a plain fast hash. Use [Argon2id](/argon2/), the recommendation of RFC 9106, with a random salt per password; use scrypt where Argon2id is not available, bcrypt in legacy systems, and [PBKDF2](/pbkdf2/) with a high iteration count where FIPS 140 compliance is required. For a hash table with keys an attacker chooses, use [SipHash](/siphash/) with a secret key, not [xxHash](/xxhash/).
