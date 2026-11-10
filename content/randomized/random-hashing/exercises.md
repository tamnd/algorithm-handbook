1. ◦ Use the [dot-product family](/dot-product-hashing/) with $p = 7$, $r = 3$ and $a = (3, 5, 1)$. Write the keys 50 and 100 as base-7 digit vectors and find their slots. Show that $h_a(100) = 2 h_a(50) \bmod 7$ for every $a$. For how many of the $343$ vectors $a$ do the two keys collide?

2. ◦ In the affine family $h_{a,b}(x) = (ax + b) \bmod 5$ with $a, b \in \{0, \ldots, 4\}$, find the one function with $h(1) = 2$ and $h(3) = 4$. Which function sends both 1 and 3 to slot 0?

3. ◦ Let $w = 8$, $\ell = 3$ and $a = 179$ in [multiply-shift hashing](/multiply-shift-hashing/). Compute $h_a(2)$, $h_a(3)$ and $h_a(128)$. Explain why $h_a(128) = 4$ for every odd $a$.

4. ◦ A chained table holds $n = 1000$ keys in $m = 500$ slots, with $h$ drawn from a universal family. Use the [expected chain length theorem](/universal-hashing-expected-chain-length/) to bound the expected chain length met by a search for an absent key and for a stored key, and the expected number of colliding pairs. What does the stored-key bound become with multiply-shift hashing?

5. ◦ A random polynomial of degree at most 2 over $\mathbb{Z}_7$, as in [k-independent hashing](/k-independent-hashing/), takes the values $1, 3, 2$ at the keys $0, 1, 2$. Find the polynomial and its value at 3. How many of the $7^3$ polynomials take these three values?

6. ◦ Draw a uniform random permutation $\pi$ of $\{0, \ldots, 7\}$. Let $A = \{0, 1, 2, 3\}$ and $B = \{2, 3, 4, 5, 6\}$. What is the probability that $\min \pi(A) = \min \pi(B)$? What number must divide the size of every exact [min-wise independent](/min-wise-independent-hashing/) family of permutations of these 8 keys?

7. ◦ Two-choice cuckoo hashing uses two tables of $r = 1000$ cells each and fully random hash functions. What does the [load threshold theorem](/cuckoo-hashing-load-threshold/) say for $n = 1100$ keys? For $n = 800$ keys, evaluate the failure bound of Pagh and Rodler, and compare it with the failure rate measured in the entry.

8. • Prove that a [pairwise independent](/pairwise-independence/) family of functions from $U$ to $[m]$, with $|U| \ge 2$, has at least $m^2$ members. Which family of the chapter has exactly $m^2$ members for $U = [m]$ when $m$ is a prime?

9. • A pairwise independent function maps $n = 10\,000$ keys into $m = 100$ slots. Let $X$ be the number of keys in slot 0. Find $E[X]$ and $\operatorname{Var}[X]$, and bound $\Pr[X \ge 200]$ with [Chebyshev's inequality](/chebyshev-inequality/). What does the [union bound](/union-bound/) over the 100 slots give for the event that some slot holds 200 keys or more?

10. • Take multiply-shift with $w = 4$ and $\ell = 2$. List the odd multipliers $a$ for which the keys 1 and 3 collide, and check that the collision probability equals the bound $2/m$.

11. • Let $n = m = 10^6$. Using the $k$-th moment bound of [k-independent hashing](/k-independent-hashing/), $\Pr[\text{some slot has at least } t \text{ keys}] \le (n/k!) / \binom{t}{k}$, find the least $t$ that makes the bound at most $1/2$, for $k = 2$ and for $k = 4$.

12. • The $20$ maps $x \mapsto (ax + b) \bmod 5$ with $a \ne 0$ are permutations of $\mathbb{Z}_5$. For $X = \{0, 1, 2\}$, compute the probability that each of $0$, $1$ and $2$ has the least value. What is the largest relative error $\big| |X| \Pr - 1 \big|$ among these three keys?

13. • Show that a min-wise independent multiset of 6 permutations of $\{0, 1, 2\}$ must contain each of the 6 permutations exactly once. (Use both the sets of size 3 and the sets of size 2.)

14. • A [MinHash](/minhash/) signature uses $k$ independent min-wise permutations and estimates the Jaccard similarity $J$ by the fraction of agreeing minima. For $J = 0.4$, how large must $k$ be for the standard deviation of the estimate to be at most $0.02$?

15. • Two cuckoo tables have $r = 4$ cells each. Six keys have the cell pairs $(T_1[h_1(x)], T_2[h_2(x)])$ equal to $(0, 0)$, $(0, 1)$, $(1, 1)$, $(1, 0)$, $(2, 2)$ and $(2, 0)$. Draw the cuckoo graph and give a placement. Then add a seventh key with cells $(2, 2)$. Show that no placement exists, although two cells are still empty.

16. • For a universal family with $m = n$ slots, show that $E\big[\sum_j L_j^2\big] \le 2n - 1$. Conclude that the two-level scheme of [FKS perfect hashing](/fks-perfect-hashing/), which gives slot $j$ a second table of $L_j^2$ cells, uses fewer than $4n$ second-level cells with probability more than $1/2$.

17. ★ Prove part 1 of the cuckoo threshold theorem with [Hall's theorem](/hall-theorem/): the keys can be placed exactly when every component of the cuckoo graph has at most as many edges as vertices.

18. ★ Cuckoo hashing with a stash of $s$ keys puts the keys that do not fit in a small extra list. Prove that the keys can be stored with a stash of size $s$ exactly when $\sum_C \max(0, e_C - v_C) \le s$, summed over the components $C$ of the cuckoo graph with $e_C$ edges and $v_C$ vertices.

19. ★ Let $X_1, \ldots, X_n$ be pairwise independent uniform bits on a finite probability space $\Omega$ in which every point has positive probability. Prove that $|\Omega| \ge n + 1$. Show that the construction of $2^k - 1$ bits from $k$ random bits in [pairwise independence](/pairwise-independence/) meets this bound.
