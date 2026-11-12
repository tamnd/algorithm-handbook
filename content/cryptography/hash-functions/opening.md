A cryptographic hash function maps a message of any length to a short digest, such as 256 bits, and it must do this so that nobody can find two messages with the same digest or a message with a given digest. Unlike the hash function of a hash table, it has an adversary in mind. A signature scheme signs the digest of a document, not the document, so a collision would let one signature cover two documents. Git and Certificate Transparency name data by its digest, Bitcoin addresses are digests of keys, and a server stores a slow, salted hash of each password rather than the password. When MD5 and SHA-1 lost collision resistance, attackers forged a certificate authority, a Microsoft code-signing chain and PGP keys.

The chapter treats hash functions as a cryptographer does. Each security claim names its model. Collision, preimage and second-preimage resistance are games against an efficient adversary, and the costs $2^{n/2}$ and $2^n$ are what a random function of $n$ output bits allows. Some results are proofs in the standard model, such as the reduction from the hash to its compression function. Some hold only in an idealized model: the random oracle model, the ideal cipher model, or the ideal permutation model behind the sponge. For the named functions, security is a conjecture backed by years of cryptanalysis, and the entries say which attacks reach how many rounds.

## What the chapter covers

The chapter is in ten groups, read in order.

1. **What a hash function must do.** The [three properties](/cryptographic-hash-function/), how they imply one another, and the [random oracle model](/random-oracle-model/) in which many protocols are proved.
2. **Generic attacks.** The [birthday attack](/birthday-attack/) at $2^{n/2}$, [Pollard's rho](/pollard-rho-collision-search/) with constant memory, [preimage search](/preimage-finding/) at $2^n$, and [Wagner's algorithm](/wagners-algorithm/) for sums of many lists.
3. **Chains and trees of hashes.** The [hash chain](/hash-chain/) of one-time passwords and the [Merkle tree](/merkle-tree/) of logs and signatures.
4. **Iterating a compression function.** The [Merkle-Damgård construction](/merkle-damgard-construction/), the [theorem](/merkle-damgard-theorem/) that proves it, its generic weaknesses such as [length extension](/length-extension-attack/), compression functions from block ciphers, and [indifferentiability](/indifferentiability-framework/).
5. **The MD4 family and its relatives.** [MD5](/md5/), [SHA-1](/sha-1/) and [SHA-2](/sha-2/), the attacks that broke the first two, and [chosen-prefix collisions](/chosen-prefix-collision/).
6. **Sponges and SHA-3.** The [sponge construction](/sponge-construction/), [SHA-3](/sha-3/) and the [extendable-output functions](/extendable-output-function/) SHAKE128 and SHAKE256.
7. **Other designs and tree modes.** [BLAKE2](/blake2/), [BLAKE3](/blake3/), the other SHA-3 finalists, and [tree hashing](/tree-hashing/).
8. **Keyed hashing.** [HMAC](/hmac/), NMAC and KMAC as MACs and pseudorandom functions, and [SipHash](/siphash/) for hash tables.
9. **Precomputation attacks.** [Time-memory tradeoffs](/time-memory-tradeoff/) and [rainbow tables](/rainbow-table/) against unsalted hashes.
10. **Password hashing.** Salts and slow functions: [PBKDF2](/pbkdf2/), [bcrypt](/bcrypt/), [scrypt](/scrypt/) and [Argon2](/argon2/), and the theory of [memory-hard functions](/memory-hard-function/).

## A first reading

For a first reading, take these fourteen entries in order: [cryptographic hash function](/cryptographic-hash-function/), [preimage resistance](/preimage-resistance/), [second-preimage resistance](/second-preimage-resistance/), [collision resistance](/collision-resistance/), [birthday attack](/birthday-attack/), [Merkle tree](/merkle-tree/), [compression function](/compression-function/), [Merkle-Damgård construction](/merkle-damgard-construction/), [length extension](/length-extension-attack/), [SHA-2](/sha-2/), [sponge construction](/sponge-construction/), [SHA-3](/sha-3/), [HMAC](/hmac/) and [password hashing](/password-hashing/). Together they give the definitions, the generic bound, the two main constructions, the hashes in use today, and the two most common ways to use a hash with a secret.

Skip at first the research entries on multicollisions, chosen-prefix collisions, indifferentiability and Wagner's algorithm, and the designs that are no longer in wide use: Tiger, Whirlpool, Grøstl, JH and Skein. The entries on MD4, MD5 and SHA-1 are best read as history and as case studies in how a hash breaks; never choose them for a new system.

## Before you start

You need the ordinary [hash function](/hash-function/) and the [birthday paradox](/birthday-paradox/), the [binary tree](/binary-tree/) for Merkle trees, and [Floyd's cycle detection](/floyd-cycle-detection/) for the rho method. From the chapter on symmetric ciphers you need the [block cipher](/block-cipher/), the [ideal cipher model](/ideal-cipher-model/), the [message authentication code](/message-authentication-code/) and the [pseudorandom function](/pseudorandom-function/); the round functions of BLAKE2 and scrypt come from [ChaCha20](/chacha20/) and [Salsa20](/salsa20/). The idea of a [one-way function](/one-way-function/) helps with preimage resistance, and the [pebbling lower bound](/pebbling-lower-bound/) is the tool behind memory-hard functions. You should be at ease with probability bounds of the form $q^2/2^n$ and with reading a reduction: an attacker against one thing turned into an attacker against another, with its cost and success counted.
