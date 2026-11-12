## What to remember

- **Diffie-Hellman is secure only against a passive adversary.** Both sides get $g^{xy}$ from $g^x$ and $g^y$. Computing it is the [CDH](/computational-diffie-hellman/) problem; telling it from random is [DDH](/decisional-diffie-hellman/). An active [man in the middle](/man-in-the-middle-attack/) runs one exchange with each side, so real protocols add authentication from data held in advance.
- **Check every received element.** In a subgroup of prime order $q$, accept $Y$ only if $2 \le Y \le p - 2$ and $Y^q \equiv 1 \pmod p$. Otherwise a [small subgroup attack](/small-subgroup-attack/) learns a static secret modulo each small factor of $p - 1$, and the invalid-curve attack does the same to [ECDH](/ecdh/). [X25519](/x25519/) clamps the scalar to a multiple of the cofactor 8 instead.
- **Forward secrecy comes from fresh secrets and erasure.** RSA key transport has none. Two-message protocols authenticated only by static keys, such as [HMQV](/hmqv/), get only weak forward secrecy; a third message, as in [SIGMA](/sigma-key-exchange/), gives full forward secrecy.
- **Bind the identities.** After an [unknown key-share attack](/unknown-key-share-attack/) two honest parties share a key but disagree on the peer. The fixes put the names into the key, $K = H(g^{xy}, \hat A, \hat B)$, or into the authentication, as SIGMA's $\mathrm{MAC}_{K_m}(\hat A)$ does.
- **Never use the shared secret as a key.** [HKDF](/hkdf/) extracts $\mathrm{PRK} = \mathrm{HMAC}(\mathit{salt}, Z)$ and expands it with $T(i) = \mathrm{HMAC}(\mathrm{PRK}, T(i-1) \,\|\, \mathit{info} \,\|\, i)$, one label per key.
- **Ratchets give two kinds of protection.** A KDF chain, $mk = \mathrm{HMAC}(ck, \texttt{0x01})$ and $ck' = \mathrm{HMAC}(ck, \texttt{0x02})$, protects old messages after a theft of the state. A Diffie-Hellman ratchet also heals the keys after one fresh exchange: post-compromise security.
- **A password allows one online guess per run.** A [PAKE](/password-authenticated-key-exchange/) lets each active run test at most one guess and gives an eavesdropper nothing to test off line. In augmented protocols, [SRP](/secure-remote-password/) and [OPAQUE](/opaque/), the server stores only a verifier.
- **Predistribution has a sharp threshold.** [Blom's scheme](/blom-scheme/) gives each user $k + 1$ field elements. Any $k$ colluders learn nothing about another pair's key; $k + 1$ learn every key.
- **Groups trade rounds against work.** For $n$ members, [Ingemarsson-Tang-Wong](/ingemarsson-tang-wong/) needs $n - 1$ rounds, [Burmester-Desmedt](/burmester-desmedt/) 2 rounds and 3 exponentiations each, and a [key tree](/tree-based-group-diffie-hellman/) handles a join in $O(\log n)$ exponentiations.

## The main two-party protocols side by side

| Protocol | Messages | Authentication | Forward secrecy | Assumption and model |
|---|---|---|---|---|
| [Ephemeral Diffie-Hellman](/diffie-hellman/) | 2 | none | yes, against a passive adversary | CDH or DDH |
| [Station-to-station](/station-to-station-protocol/) | 3 | signatures, explicit | full | no proof in the CK model as first given |
| SIGMA-I | 3 | signature and MAC, explicit | full | CK model: DDH, unforgeable signature, secure MAC, PRF |
| [MQV](/mqv/) | 2 | static DH keys, implicit | weak | no proof |
| HMQV | 2 | static DH keys, implicit | weak | CK model, ROM, CDH; KCI needs gap-DH and KEA1 |
| [X3DH](/x3dh/) | 1, asynchronous | static DH keys, implicit | yes; weaker with no one-time prekey | gap-DH, KDF as a random oracle |
| [EKE2](/encrypted-key-exchange/) | 2 | password, implicit | yes | CDH, ideal cipher model and ROM |
| [SPAKE2](/spake2/) | 2, plus 2 optional tags | password, explicit with the tags | yes, against an eavesdropper | BPR model, ROM, CDH |
| [CPace](/cpace/) | 2 (one round) | password, implicit | weak; perfect with a MAC round | UC, ROM, sCDH and sSDH |
| SRP-6a | 4 | password, augmented | yes, against an eavesdropper | no proof in a standard model |
| OPAQUE | 3 | password, augmented | yes | UC strong aPAKE, ROM, one-more DH |

: Two-party protocols. Weak forward secrecy covers only sessions whose messages the adversary did not change. Every row rests on a discrete logarithm, which Shor's algorithm solves on a quantum computer; hence [hybrid key exchange](/hybrid-key-exchange/).

## Choosing a method

- Client and server with certificates: the TLS 1.3 or IKEv2 handshake, which follow SIGMA. Do not design a new protocol.
- Known static keys and no certificates: a [Noise](/noise-protocol-framework/) pattern such as XX or IK.
- Asynchronous messaging: X3DH, then the [double ratchet](/double-ratchet/).
- A password shared by two devices: a balanced PAKE, CPace or SPAKE2. A password login to a server: an augmented PAKE; the CFRG chose OPAQUE.
- Secrecy against a future quantum computer: X25519 and ML-KEM in a hybrid exchange, both secrets fed to a KDF. Authentication stays classical.
- Sensors too weak for public keys: [key predistribution](/key-predistribution-problem/), with $k$ above the number of devices an attacker may capture.
- Always validate received keys, erase ephemeral secrets, and derive each key with its own label.
