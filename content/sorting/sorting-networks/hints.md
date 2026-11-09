1. The wires become $\langle 3, 4, 2, 1 \rangle$, $\langle 3, 4, 1, 2 \rangle$, $\langle 1, 4, 3, 2 \rangle$, $\langle 1, 2, 3, 4 \rangle$ and $\langle 1, 2, 3, 4 \rangle$. The first four comparators exchange; the last one, $[1{:}2]$, does not.

2. Size 9. The layers are $\{[0{:}1], [3{:}4]\}$, $\{[2{:}4]\}$, $\{[2{:}3], [1{:}4]\}$, $\{[0{:}3]\}$, $\{[0{:}2], [1{:}3]\}$ and $\{[1{:}2]\}$, so the depth is 6. It is not the smallest: $d(5) = 5$.

3. Only $\langle 1, 1, 1, 0 \rangle$ fails; it comes out as $\langle 1, 0, 1, 1 \rangle$. The input $\langle 4, 3, 2, 1 \rangle$ comes out as $\langle 2, 1, 3, 4 \rangle$.

5. After the first layer, $\langle 2, 4, 3, 1, 5, 6, 9, 7 \rangle$; after the second, $\langle 2, 1, 3, 4, 5, 6, 9, 7 \rangle$; after the third, $\langle 1, 2, 3, 4, 5, 6, 7, 9 \rangle$.

6. The even places hold $2, 6$ and $1, 4$, which merge to $1, 2, 4, 6$. The odd places hold $5, 8$ and $3, 7$, which merge to $3, 5, 7, 8$. Interleaving gives $\langle 1, 3, 2, 5, 4, 7, 6, 8 \rangle$, and the layer $[1{:}2], [3{:}4], [5{:}6]$ makes three exchanges and leaves $\langle 1, \ldots, 8 \rangle$.

7. (a) $2^6 - 6 - 1 = 57$. (b) $(3+1)(3+1) = 16$. (c) Bitonic sort has 240 comparators and odd-even merge sort 191; both have depth 15.

8. For $n = 3$ the two bounds give 2 and $\lceil \lg 6 \rceil / 1 = 3$, so the counting bound is tight. For $n = 12$ they give 4 and $\lceil \lg 12! \rceil / 6 = 29/6$, rounded up to 5, well below 8. Van Voorhis gives $s(13) \ge 39 + 4 = 43$.

9. Take the sorted input and exchange the items $i$ and $i + 1$. Every comparator other than $[i{:}i+1]$ sees two items already in order, so the network must contain $[i{:}i+1]$ to fix them.

10. Compare the pairs $[2i{:}2i+1]$, then find the minimum of the even wires and the maximum of the odd wires with chains of $n/2 - 1$ comparators each; the two chains run side by side, so the depth is $n/2$. The lower bound is the adversary argument for finding the minimum and the maximum together, since a network is a comparison algorithm.

13. Map each input $x$ to $x'$ with $x'_w = -x_{n-1-w}$. Running the mirror on $x'$ gives the negated and reversed output of the original on $x$.

14. A sorted 0-1 output with $m$ ones has its ones on wires $n - m$ to $n - 1$. Each comparator is a pair of gates, AND for the minimum and OR for the maximum; take wire 3 of an optimal network on 7 wires, which has 16 comparators.

15. Wires 4 and 5 first meet in $[4{:}5]$ of the first stage. In the merge of wires 4 to 7, the flip and the first half-cleaner touch wire 6 or 7 and are gone, so the next comparator on wires 4 and 5 is $[4{:}5]$ again. A comparator applied twice in a row does nothing the second time.

16. Use the zero-one principle with $m$ zeros. After the two sorts, the first half has $a$ zeros at its start and the second half $b = m - a$ zeros at its start. The comparator $[i{:}2m-1-i]$ meets two zeros only if $i < a$ and $2m-1-i < m + b$, which needs $a + b > m$; so each pair has at most one zero, and the comparator puts it on the first half. The depth is $\tfrac12 k(k+1) + 1$.

17. $[0{:}2], [0{:}1]$ fails only on $\langle 0, 1, 0 \rangle$, and $[0{:}2], [1{:}2]$ fails only on $\langle 1, 0, 1 \rangle$. Also $[1{:}2], [0{:}1]$ fails only on $\langle 1, 0, 0 \rangle$, and $[0{:}1], [1{:}2]$ only on $\langle 1, 1, 0 \rangle$. A test that skips one of the four inputs passes the network that fails only there.

18. An adjacent comparator removes at most one inversion, and the reversed input has $n(n-1)/2$.

19. Induction on the number of comparators. After the change, the network computes the old output with two wire names exchanged at every step from then on, so it outputs a fixed permutation of a sorted vector. A standard network leaves a sorted input unchanged, so the permutation is the identity.

20. By the zero-one principle, it suffices to sort every 0-1 input with $k$ ones. Order 0-1 vectors with $k$ ones by comparing the positions of their ones; adjacent comparators preserve this order, and the vector with all ones first is the smallest.

21. Follow the largest item from each input wire: the paths form a tree that ends at wire $n - 1$, so some path has at least $\lceil \lg n \rceil$ comparators. Fix $+\infty$ on that path's input; its comparators now route items without comparing them. Remove them and untangle with exercise 19.

22. Each filter layer compares wires $w$ and $w + 2^b$ for one bit $b$ that $w$ lacks, and later layers keep the order. A 0-1 input whose ones already form an up-set passes through unchanged. The count is the number of monotone Boolean functions of four variables.
