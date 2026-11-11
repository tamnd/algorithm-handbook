## What to remember

- [Ring leader election](/ring-leader-election/) asks exactly one process to become the leader. In the [explicit form](/explicit-leader-election/) every process also learns the leader's identifier, for at most $n$ more messages on a ring.
- [Chang-Roberts](/chang-roberts/) sends each identifier forward until a larger one stops it. It sends $n(n+1)/2$ election messages in the worst case and $2n - 1$ in the best, and $n H_n \approx 0.69\, n \lg n$ on average over all orders.
- Phases that at least halve the number of candidates give $O(n \log n)$. [Franklin](/franklin/) keeps the local maxima at $2n$ messages per phase, for at most $2n \lfloor \lg n \rfloor + 2n$. [Peterson](/peterson-leader-election/) and [Dolev-Klawe-Rodeh](/dolev-klawe-rodeh/) simulate Franklin on a one-way ring. [Hirschberg-Sinclair](/hirschberg-sinclair/) probes to distance $2^k$ in phase $k$ and needs neither FIFO channels nor orientation.
- The [lower bound](/ring-election-lower-bound/) is $\Omega(n \log n)$ for uniform asynchronous rings and for synchronous algorithms that only compare identifiers. A synchronous algorithm that uses identifiers as numbers can elect with $n$ messages by waiting $n \cdot u_{\min}$ rounds.
- On an [anonymous ring](/anonymous-ring-impossibility/) no deterministic algorithm elects a leader, even when $n$ is known. With $n$ known, [Itai-Rodeh](/itai-rodeh/) elects with probability 1, in at most $(1 - 1/n)^{-n} \le 4$ expected rounds. With $n$ unknown, no randomized algorithm both always terminates and is always correct.
- [FloodMax](/floodmax/) elects in exactly $d$ rounds with $2md$ messages if $d$ is at least the diameter; with a smaller $d$ it can elect two leaders.
- A [tree](/tree-leader-election/) needs $\Theta(n)$ messages, and [saturation](/tree-election/) uses $3n + k - 4 \le 4n - 4$ with $k$ starters. A general network needs $O(m + n \log n)$, which [Awerbuch's algorithm](/awerbuch-leader-election/) reaches in $O(n)$ time.
- A [complete network](/complete-network-leader-election/) still needs $\Omega(n \log n)$ messages without a sense of direction. [Korach-Kutten-Moran](/korach-kutten-moran/) sends at most $4 n H_n$, and [Afek-Gafni](/afek-gafni/) at most $4n \lceil \lg n \rceil + n - 1$ in $4 \lceil \lg n \rceil + 1$ rounds.
- The [bully algorithm](/bully-algorithm/) elects the largest live process under crashes but needs synchronous timeouts and breaks under partitions. The [invitation algorithm](/invitation-algorithm/) promises only one coordinator per group.

## The algorithms side by side

| Algorithm | Network | Channels | Messages, worst case | Leader |
|---|---|---|---|---|
| [Chang-Roberts](/chang-roberts/) | one-way ring | any order | $n(n+1)/2 + n$ | largest identifier |
| [Hirschberg-Sinclair](/hirschberg-sinclair/) | two-way ring | any order | at most $8n \lceil \lg n \rceil$, plus $n$ | largest identifier |
| [Franklin](/franklin/) | two-way ring | FIFO | $2n \lfloor \lg n \rfloor + 2n$, plus $n$ | largest identifier |
| [Peterson](/peterson-leader-election/) | one-way ring | FIFO | $2n \lfloor \lg n \rfloor + n$, plus $n$ | holder of the largest value |
| [Dolev-Klawe-Rodeh](/dolev-klawe-rodeh/) | one-way ring | FIFO | $2n \lfloor \lg n \rfloor + 2n$ | largest identifier |
| [Itai-Rodeh](/itai-rodeh/) | anonymous one-way ring, $n$ known | FIFO | $O(n \log n)$ expected | random |
| [FloodMax](/floodmax/) | any, synchronous | rounds | $2md$ | largest identifier |
| [Saturation](/tree-election/) | tree | any order | $3n + k - 4$ | largest identifier |
| [Awerbuch](/awerbuch-leader-election/) | any | any order | $O(m + n \log n)$ | root of the last fragment |
| [Korach-Kutten-Moran](/korach-kutten-moran/) | complete | any order | $4 n H_n$ | highest level |
| [Bully](/bully-algorithm/) | complete, synchronous, crashes | rounds | $O(n^2)$ | largest live identifier |

: Election algorithms by network and worst-case message count. "Plus $n$" is the announcement that makes the election explicit; $m$ counts links, $d$ is the diameter bound and $k$ the number of starters.

## Choosing a method

On a ring with identifiers, use [Chang-Roberts](/chang-roberts/) when $n$ is small or the order of identifiers is random, since its average is close to the optimum. When the worst case matters, use [Franklin](/franklin/) on a two-way ring with FIFO channels, [Peterson](/peterson-leader-election/) on a one-way ring with FIFO channels, and [Hirschberg-Sinclair](/hirschberg-sinclair/) when channels may reorder messages. If every process must know that the largest identifier won, use [Dolev-Klawe-Rodeh](/dolev-klawe-rodeh/) or add an announcement.

If the processes have no identifiers, draw random ones with [Itai-Rodeh](/itai-rodeh/); it needs $n$ known or bounded within a factor of two.

On a tree, use [saturation](/tree-election/). On a synchronous network with a known diameter bound, [FloodMax](/floodmax/) is the simplest choice. On a general asynchronous network, build a spanning tree and elect on it, or run [Awerbuch's algorithm](/awerbuch-leader-election/) when time matters too.

In a real cluster where machines crash, the [bully algorithm](/bully-algorithm/) is safe only with true timing bounds. Where the network can split, either accept one coordinator per group as in the [invitation algorithm](/invitation-algorithm/), or elect through a consensus protocol such as [Raft](/raft/), whose majority rule prevents [split brain](/split-brain/).
