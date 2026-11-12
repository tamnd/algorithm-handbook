Two parties share a secret key of 128 bits. With it they want to send each other gigabytes of data so that an eavesdropper learns nothing beyond the length, and so that anyone who changes a byte on the way is caught. That is the job of a symmetric cipher. Every TLS 1.3 connection does it with one of two schemes, AES-GCM or ChaCha20-Poly1305, and both are short programs built from parts that this chapter takes apart one by one.

The chapter starts with the attacker, because a cipher is only secure against a stated adversary. [Kerckhoffs's principle](/kerckhoffs-principle/) gives the attacker the whole design and keeps only the key secret. The attack models then say what else it gets: ciphertexts only, known plaintexts, or encryptions of plaintexts it picks. The modern goal is IND-CPA, in the standard model: an efficient attacker with an encryption oracle cannot tell which of two messages of its choice was encrypted. The [one-time pad](/one-time-pad/) meets a stronger, information-theoretic goal, [perfect secrecy](/perfect-secrecy/), but Shannon proved that this needs as much key as message. Everything after the first group accepts computational security in exchange for short keys.

## What the chapter covers

1. **The problem and the attacker.** [Symmetric encryption](/symmetric-encryption/), [cryptanalysis](/cryptanalysis/), the [ciphertext-only](/ciphertext-only-attack/), [known-plaintext](/known-plaintext-attack/) and [chosen-plaintext](/chosen-plaintext-attack/) attacks, perfect secrecy and [Shannon's theorem](/shannon-perfect-secrecy-theorem/).
2. **Classical ciphers and how they fall.** The [Caesar](/caesar-cipher/), [affine](/affine-cipher/), [substitution](/substitution-cipher/), [Playfair](/playfair-cipher/), [columnar transposition](/columnar-transposition-cipher/), [Hill](/hill-cipher/) and [Vigenère](/vigenere-cipher/) ciphers and the [Enigma machine](/enigma-machine/), with [frequency analysis](/frequency-analysis/), the [index of coincidence](/index-of-coincidence/), [Kasiski examination](/kasiski-examination/) and the general method of [cipher breaking](/cipher-breaking/).
3. **Building a block cipher.** The [block cipher](/block-cipher/) as a keyed permutation, [confusion and diffusion](/confusion-and-diffusion/), the [S-box](/s-box/), the [key schedule](/key-schedule/), the [Feistel network](/feistel-network/) and the [substitution-permutation network](/substitution-permutation-network/).
4. **DES and AES.** [DES](/data-encryption-standard/), [key recovery](/key-recovery/), [exhaustive key search](/exhaustive-key-search/), [Triple DES](/triple-des/) and [AES](/advanced-encryption-standard/).
5. **Pseudorandom functions and permutations.** The [PRF](/pseudorandom-function/) and [PRP](/pseudorandom-permutation/), the [switching lemma](/prp-prf-switching-lemma/), [semantic security](/semantic-security/), the [Luby-Rackoff theorem](/luby-rackoff-theorem/), the [ideal cipher model](/ideal-cipher-model/) and [key whitening](/key-whitening/).
6. **Modes of operation.** The [initialization vector](/initialization-vector/) and the [nonce](/nonce/), [block padding](/block-padding/) and [PKCS #7](/pkcs7-padding/), and the modes [ECB](/ecb-mode/), [CBC](/cbc-mode/), [CFB](/cfb-mode/), [OFB](/ofb-mode/), [CTR](/ctr-mode/) and [XTS](/xts-mode/).
7. **Stream ciphers.** The [stream cipher](/stream-cipher/), the [LFSR](/lfsr/), [RC4](/rc4/), [A5/1](/a5-1/), [Salsa20](/salsa20/), [ChaCha20](/chacha20/), [Trivium](/trivium/), [Grain](/grain/), [SNOW 3G](/snow-3g/) and [ZUC](/zuc/).
8. **Message authentication and authenticated encryption.** [Message authentication](/message-authentication/), the [MAC](/message-authentication-code/), [CBC-MAC](/cbc-mac/), [CMAC](/cmac/), [Poly1305](/poly1305/), [authenticated encryption](/authenticated-encryption/), [GCM](/gcm-mode/), [CCM](/ccm-mode/) and its [decryption check](/ccm-decryption-check/), [EAX](/eax-mode/), [OCB](/ocb-mode/), [ChaCha20-Poly1305](/chacha20-poly1305/) and [Ascon](/ascon/).
9. **Attacks on block ciphers.** [Differential](/differential-cryptanalysis/), [linear](/linear-cryptanalysis/), [boomerang](/boomerang-attack/), [integral](/integral-cryptanalysis/), [slide](/slide-attack/) and [related-key](/related-key-attack/) attacks.
10. **More block ciphers.** [Blowfish](/blowfish/), [TEA](/tea/), [XTEA](/xtea/), [IDEA](/idea/), [RC5](/rc5/), [RC6](/rc6/), [Serpent](/serpent/), [Twofish](/twofish/), [Camellia](/camellia/), [ARIA](/aria/), [SM4](/sm4/), [GOST 28147-89](/gost-28147-89/), [Kuznyechik](/kuznyechik/), [Skipjack](/skipjack/), [PRESENT](/present/), [SIMON](/simon-cipher/), [SPECK](/speck/) and [lightweight cryptography](/lightweight-cryptography/).

## A first reading

Read these in order for one path from the definition to a cipher you would deploy:

1. [Symmetric encryption](/symmetric-encryption/), for the syntax and the IND-CPA goal.
2. [Chosen-plaintext attack](/chosen-plaintext-attack/), for the game itself.
3. [One-time pad](/one-time-pad/) and [Shannon's theorem](/shannon-perfect-secrecy-theorem/), for the limit of perfect secrecy.
4. [Block cipher](/block-cipher/) and [Feistel network](/feistel-network/).
5. [AES](/advanced-encryption-standard/), the cipher in use.
6. [Exhaustive key search](/exhaustive-key-search/), which sets the key length.
7. [Pseudorandom permutation](/pseudorandom-permutation/) and the [switching lemma](/prp-prf-switching-lemma/).
8. [CBC mode](/cbc-mode/) and [CTR mode](/ctr-mode/).
9. [Authenticated encryption](/authenticated-encryption/) and [GCM](/gcm-mode/).

Skip the classical ciphers on a first pass unless you like puzzles; they teach attack methods, not designs to use. Leave the attacks on block ciphers and the catalogue of other ciphers for a second reading. The code on every page is for study only and is not constant time; real systems take AES or ChaCha20 from a validated library.

## Before you start

The proofs use the [birthday paradox](/birthday-paradox/) and the [union bound](/union-bound/) on almost every page: block sizes and nonce lengths come from them. The classical ciphers need [congruences](/congruence/), the [modular inverse](/modular-inverse/) and, for the Hill cipher, the [determinant](/determinant/) modulo 26. AES and GCM compute in fields of characteristic 2, so [polynomial arithmetic over GF(2)](/gf2-polynomial-arithmetic/) helps, and the stream ciphers use the [linear feedback shift register](/linear-feedback-shift-register/). The security definitions build on [computational indistinguishability](/computational-indistinguishability/) and the [pseudorandom generator](/pseudorandom-generator/). The [meet-in-the-middle attack](/meet-in-the-middle-attack/) explains why double encryption adds almost nothing.
