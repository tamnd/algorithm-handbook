## What to remember

- [Entity authentication](/entity-authentication/) needs freshness: a one-message protocol with a stateless verifier cannot stop replay, and mutual authentication from nonces alone needs three messages. The answer must name the prover, or a reflection attack works.
- A [commitment](/commitment-scheme/) cannot be both perfectly hiding and perfectly binding. [Pedersen's](/pedersen-commitment/) $C = g^m h^r$ is perfectly hiding and binding under the discrete logarithm assumption, and whoever knows $\log_g h$ can open $C$ to any value. In every $r$-round [coin flip](/fair-coin-flipping/) a party who may abort gets a bias of $\Omega(1/r)$, by Cleve's bound.
- A [sigma protocol](/sigma-protocol/) has three moves, special soundness and special honest-verifier [zero knowledge](/zero-knowledge-proof/), so it is a [proof of knowledge](/proof-of-knowledge/) with knowledge error $1/|C|$. In [Schnorr's protocol](/schnorr-identification-protocol/), answers $z, z'$ to challenges $c \ne c'$ for one nonce give $x = (z - z')(c - c')^{-1} \bmod q$, so a reused nonce leaks the key.
- In [Shamir's scheme](/shamir-secret-sharing/) any $t$ shares give $s = \sum_j \lambda_j y_j$ and any $t - 1$ shares are uniform. A wrong share shifts the secret by $\lambda_j \delta$ without a sign; [verifiable secret sharing](/verifiable-secret-sharing/) adds checks, and [threshold cryptography](/threshold-cryptography/) never rebuilds the key.
- [Secure computation](/secure-multiparty-computation/) is defined by simulation. Against [semi-honest](/semi-honest-model/) parties every function is computable for $t < n$ from [oblivious transfer](/oblivious-transfer/), and for $t < n/2$ over private channels with no assumption. Against [malicious](/malicious-adversary-model/) parties perfect security needs $t < n/3$, full security an honest majority, and a dishonest majority gets security with abort.
- [OT extension](/oblivious-transfer-extension/) turns $\kappa$ base OTs into any number, each costing $\kappa$ bits from the receiver, $2\ell$ from the sender and three hash calls.
- [Garbled circuits](/yao-garbled-circuits/) take constant rounds and, with half gates, $2k$ bits per AND gate and none per XOR. [GMW](/gmw-protocol/) takes $d + O(1)$ rounds for AND depth $d$, and [BGW](/bgw-protocol/) reduces the degree $2t$ of each product back to $t$. A [cut-and-choose](/cut-and-choose/) check that opens $c$ of $s$ copies misses $k$ bad copies with probability $\binom{s-k}{c}/\binom{s}{c}$.
- [zk-SNARKs](/zk-snark/) rest on knowledge assumptions, the generic group model or a random oracle; no SNARG for NP has a black-box proof from a falsifiable assumption. [zk-STARKs](/zk-stark/) need only a hash function in the random oracle model.

## The protocols side by side

| Protocol | Adversary | Rounds | Assumption |
|---|---|---|---|
| [Blum coin flip](/fair-coin-flipping/) | malicious, 2 parties, secure with abort | 3 messages | a commitment scheme |
| [Schnorr identification](/schnorr-identification-protocol/) | passive impersonation; honest-verifier ZK | 3 moves | discrete log; one-more discrete log for active attacks |
| [Feige-Fiat-Shamir](/feige-fiat-shamir-identification/) | soundness $2^{-kt}$; ZK when $2^k$ is polynomial | $t$ rounds of 3 moves | square roots modulo $n$, as hard as factoring |
| [Shamir sharing](/shamir-secret-sharing/) | any $t - 1$ parties, unbounded | 1 message | none |
| [IKNP extension](/oblivious-transfer-extension/) | semi-honest | base OTs, then 1 message each way | base OT and a random oracle |
| [Yao's garbled circuits](/yao-garbled-circuits/) | semi-honest, 2 parties | 2 messages plus the OT rounds | OT; circular correlation robustness for free XOR |
| [GMW](/gmw-protocol/) | semi-honest, $t < n$ | AND depth $d$, plus input and output | OT |
| [BGW](/bgw-protocol/) | perfect; semi-honest $t < n/2$, malicious $t < n/3$ | $O(d)$ | private channels only |
| [DH private set intersection](/private-set-intersection/) | semi-honest | 2 messages | DDH in the random oracle model |
| [Two-server PIR](/private-information-retrieval/) | servers that do not collude, perfect | 1 query to each server | none |
| [Dining cryptographers](/dining-cryptographers/) | unbounded, honest key graph connected | 1 broadcast round | none |
| [TLS 1.3 handshake](/tls-handshake/) | active network attacker, multi-stage model | 1 round trip | Diffie-Hellman, signature, HKDF, hash |

: Selected protocols with the model, rounds and assumption that their entries state.

## Choosing a method

To log in, use [challenge-response](/challenge-response-authentication/) over a fresh nonce and both names, or TOTP as a second factor. Inside an organization use [Kerberos](/kerberos/), and on the internet the [TLS 1.3 handshake](/tls-handshake/), without 0-RTT data for requests that must not run twice. For messaging through an untrusted server, use the [Signal protocol](/signal-protocol/), or MLS for large groups.

To back up a key, use [Shamir's scheme](/shamir-secret-sharing/). When no machine may hold it, use [threshold signing or decryption](/threshold-cryptography/) with distributed key generation.

Between two parties, use [garbled circuits](/yao-garbled-circuits/) when latency is high or the circuit is deep, and [GMW](/gmw-protocol/) on a fast network with shallow circuits. With an honest majority, [BGW](/bgw-protocol/) on Shamir shares needs no assumption. Accept semi-honest security only for audited parties; otherwise add [cut-and-choose](/cut-and-choose/) or MAC checks. Special protocols such as [PSI](/private-set-intersection/) and [PIR](/private-information-retrieval/) are far cheaper than generic ones.

For a short public proof, a [zk-SNARK](/zk-snark/) is smallest if a trusted setup is acceptable; a [zk-STARK](/zk-stark/) needs no setup.
