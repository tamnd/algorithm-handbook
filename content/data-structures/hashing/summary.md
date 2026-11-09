## What to remember

- A **hash table** with $n$ keys in $m$ slots takes $O(1 + \alpha)$ expected time per operation, where $\alpha = n/m$, and $\Theta(n)$ in the worst case. Doubling the table when $\alpha$ passes a limit keeps $\alpha$ bounded at a cost of $O(1)$ amortized time per insert.
- **Separate chaining**, under simple uniform hashing, examines exactly $\alpha$ keys on average in an unsuccessful search and $1 + \alpha/2 - \alpha/(2n)$ in a successful one. It works at any load, even above 1.
- **Open addressing** with **uniform hashing** takes at most $1/(1-\alpha)$ probes for an unsuccessful search and $(1/\alpha)\ln(1/(1-\alpha))$ for a successful one. Yao showed that no scheme of this kind does better. **Linear probing** pays for its clusters: $\frac12(1 + 1/(1-\alpha)^2)$ and $\frac12(1 + 1/(1-\alpha))$. It is still the fastest in practice at moderate load, because its probes stay in one cache line.
- Deletion in open addressing needs **tombstones**, or, for linear probing and Robin Hood hashing, a **backward shift**. Tombstones count toward the load and are cleared by a rehash.
- A fixed hash function has inputs that put every key in one slot, and attackers can find them. A function drawn from a **universal family** gives every pair of keys a collision probability of at most $1/m$, so the expected bounds hold for every input. Linear probing needs more: 5-wise independence suffices, and some pairwise independent families give $\Omega(\log n)$ expected time.
- **Cuckoo hashing** stores each key in one of two cells, so a search or delete takes $O(1)$ time in the worst case. Inserts take $O(1)$ expected amortized time while the load stays below $1/2$.
- For a **fixed set**, FKS perfect hashing gives $O(1)$ worst-case search in $\Theta(n)$ space after an $O(n)$ expected build: it retries until $\sum n_j^2 \le 4n$ and gives bucket $j$ a table of $n_j^2$ cells. A **minimal perfect hash function** needs at least about $1.443$ bits per key, and practical ones use 2 to 3.
- **Extendible** and **linear hashing** grow a table on disk one bucket at a time, with no full rehash.

## The main schemes side by side

| Scheme | Search | Insert | Delete | Space | Note |
|---|---|---|---|---|---|
| [Separate chaining](/separate-chaining/) | $O(1 + \alpha)$ expected | $O(1)$ | $O(1 + \alpha)$ expected | $\Theta(n + m)$ | any $\alpha$ |
| [Linear probing](/linear-probing/) | $\Theta(1)$ expected, $\Theta(m)$ worst | same as search | backward shift | $\Theta(m)$ | $\alpha < 1$ |
| [Double hashing](/double-hashing/) | $O(1/(1-\alpha))$ expected, $\Theta(m)$ worst | same as search | tombstone | $\Theta(m)$ | $\alpha < 1$ |
| [Robin Hood hashing](/robin-hood-hashing/) | $O(1)$ expected, $\Theta(m)$ worst | same as search | backward shift | $\Theta(m)$ | low variance |
| [Hopscotch hashing](/hopscotch-hashing/) | $O(H)$ worst | $O(m \cdot H)$ worst | $O(H)$ worst | $\Theta(m)$ | $H$ usually 32 |
| [Cuckoo hashing](/cuckoo-hashing/) | $O(1)$ worst | $O(1)$ expected amortized | $O(1)$ worst | two tables of $r \ge (1 + \varepsilon) n$ cells | load $< 1/2$ |
| [FKS perfect hashing](/fks-perfect-hashing/) | $O(1)$ worst | static, $O(n)$ expected build | static | $\Theta(n)$ | fixed set |
| [Dynamic perfect hashing](/dynamic-perfect-hashing/) | $O(1)$ worst | $O(1)$ expected amortized | $O(1)$ expected amortized | $O(n)$ | |

: Expected times assume a good random hash function and a load factor $\alpha$ bounded away from 1 for the open-addressing schemes. $H$ is the neighbourhood size of hopscotch hashing.

## Choosing a method

- For a general in-memory map, use open addressing with linear probing or a Swiss table, keep $\alpha$ at most about $1/2$ to $7/8$ depending on the scheme, and double when it is passed.
- Use separate chaining when the keys are large or the records must not move, since a pointer to a record stays valid, or when the load cannot be controlled.
- When the keys come from users who might be hostile, seed the hash function at random, as Python and other languages now do, or use a universal family.
- When the worst-case search time matters, as in network hardware, use cuckoo hashing. When the set is fixed, use a perfect hash function, and a minimal one when space is tight.
- For a table on disk that grows without pauses, use linear hashing; use extendible hashing when a directory in memory is acceptable and each search must read only one bucket.
