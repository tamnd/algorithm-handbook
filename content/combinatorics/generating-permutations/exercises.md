1. ◦ Use Legendre's formula from the [factorial](/factorial/) entry to find how many zeros $1000!$ ends with in decimal, and the exponent of 2 in $20!$.

2. ◦ Apply the [lexicographic successor](/lexicographic-permutation-successor/) rule to $2\,5\,4\,3\,1$ and to the multiset permutation $3\,1\,4\,4\,2\,1$. For each, give the index $i$ where the first scan stops, the item exchanged with $a_i$, and the result.

3. ◦ Find the lexicographic rank, counting from 0, of $3\,5\,1\,4\,2$ among the permutations of $\{1, \ldots, 5\}$, and the permutation of rank 100. Use [permutation ranking](/permutation-ranking/) and [permutation unranking](/permutation-unranking/).

4. ◦ How many distinct words can be made from the letters of COMBINATORICS, using each letter as often as it appears? How many of them begin with C?

5. ◦ Write $4\,6\,1\,3\,8\,2\,7\,5$, in one-line notation with $\pi(1) = 4$, as a product of disjoint cycles. Give its cycle type, its sign and its order.

6. ◦ In the [Steinhaus-Johnson-Trotter](/steinhaus-johnson-trotter/) order for $n = 4$, value 4 moves at every step except steps 4, 8, 12, 16 and 20, where step $s$ goes from the $s$-th permutation of the list to the next one. Which value moves at each of these five steps? What is the last permutation of the list?

7. ◦ Count the [involutions](/generating-involutions/) of $\{1, \ldots, 8\}$ with exactly $k$ cycles of length 2, for $k = 0, 1, 2, 3, 4$. Check that the counts add up to $t_8$.

8. • A step of [next permutation](/next-permutation/) is one exchange followed by the reversal of a suffix of length $L$. Using the [sign](/permutation-sign/), find for which $L$ the step changes the sign. Of the 23 steps for $n = 4$, how many change the sign? Write down the sequence of the 24 signs.

9. • Show that in the Steinhaus-Johnson-Trotter order, value $m$ moves exactly $(m-1)\,(m-1)!$ times, for every $n \ge m$. Check that the moves add up to $n! - 1$.

10. • Join two permutations of $\{1, 2, 3\}$ by an edge when they differ by an exchange of neighbors. Draw the graph. How many lists of all six permutations, read from a first to a last element, move along an edge at each step? Then show that the six arrangements of the multiset $\{1, 1, 2, 2\}$ cannot be listed so that each step exchanges two neighbors with different values.

11. • Find the lexicographic rank, counting from 0, of $2\,3\,1\,2\,1$ among the 30 arrangements of the multiset $\{1, 1, 2, 2, 3\}$, and the arrangement of rank 20. Use the rank formula of [multiset permutations](/multiset-permutations/), not a list.

12. • A $k$-permutation of $\{1, \ldots, n\}$ is a sequence of $k$ distinct items. Adapt the lexicographic rank to $k$-permutations, and find the rank, counting from 0, of $(3, 1, 4)$ among the 60 3-permutations of $\{1, \ldots, 5\}$.

13. • How many permutations of $\{1, \ldots, 6\}$ have order exactly 6? How many of $\{1, \ldots, 7\}$? Use the count of permutations of a given cycle type from [permutation cycle decomposition](/permutation-cycle-decomposition/).

14. • Apply the fundamental bijection to the permutation of Exercise 5: write it in the standard representation, with the largest item first in each cycle and the cycles in increasing order of their first items, erase the parentheses, and count the left-to-right maxima of the result.

15. • The unrank function of Myrvold and Ruskey starts from the identity on $\{0, \ldots, n-1\}$, and for $m = n, n - 1, \ldots, 1$ it exchanges positions $m - 1$ and $r \bmod m$ and sets $r \leftarrow \lfloor r/m \rfloor$. Unrank $r = 13$ for $n = 4$. Then write the rank function that inverts it in $O(n)$ time.

16. • The [involution generator](/generating-involutions/) branches on the smallest free item: it is either a fixed point or paired with a larger free item. Let $N(n)$ be the number of nodes of its search tree, leaves included. Show that $N(0) = 1$, $N(1) = 2$ and $N(n) = 1 + N(n-1) + (n-1)\,N(n-2)$. Prove that $N(n) \le 3t_n - 1$, and compute $N(8)$.

17. ★ Let $\pi'$ be $\pi$ with the value $n$ removed, and let $p$ be the position of $n$ in $\pi$, counting from 0. Express the rank of $\pi$ in the Steinhaus-Johnson-Trotter order through the rank of $\pi'$ in the order for $n - 1$ and through $p$. Use your formula to rank $3\,5\,1\,4\,2$ and to unrank 100 for $n = 5$.

18. ★ For the multiset with $a$ copies of 1 and $b$ copies of 2, let $D(a, b)$ be the number of arrangements with an even number of [inversions](/inversion/) minus the number with an odd number. Show that $D(a, b) = 0$ when $a$ and $b$ are both odd, and $D(a, b) = \binom{\lfloor (a+b)/2 \rfloor}{\lfloor a/2 \rfloor}$ otherwise. Conclude that when $a, b \ge 2$ and not both are odd, no list of the arrangements exchanges two neighbors at each step.

19. ★ Let $z_2 = (2)$, and for $n \ge 3$ let $z_n$ be the sequence $z_{n-1}, n, z_{n-1}, n, \ldots, n, z_{n-1}$, with $n$ copies of $z_{n-1}$ and $n - 1$ copies of $n$. Start from $1\,2 \cdots n$, and for each number $k$ of $z_n$ in turn reverse the first $k$ items. Show that this visits each of the $n!$ permutations once. How long is $z_n$, and what is the last permutation?
