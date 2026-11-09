1. ◦ Insert the keys 27, 40, 13, 51, 62, 8, 35, 19, in this order, into a table of $m = 11$ slots with [linear probing](/linear-probing/) and $h(k) = k \bmod 11$. Show the final table. Count a probe for every slot examined, the empty slot that ends a failed search included. What is the average number of probes of a successful search for these keys? Of an unsuccessful search, averaged over the 11 home slots?

2. ◦ Insert the keys 12, 23, 5, 21, 30, 44, 8, 17 into a table of $m = 7$ slots with [separate chaining](/separate-chaining/), $h(k) = k \bmod 7$, and new keys at the end of their chain. Draw the chains. How many slots are empty? Counting the keys compared, what is the average cost of a successful search, and of an unsuccessful search averaged over the 7 slots?

3. ◦ Use [double hashing](/double-hashing/) with $m = 11$, $h_1(k) = k \bmod 11$ and $h_2(k) = 1 + (k \bmod 7)$. Insert 14, 25, 36, 3, 47 in this order. Where does each key go, and how many probes does each insert take? How many probes in all would linear probing take on the same keys?

4. ◦ Quadratic probing with the offsets $c(i) = i^2$ visits the slots $h(k) + i^2 \bmod m$. Take $m = 8$. Which slots can an insert with $h(k) = 0$ reach? Give a table with five empty slots in which this insert fails.

5. ◦ Take a load factor of $\alpha = 0.8$. How many probes does an unsuccessful search take on average under the [uniform hashing assumption](/uniform-hashing-assumption/), and a successful one? Answer the same two questions for linear probing, with Knuth's formulas.

6. ◦ [Multiplicative hashing](/multiplicative-hashing/) with $w = 16$, $\ell = 4$ and $a = 40503$ computes $h(k) = (ak \bmod 2^{16}) \gg 12$. Compute $h(1), \ldots, h(5)$.

7. ◦ A table starts with 16 slots and doubles when the number of keys passes $0.75$ times the number of slots, as Java's `HashMap` does. Insert 1000 distinct keys. How many times does the table double, and how many slots does it have at the end?

8. ◦ A group of the [Swiss table](/swiss-table/) holds 16 full slots, each with a 7-bit tag taken from the hash. A search for an absent key compares its tag with the 16 tags. If tags are uniform and independent, what is the expected number of false tag matches, and the probability of at least one?

9. ◦ Take the Carter–Wegman family $h_{a,b}(x) = ((ax + b) \bmod p) \bmod m$ of [universal hash functions](/universal-hash-family/) with $p = 13$ and $m = 4$. How many functions does it hold? Compute $h_{3,5}(10)$.

10. • Hash $n$ keys uniformly and independently into $m = 2^{16}$ slots. Find the smallest $n$ for which the probability of at least one [collision](/hash-collision/) is at least $1/2$. Compare it with $\sqrt{2m \ln 2}$.

11. • In [cuckoo hashing](/cuckoo-hashing/) take two tables of $r = 7$ cells, $h_1(k) = k \bmod 7$ and $h_2(k) = \lfloor k/7 \rfloor \bmod 7$, and ignore the test that grows the tables. Insert 29, 36, 30, 37 and then 1. Show both tables after each insert. How many keys does the insert of 1 move?

12. • With the hash functions of the previous exercise, give three keys whose insert must fail, whatever the order and however long the walk may run. Explain why.

13. • Six keys A, B, C, D, E, F have the home slots 2, 2, 3, 2, 4, 3 in a table of 10 slots. Insert them in this order with plain linear probing, and again with [Robin Hood hashing](/robin-hood-hashing/), where a key that has moved further from home takes the slot of a key that has moved less, and ties do not swap. Give the slot and the displacement of each key in both tables. Compare the largest and the total displacement.

