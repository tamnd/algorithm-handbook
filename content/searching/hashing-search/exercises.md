1. ◦ The keys come from $\{0, 1, \ldots, 10^6 - 1\}$. A set of them is stored either as a bit vector, the [direct-address table](/direct-address-table/) of a pure set, or as a sorted array of 4-byte keys. For which numbers $n$ of keys is the bit vector smaller? What does each cost for a membership test?

2. ◦ Let $S = \{10, 22, 37, 45\}$. Is $h(x) = x \bmod 4$ a [perfect hash function](/perfect-hash-function/) for $S$? What is the smallest $m$ for which $x \bmod m$ is perfect for $S$? Is $h(x) = (x \bmod 10) \bmod 4$ a [minimal perfect hash function](/minimal-perfect-hash-function/) for $S$?

3. ◦ A uniformly random function maps 5 keys to $m$ slots. What is the chance that it is perfect for $m = 10$, and for $m = 5$? A minimal perfect hash function for $10^9$ keys needs about $1.443$ bits per key. How many megabytes is that, and how does it compare with storing the keys as 64-bit integers?

4. ◦ A chained table has $m = 1000$ slots and $n = 3000$ keys, under [simple uniform hashing](/simple-uniform-hashing/). Using [expected search time with chaining](/chaining-expected-search-time/), give the expected number of keys examined by an unsuccessful search and its standard deviation, and the expected number examined by a successful search.

5. ◦ An open-addressing table is filled to load $\alpha = 0.8$. Give the expected number of probes of an unsuccessful and of a successful search under uniform hashing, from [expected probes in open addressing](/open-addressing-expected-probes/). Do the same for linear probing, whose costs are about $\frac{1}{2}(1 + 1/(1 - \alpha)^2)$ and $\frac{1}{2}(1 + 1/(1 - \alpha))$.

6. ◦ Insert the keys 23, 15, 34, 26, 3, 9, 20, in this order, into a table of $m = 11$ slots with linear probing and $h(k) = k \bmod 11$. Give the final table, the number of probes of each insertion, and the average number of probes of an unsuccessful search when the home slot is uniform over the 11 slots. Point out the [primary clustering](/primary-clustering/).

7. ◦ A table under linear hashing, a form of [dynamic hashing](/dynamic-hashing/), started with $m_0 = 4$ buckets. It is in the round that started with 8 buckets, and its split pointer is $p = 3$. How many buckets does it have? In which buckets are the keys with hash values 13, 22, 17 and 26?

8. ◦ A chess program uses [Zobrist hashing](/zobrist-hashing/) with one random word for each kind of piece of each colour on each square, and one word for the side to move. How many words does it need? How many XORs update the hash after a move that captures a piece?

9. • Under simple uniform hashing, $n$ keys go into $m$ slots. Find the expected number of empty slots. Evaluate it for $n = m = 1000$ and compare it with $m/e$.

10. • The chaining entry gives the tail bound $\Pr[L \ge t] \le (e\alpha/t)^t$ for the length $L$ of one chain. With $n = m = 10^6$ and a union bound over the slots, find the least $t$ for which the chance that some chain holds $t$ or more keys is below $10^{-6}$.

11. • Under uniform hashing a successful search costs about $(1/\alpha)\ln(1/(1 - \alpha))$ probes, and under linear probing about $\frac{1}{2}(1 + 1/(1 - \alpha))$. Find, for each, the largest load at which a successful search costs at most 2 probes on average.

12. • In an open-addressing table without deletions, keys never move. Show that a successful search for a key makes as many probes as its insertion did, and deduce that if an unsuccessful search at load $t$ costs $U(t)$, a successful search at load $\alpha$ costs about $(1/\alpha)\int_0^\alpha U(t)\,dt$. Derive the successful cost of linear probing from its unsuccessful cost $\frac{1}{2}(1 + 1/(1 - t)^2)$.

13. • The family $h_a(x) = (ax \bmod 11) \bmod 4$, for $a = 1, \ldots, 10$, maps $\{0, \ldots, 10\}$ to 4 slots. For how many values of $a$ do the keys 1 and 5 collide? Is the family universal in the sense of the [universal hashing lemma](/universal-hashing-lemma/)? What does the lemma still give for chains under this family?

14. • Delete the key 23 from the final table of Exercise 6. Show that simply emptying its slot makes a search for 34 fail. Then delete it by moving later keys of the run back, one at a time, and give the table that results. State the rule that decides whether a key may move into the hole.

15. • Quadratic probing with $h(k, i) = (k + i^2) \bmod 7$ has [secondary clustering](/secondary-clustering/). Which slots can a key with home slot 0 ever reach? Give four keys whose insertion makes the insertion of the key 7 fail, although three slots are empty. Why can a key reach at most $(m + 1)/2$ slots when $m$ is prime?

16. • A hash-and-displace construction builds a minimal perfect hash function for six keys in six slots. A first hash puts the keys into three buckets, and a key $x$ in bucket $B$ goes to slot $(f(x) + d_B) \bmod 6$. Bucket 0 holds three keys with $f$ values 0, 3 and 4, bucket 1 holds two keys with $f$ values 0 and 2, and bucket 2 holds one key with $f$ value 0. Place the buckets in order of decreasing size, giving each the least displacement $d_B$ that puts all its keys into free slots. What goes wrong if two keys of one bucket have the same $f$ value?

17. • Extendible hashing keeps a directory of $2^d$ pointers indexed by the first $d$ bits of the hash, and buckets of capacity 2. Three keys have hash values that begin with ten 0 bits, followed by 0, 1 and 1. What is the size of the directory after the three keys are inserted into an empty table? What does this say about the size of the directory as a function of $n$?

18. • A Zobrist hash of a set of items is the XOR of a random word for each item in the set. Show that it fails for a multiset in which items can appear several times. Fix it with one random word for each pair (item, count), and give the cost of adding or removing one copy of an item.

19. ★ A rolling hash of the last $w$ characters of a stream uses a random word $T[c]$ for each character $c$. Show that the plain XOR of the $T[c]$ in the window gives the same hash to any two windows that are anagrams. Fix it with cyclic rotations of the words, give an update that takes $O(1)$ time per new character, and say what goes wrong when $w$ is larger than the number of bits in a word.

20. ★ Zobrist hashing of a key made of $c$ characters, each with its own table of random words, is simple tabulation hashing. Give four keys of two characters whose hashes always XOR to 0, so that the scheme is not 4-wise independent. Then prove that it is 3-wise independent.

21. ★ Prove that in linear probing, without deletions, the set of occupied slots does not depend on the order in which the keys are inserted. Deduce that the cost of every later unsuccessful search does not depend on it either.

22. ★ A program maps every key of an $n$-set $S$ from a universe of size $u$ to a slot in $\{0, \ldots, n - 1\}$ given in advance for that key, for any $S$ and any such assignment. Show that, when $u$ is much larger than $n$, it needs about $n \lg n$ bits for some $S$ and assignment, against about $1.443\,n$ bits for a minimal perfect hash function.
