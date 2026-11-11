## What to remember

- A [Byzantine](/byzantine-failure-model/) process may send anything, including different values to different processes. Without signatures, [broadcast](/byzantine-broadcast/) and consensus among $n$ processes with $t$ faults are possible exactly when $n > 3t$; on a general network the vertex connectivity must also be at least $2t + 1$. The [resilience bound](/byzantine-resilience-bound/) proves both.
- With unforgeable signatures, broadcast works for every $t < n$, but consensus with [strong validity](/strong-validity/) still needs $n > 2t$, by the [authenticated resilience bound](/authenticated-resilience-bound/). [Weak validity](/weak-validity/) does not lower the bound $n > 3t$ when there are no signatures.
- A deterministic algorithm needs $t + 1$ rounds in some run when $t \le n - 2$, with or without signatures, by the [round lower bound](/byzantine-round-lower-bound/). It also needs $\Omega(n + t^2)$ messages by the [Dolev-Reischuk bound](/dolev-reischuk-lower-bound/), so the $O(n^2)$ messages of [Dolev-Strong](/dolev-strong-algorithm/) are optimal for $t = \Theta(n)$.
- The [oral messages algorithm](/oral-messages-algorithm/) meets both $n > 3t$ and $t + 1$ rounds, but sends $(n-1)(n-2)\cdots(n-t-1)$ messages in its last round. The [phase king](/phase-king-algorithm/) trades $3(t + 1)$ rounds for $O(n^2 t)$ one-bit messages, and the [phase queen](/phase-queen-algorithm/) uses $2(t + 1)$ rounds but needs $n > 4t$.
- In an asynchronous network a deterministic algorithm cannot agree. [Bracha's reliable broadcast](/bracha-reliable-broadcast/) echoes on more than $(n + t)/2$ ECHO messages, amplifies on $t + 1$ READY messages and delivers on $2t + 1$, so honest processes never deliver different values. [Bracha's agreement](/bracha-asynchronous-agreement/) runs on it with local coins in $O(2^n)$ expected rounds; a common coin, as in [Rabin's algorithm](/rabin-randomized-byzantine-agreement/), makes it a constant.
- With $n = 3f + 1$ replicas a [quorum certificate](/quorum-certificate/) holds $2f + 1$ signed votes, and two certificates share at least $f + 1$ replicas, so at least one honest replica, which never votes twice. A client needs $f + 1$ matching replies. A [masking quorum system](/byzantine-quorum-system/) needs overlap $2f + 1$ and $n \ge 4f + 1$.
- [PBFT](/pbft/) commits in 3 message delays with $2n(n-1)$ messages. [HotStuff](/hotstuff/) uses $8(n-1)$ messages per view and a lock on the second certificate. [HoneyBadgerBFT](/honeybadger-bft/) makes progress with no timing assumption at all.

## The protocols side by side

| Protocol | Timing model | Faults tolerated | Best case | Messages, best case | Weak point |
|---|---|---|---|---|---|
| [Oral messages](/oral-messages-algorithm/) | synchronous | $n > 3t$ | $t + 1$ rounds | $n^{\Theta(t)}$ | exponential messages |
| [Phase king](/phase-king-algorithm/) | synchronous | $n > 3t$ | $3(t + 1)$ rounds | $O(n^2 t)$ | always all phases |
| [Phase queen](/phase-queen-algorithm/) | synchronous | $n > 4t$ | $2(t + 1)$ rounds | $O(n^2 t)$ | lower resilience |
| [Dolev-Strong](/dolev-strong-algorithm/) | synchronous, signatures | $t < n$ | $t + 1$ rounds | $(n-1)^2$ | needs a public-key setup |
| [Bracha agreement](/bracha-asynchronous-agreement/) | asynchronous | $n > 3t$ | 1 round of 3 steps | $O(n^3)$ per round | exponential expected rounds |
| [Rabin](/rabin-randomized-byzantine-agreement/) | synchronous, dealt coin | $n \ge 8t + 1$ as given | 1 round | $2n(n-1)$ | trusted dealer |
| [PBFT](/pbft/) | partial synchrony | $n = 3f + 1$ | 3 delays | $2n(n-1)$ | quadratic, heavy view change |
| [Zyzzyva](/zyzzyva/) | partial synchrony | $n = 3f + 1$ | 3 delays | $2n$ | published view change unsafe |
| [Tendermint](/tendermint/) | partial synchrony | $n = 3f + 1$ | 3 delays | $\Theta(n^2)$ | waits for timeouts |
| [HotStuff](/hotstuff/) | partial synchrony | $n = 3f + 1$ | 7 delays | $8(n-1)$ per view | more delays |
| [HoneyBadgerBFT](/honeybadger-bft/) | asynchronous | $n = 3f + 1$ | $O(\log n)$ expected rounds | $O(n^3)$ | threshold cryptography, high latency |

: Byzantine agreement and replication protocols. $n$ counts processes or replicas, $t$ or $f$ faults.

## Choosing a method

For a fixed group of replicas that must stay correct when some are compromised, use a leader-based protocol with $3f + 1$ replicas under partial synchrony. [PBFT](/pbft/) suits a small group in one data centre. For hundreds of replicas, [HotStuff](/hotstuff/) sends linear messages per view and [Tendermint](/tendermint/) spreads votes by gossip; both rotate the leader. Do not deploy [Zyzzyva](/zyzzyva/) as published.

When an attacker may control the network's timing, timeouts can stall forever; use an asynchronous protocol such as [HoneyBadgerBFT](/honeybadger-bft/), built on [reliable broadcast](/byzantine-reliable-broadcast/) and randomized binary agreement with a common coin.

For a one-shot decision in synchronous rounds, use [Dolev-Strong](/dolev-strong-algorithm/) when a public-key setup exists, since it tolerates any $t < n$. Without signatures, use the [phase king](/phase-king-algorithm/) for binary values with $n > 3t$, or the phase queen when $n > 4t$ and rounds matter. Keep the [oral messages algorithm](/oral-messages-algorithm/) for teaching.
