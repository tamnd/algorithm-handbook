## What to remember

- A [public-key encryption](/public-key-encryption/) scheme is a triple $(\mathrm{Gen}, \mathrm{Enc}, \mathrm{Dec})$, and its security claim has two parts: a notion such as [IND-CPA](/ind-cpa-security/) or [IND-CCA2](/ind-cca-security/), and an assumption with a model, standard or [random oracle](/random-oracle-model/). A deterministic scheme is never IND-CPA, because the adversary can encrypt both candidates itself.
- In [RSA](/rsa-cryptosystem/), $ed \equiv 1 \pmod{\lambda(N)}$ and decryption is $c^d \bmod N$, about four times faster with the CRT. The [RSA problem](/rsa-problem/) is no harder than factoring, and the converse is open. Knowing $(N, e, d)$ factors $N$. [Rabin](/rabin-cryptosystem/) is as hard to invert as factoring, but one decryption query factors $N$ with probability $1/2$.
- Textbook RSA, ElGamal, Goldwasser-Micali and Paillier are malleable, and a scheme with a useful homomorphism cannot be IND-CCA2: the adversary transforms the challenge and asks for its decryption. NM-CCA2 is equivalent to IND-CCA2.
- [PKCS #1 v1.5](/rsa-pkcs1-v1-5-encryption/) has no security proof, and a padding error oracle decrypts with about a million queries (Bleichenbacher 1998). [OAEP](/rsa-oaep/) is IND-CCA2 under the RSA assumption in the random oracle model, with a loose reduction of order $\varepsilon^2/4$, and carries at most $k - 2h - 2$ octets.
- DDH $\le$ CDH $\le$ DL: an algorithm for the right one solves the left one. [ElGamal](/elgamal-encryption/) is IND-CPA under [DDH](/decisional-diffie-hellman/) in the standard model, with $\mathrm{Adv}^{\mathrm{ind\text{-}cpa}} = 2\,\mathrm{Adv}^{\mathrm{ddh}}$. DDH fails in all of $\mathbb{Z}_p^*$, where the Legendre symbol gives advantage $1/2$, so the group must have prime order.
- A [KEM](/key-encapsulation-mechanism/) plus a one-time DEM gives [hybrid encryption](/hybrid-encryption/) with $\mathrm{Adv} \le 2\,\mathrm{Adv}^{\mathrm{kem}} + \mathrm{Adv}^{\mathrm{dem}}$, a tight bound in the standard model. The [Fujisaki-Okamoto transform](/fujisaki-okamoto-transform/) turns a weak scheme into an IND-CCA KEM in the random oracle model.
- The implementation leaks even when the scheme is sound. [Blinding](/rsa-blinding/) hides the input of $c^d$ from [timing attacks](/timing-attack/), and one faulty CRT signature $s'$ factors $N$ as $\gcd(s'^e - m, N)$ unless the device [verifies](/rsa-fault-attack/) it before it answers.
- At 128-bit security, SP 800-57 puts 3072-bit RSA level with a 256-bit [elliptic curve](/elliptic-curve-cryptography/). [Shor's algorithm](/shor-algorithm/) breaks both on a quantum computer.

## The schemes side by side

| Scheme | Assumption | Notion and model | Ciphertext |
|---|---|---|---|
| [Textbook RSA](/rsa-cryptosystem/) | RSA | one-way only, deterministic | one element of $\mathbb{Z}_N$ |
| [PKCS #1 v1.5](/rsa-pkcs1-v1-5-encryption/) | none proved | not IND-CCA | $k$ octets |
| [RSA-OAEP](/rsa-oaep/) | RSA | IND-CCA2, random oracle model | $k$ octets, message at most $k - 2h - 2$ |
| [Rabin](/rabin-cryptosystem/) | factoring | one-way only | one element of $\mathbb{Z}_N$ |
| [ElGamal](/elgamal-encryption/) | DDH | IND-CPA, standard model, tight | two group elements |
| [Cramer-Shoup](/cramer-shoup-cryptosystem/) | DDH and a target collision resistant hash | IND-CCA2, standard model | four group elements |
| [ECIES](/ecies/) | oracle Diffie-Hellman | IND-CCA2, random oracle model | a point, the message and a tag |
| [Goldwasser-Micali](/goldwasser-micali-cryptosystem/) | quadratic residuosity | IND-CPA, standard model | one element of $\mathbb{Z}_N$ per message bit |
| [Blum-Goldwasser](/blum-goldwasser-cryptosystem/) | factoring Blum integers | IND-CPA, standard model | the message plus one element of $\mathbb{Z}_N$ |
| [Paillier](/paillier-cryptosystem/) | DCR | IND-CPA, standard model, tight | one element of $\mathbb{Z}_{N^2}$ |

: Public-key encryption schemes of the chapter. $k$ is the length of $N$ in octets and $h$ the hash length in octets. Only the rows with IND-CCA2 resist an active attacker.

## Choosing a method

To encrypt data to a public key, use [hybrid encryption](/hybrid-encryption/) with an IND-CCA KEM and an authenticated cipher, as HPKE (RFC 9180) does. Take it from a maintained library, such as a FIPS 140 validated module or libsodium's sealed boxes, never from the study code of the entries, which is not constant time. On elliptic curves that means a DHKEM or [ECIES](/ecies/). When RSA keys are required, use [OAEP](/rsa-oaep/) or RSA-KEM with 3072-bit moduli for 128-bit security, and never PKCS #1 v1.5 in a new design. For protection against a future quantum computer, use [ML-KEM](/crystals-kyber/).

Use a standard-model scheme such as [Cramer-Shoup](/cramer-shoup-cryptosystem/) when a proof without random oracles matters more than size. Use [Paillier](/paillier-cryptosystem/) or exponential [ElGamal](/elgamal-encryption/) only inside protocols that need to add ciphertexts, such as voting, and never let them decrypt inputs from untrusted parties. Keep textbook RSA, Rabin, Goldwasser-Micali and the [knapsack](/merkle-hellman-knapsack-cryptosystem/) for teaching.
