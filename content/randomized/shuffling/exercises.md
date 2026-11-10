1. ◦ Run the [Fisher-Yates shuffle](/fisher-yates-shuffle/) on $[a, b, c, d, e]$ with the calls of line L2 returning $j = 2, 0, 2, 1$ for $i = 4, 3, 2, 1$. Show the array after each swap. Then find the choices that give the reversed order $[e, d, c, b, a]$.

2. ◦ How many equally likely runs does the [naive shuffle](/naive-shuffle/) have on four items, and how many does Fisher-Yates have? A third loop runs $i$ from 1 to $n - 1$ and draws $j$ from $\{0, \ldots, n-1\}$. Count its runs for $n = 4$ and say whether it can be uniform.

3. ◦ Run [Sattolo's algorithm](/sattolo-algorithm/) on $[0, 1, 2, 3]$ with $j = 0, 1, 0$ for $i = 3, 2, 1$. Write the result as a single cycle.

4. ◦ How many out-shuffles return a 14-card deck to its starting order under the [faro shuffle](/faro-shuffle/)? How many in-shuffles? In an 8-card deck, which shuffles move the top card to position 5, counting from 0?

5. ◦ [Permute by sorting](/permute-by-sorting/) draws $n = 5$ keys from a range of size $M = n^3 = 125$. Bound the probability of a tie with the union bound, then compute it exactly.

6. ◦ Insertion sort runs with a comparator that answers "smaller" or "larger" by a fair coin, as in the [sort-based shuffle](/sort-based-shuffle/). Find the probability that the last input item ends up first. Compare it with $1/n$ for $n = 10$.

7. ◦ How many [derangements](/derangement/) of 4 items are there? A program draws uniform permutations until it gets a derangement; how many draws does it make on average? With what probability does Sattolo's algorithm give each derangement of 4 items?

8. ◦ For the [top-to-random shuffle](/top-to-random-shuffle/) on 3 cards, find the total variation distance to uniform after one move, and the mean of the strong uniform time $T$. What is $E[T]$ for 10 cards?

9. ◦ One shuffle of the [Gilbert-Shannon-Reeds model](/gilbert-shannon-reeds-model/) acts on 5 cards in order. What is the probability that they stay in order, and how many orders can it reach? Count the rising sequences of the 7-card order $[3, 0, 4, 1, 5, 2, 6]$ and find its probability after two shuffles of the sorted deck.

10. ◦ Broder's rule gives a [strong uniform time](/strong-uniform-time/) for the [random transposition shuffle](/random-transposition-shuffle/) with mean $\frac{2n^2}{n+1} H_n$. Evaluate it for $n = 3$ and for $n = 52$, and compare the second value with the mixing time of about 103 moves.

11. • Prove the inside-out form of Fisher-Yates correct. Show that after the step for $i$, the map from (the order of $B[0 \ldots i-1]$, the choice $j$) to the order of $B[0 \ldots i]$ is a bijection, and conclude by induction.

12. • Give a version of the partial Fisher-Yates shuffle that returns a uniform $k$-permutation of $\{0, \ldots, n-1\}$ in $O(k)$ expected time and $O(k)$ space, without an array of size $n$. Use a [hash table](/hash-table/) that stores only the positions that have changed.

13. • Find the expected number of steps of Fisher-Yates in which $j \ne i$, so that the swap moves something. Evaluate it for $n = 52$.

14. • A machine has 4-bit random words, and Fisher-Yates on 3 items draws $j$ as `word mod (i + 1)`. Find the probability of each of the six orders and the total variation distance to uniform.

15. • A merge of two shuffled lists of two items each takes the next item from the left or the right by a fair coin while both are non-empty. Find the probability of each of the six left-right patterns, and the total variation distance from the uniform law over the patterns. Then show that taking the left item with probability $\ell/(\ell + r)$, as in [shuffling a linked list](/shuffling-a-linked-list/), makes all six patterns equally likely.

16. • [MergeShuffle](/merge-shuffle/) merges two halves of two items each with fair coins and stops when a coin chooses an empty half; the $R$ items left are placed by inside-out Fisher-Yates. Find $E[R]$ and $\Pr[R = 0]$.

17. • Permute by sorting runs on two items with a [stable sort](/stable-sort/) and $M$ key values, but does not redraw on a tie. Find the probability that the items keep their order. How large must $M$ be for the bias to be at most $10^{-6}$?

18. • Prove that 26 in-shuffles reverse a deck of 52 cards. Use the 1-based map $q \mapsto 2q \bmod 53$ and the [multiplicative order](/multiplicative-order/) of 2 modulo 53.

19. • A shuffle that has $m$ possible moves reaches at most $m^t$ orders in $t$ moves, so $d(t) \ge 1 - m^t/n!$, as shown in [card shuffling](/card-shuffling/). Use this bound to find the number of top-to-random moves for 52 cards below which $d(t) \ge \frac12$.

20. • The random-to-top shuffle takes a uniformly random card and puts it on top. Prove that after $t$ moves its distance to uniform is the same as that of top-to-random.

21. • Use the Bayer-Diaconis formula to find the total variation distance to uniform after one and after two riffles of 3 cards.

22. • In the random transposition shuffle, each move picks positions $L$ and $R$ independently and uniformly and swaps them. Find the expected number of positions never touched in $t$ moves, and evaluate it for $n = t = 52$. Then show that it is at least $e^{2c}$ when $t = \frac12 (n-1) \ln n - c(n-1)$, using $\ln(1 - 1/n) \ge -1/(n-1)$.

23. ★ Show that the number of [cycles](/permutation-cycles/) of a uniform random permutation of $n$ items is a sum of independent Bernoulli variables with means $1, \frac12, \ldots, \frac1n$. Deduce its mean $H_n$ and its variance $H_n - \sum_{i=1}^n 1/i^2$, and check the variance for $n = 3$ by listing the six permutations.

24. ★ The separation distance of a shuffle after $k$ steps is $s(k) = \max_\sigma (1 - n!\, P^k(\sigma))$. Show that $k$ riffles in the GSR model have $s(k) = 1 - \prod_{i=0}^{n-1} (1 - i/2^k)$. Find the first $k$ with $s(k) < \frac12$ for $n = 52$ and for $n = 104$, and show that this $k$ is about $2 \log_2 n - \log_2(2 \ln 2)$.

25. ★ After four riffles a deck has at most 16 rising sequences. Use this to prove a lower bound on $d(4)$ for 52 cards in terms of the number of rising sequences of a uniform permutation, and compute it with the [Eulerian numbers](/eulerian-numbers/). Compare it with the counting bound $d(4) \ge 1 - 2^{-17}$.

26. ★ The bijection behind Fisher-Yates gives a ranking of permutations. Write an [unranking](/permutation-unranking/) algorithm that maps $r \in \{0, \ldots, n! - 1\}$ to a permutation in $O(n)$ arithmetic operations, by swapping $\pi[n-1]$ with $\pi[r \bmod n]$ and recursing on $\lfloor r/n \rfloor$. Then write the inverse ranking algorithm in $O(n)$ time, using an inverse array.

27. ★ Show that the number of rising sequences of a uniform random permutation of $n \ge 2$ items has mean $\frac{n+1}{2}$ and variance $\frac{n+1}{12}$. Relate rising sequences to the descents of the inverse permutation, and find the covariance of two adjacent descent indicators.
