## What to remember

- **One probe is possible in two cases.** A direct-address table reads one slot when the universe is small. A perfect hash function reads one slot for a fixed key set, at the cost of building the function after the keys are known; a minimal one needs about $1.443$ bits per key and no more.
- **Every expected cost has a model behind it.** Simple uniform hashing assumes the hash values behave like independent uniform random slots. No fixed hash function satisfies it for all inputs, so it is either an assumption about the keys or a property of a random choice of the function.
- **Chaining costs $\Theta(1 + \alpha)$.** An unsuccessful search examines $\alpha$ keys on average and a successful one $1 + (n - 1)/(2m)$. A universal family gives the same means for every key set, so a random seed protects a table against chosen inputs.
- **Open addressing pays more as the table fills.** Without clustering, an unsuccessful search costs $1/(1 - \alpha)$ probes and a successful one $(1/\alpha)\ln(1/(1 - \alpha))$. Both grow without bound as $\alpha \to 1$, so open-addressing tables grow well before they are full.
- **Clustering is the price of a simple probe sequence.** Linear probing builds runs and its unsuccessful cost grows like $1/(1 - \alpha)^2$. Quadratic probing removes the runs but keeps secondary clustering, which costs only a few extra probes at practical loads. Double hashing behaves almost like uniform probing.
- **Averages hide the worst search.** With $n = m$, the longest chain holds $\Theta(\log n/\log\log n)$ keys with high probability, and a fixed hash function has inputs that put all keys in one slot.
- **The setting can change the hash.** Zobrist hashing makes the hash of a position cheap to update after a move, and dynamic hashing moves the keys of one bucket at a time instead of the whole table.

## The costs side by side

| Method | Unsuccessful search | Successful search | Both at $\alpha = 1/2$ | Worst case |
|---|---|---|---|---|
| [Direct-address table](/direct-address-table/) | 1 slot | 1 slot | 1 and 1 | $\Theta(1)$ |
| [Perfect hash function](/perfect-hash-function/) | 1 slot and a key check | 1 slot | 1 and 1 | $O(1)$ |
| [Separate chaining](/chaining-expected-search-time/) | $\alpha$ keys | $1 + \alpha/2$ keys | 0.5 and 1.25 | $\Theta(n)$ |
| [Uniform probing](/open-addressing-expected-probes/) | $\frac{1}{1 - \alpha}$ | $\frac{1}{\alpha}\ln\frac{1}{1 - \alpha}$ | 2 and 1.39 | $\Theta(n)$ |
| [Secondary clustering](/secondary-clustering/) | $\frac{1}{1 - \alpha} - \alpha + \ln\frac{1}{1 - \alpha}$ | $1 + \ln\frac{1}{1 - \alpha} - \frac{\alpha}{2}$ | 2.19 and 1.44 | $\Theta(n)$ |
| [Linear probing](/primary-clustering/) | $\frac{1}{2}\left(1 + \frac{1}{(1 - \alpha)^2}\right)$ | $\frac{1}{2}\left(1 + \frac{1}{1 - \alpha}\right)$ | 2.5 and 1.5 | $\Theta(n)$ |

: Expected cost of a search. The open-addressing rows count probes and are limits for large tables; the chaining row counts keys examined, after the hash. The secondary clustering row is Knuth's approximation for a scheme in which the sequence depends only on the first probe. Space is $\Theta(u)$ for the direct-address table and $\Theta(n + m)$ for the others.

## Choosing a table

- When the keys are small integers, use a direct-address table or a bit vector. Nothing is faster, and the code is a single array access.
- When the key set is fixed and known in advance, as for the keywords of a language or a dictionary shipped with a program, build a perfect hash function. Store the keys too if a search may ask for keys outside the set.
- For a general in-memory table, use chaining, or open addressing with a resize at a load between $1/2$ and $7/8$. Linear probing is fast in practice at moderate loads because its probes stay in one cache line.
- When an adversary may choose the keys, draw the hash function from a universal family with a secret seed.
- When the table lives on disk or must never pause for a full rebuild, use linear hashing or extendible hashing.
- When the keys are states that change a little at a time, such as board positions, use Zobrist hashing and update the hash with each change.