14. • A table starts with 8 slots. Before an insert that would make $n > m/2$, it doubles $m$ and [rehashes](/rehashing/) the $n$ keys it holds. Insert 1000 distinct keys. How many times does it double, how many key moves do the rehashes make in all, and what is the final $m$?

15. • Under the uniform hashing assumption, an unsuccessful search in a table of $m$ slots and $i$ keys takes $(m+1)/(m-i+1)$ probes on average. Take $m = 10$ and $n = 8$. Give the exact cost of an unsuccessful search. Then find the exact average cost of a successful search, using the fact that a search for a key repeats the probes of its insert. Compare it with the bound $(1/\alpha)\ln(1/(1-\alpha))$.

16. • In double hashing with $m = 12$, which values of $h_2(k)$ in $\{1, \ldots, 11\}$ make the probe sequence visit every slot? For the other values, how many slots does the sequence visit?

17. • Let $a$ be uniform on $\{0, \ldots, 7\}$ and $h_a(x) = ax \bmod 8$. Find two keys $x \ne y$ in $\{0, \ldots, 7\}$ with $\Pr[h_a(x) = h_a(y)] = 1/2$. Is this family universal?

18. • [FKS perfect hashing](/fks-perfect-hashing/) stores $n = 8$ keys. The first level, with 8 buckets, puts $3, 1, 1, 0, 2, 0, 1, 0$ keys in the buckets. Is this first level accepted? How many second-level cells does it need in all? What is $E[\sum_j n_j^2]$ for a truly random first-level function with $n = m = 8$?

19. • An [extendible hashing](/extendible-hashing/) table has buckets of capacity $b = 2$ and indexes its directory by the low bits of the hash. It starts with global depth 0 and receives three keys with hash values 0, 32 and 16. What is the global depth at the end, and how many directory entries are there?

20. • A [linear hashing](/linear-hashing/) table starts with $N = 4$ buckets and has split six times. What are the level $L$, the split pointer $p$ and the number of buckets? In which buckets do the keys with hash values 25, 13 and 8 live?

21. • [Duplicate removal](/dedup/) needs $\Omega(n \log n)$ comparisons in the [comparison model](/comparison-model/), yet hashing does it in $O(n)$ expected time. Explain why this is not a contradiction.

22. • An attacker sends $2^{16}$ distinct keys that all have the same hash code. The table uses chaining and checks the whole chain for a duplicate before it adds a key. How many key comparisons do the inserts make in all? About how many would they make if each chain became a balanced search tree once it grew long, as Java 8 does?

23. • Keys and pointers each take one word, and you have $3n$ words for $n$ keys. Separate chaining spends one word per slot and two per key, so it gets $m = n$ slots. Linear probing gets $m = 3n$ slots. Compare the expected cost of a successful and of an unsuccessful search in the two tables.

24. ★ Show that in linear probing with no deletions, the set of occupied slots after $n$ inserts does not depend on the order in which the keys are inserted.

25. ★ Show that Robin Hood hashing and plain linear probing, given the same keys, occupy the same slots and have the same total displacement. So Robin Hood changes only how the displacement is shared among the keys.

26. ★ For linear probing, a successful search for a key repeats the probes of its insert. Assume the unsuccessful search at load $x$ costs $\frac12(1 + 1/(1-x)^2)$ probes, and average this over the inserts as the load grows from 0 to $\alpha$. Derive the cost $\frac12(1 + 1/(1-\alpha))$ of a successful search.

27. ★ The cuckoo graph has one vertex per cell and one edge $\{T_1[h_1(k)], T_2[h_2(k)]\}$ per key. Prove that a set of keys can be placed with one key per cell exactly when no connected component of the graph has more edges than vertices.

28. ★ Take double hashing with $m = 16$ and $h_2(k)$ odd. Show that different pairs $(h_1(k), h_2(k))$ give different probe sequences. How many distinct probe sequences are there? How many does linear probing have, and how many does the uniform hashing assumption allow?
