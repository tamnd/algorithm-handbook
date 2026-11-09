1. ◦ A $5 \times 7$ matrix of 4-byte entries starts at address 2000, and indices start at 0. Give the address of $A[3][4]$ in [row-major order](/row-major-order/) and in column-major order.

2. ◦ A [circular buffer](/circular-buffer/) has $N = 5$ cells and starts with $h = 0$ and $n = 0$. Enqueue 1, 2, 3, 4, 5, dequeue twice, then enqueue 6 and 7. Give the array, $h$ and $n$, and the value of GET$(B, 3)$. A variant keeps two indices, front and back, and no count. How many items can it hold with $N$ cells, and why?

3. ◦ A [dynamic array](/dynamic-array/) starts with $n = 0$ and $cap = 1$, doubles when full and halves when a pop leaves it a quarter full. After 17 appends, how many item copies have the resizes made in all, and what is $cap$? Then pop one item at a time. After how many pops does the first shrink happen, and what is $cap$ after it?

4. ◦ A [generalized queue](/generalized-queue/) receives insert $a, b, c, d, e, f$, then delete(2), delete(4), delete(1), insert $g$ and delete(3). Which items do the four deletes return, and what is left?

5. ◦ The nodes $A, B, C, D$ of an [XOR linked list](/xor-linked-list/) sit at the addresses 0x10, 0x20, 0x30 and 0x40, in this order from the front, and the null address is 0. Give the link field of each node.

6. ◦ Run [postfix evaluation](/postfix-evaluation/) on `6 2 3 + × 8 4 / −`. Give the stack after each token, the result and the largest height the stack reaches.

7. ◦ Convert `( a + b ) * c - d / e ^ f ^ g` to postfix with [the shunting-yard algorithm](/infix-to-postfix/), where `^` is right-associative and binds tighter than `*` and `/`.

8. ◦ Solve the [next greater element](/next-greater-element/) problem on $\langle 3, 8, 4, 1, 6, 2, 9, 5 \rangle$ with one left-to-right scan and a stack. Give the answers, the number of pops, and the values left on the stack at the end.

9. ◦ Run the sliding-window minimum of the [monotonic deque](/monotonic-deque/) on $\langle 5, 1, 4, 6, 2, 7, 3, 8 \rangle$ with window $k = 3$. Give the six outputs and the pairs (position, item) left in the deque at the end.

10. ◦ The list is $a, b, c, d, e$ and the requests are $c, c, e, a, e, b$, where an access at position $i$ costs $i$. Give the total cost of the [move-to-front heuristic](/move-to-front-heuristic/), of transpose (swap the item with the one before it) and of the list that never changes, and the final list of the first two.

11. ◦ Let $f(x) = (x^2 + 2) \bmod 13$ and $x_0 = 0$. Write out $x_0, \ldots, x_8$ and give $\mu$ and $\lambda$. After how many steps of the first phase of [Floyd's cycle detection](/floyd-cycle-detection/) do the tortoise and the hare meet, and at which value?

12. • How many postfix strings have the operands $a, b, c, d$ in this order and three copies of one binary operator $\circ$? List them, and give the count for $n$ operands in general.

13. • Requests are independent, with $p = (1/2, 1/3, 1/6)$ for three items. Compute the long-run expected cost of move-to-front, the cost $E_{\mathrm{OPT}}$ of the best fixed order and the bound $2 E_{\mathrm{OPT}} - 1$.

14. • Write a procedure that reverses a [singly linked list](/singly-linked-list/) in groups of $k$ nodes, the last group too even when it is shorter, in $O(n)$ time and $O(1)$ extra space. What does it give on $1, 2, \ldots, 8$ with $k = 3$?

15. • Two singly linked lists, of lengths $m$ and $n$, end in a common tail: from some node on, their nodes are the same. Find the first common node in $O(m + n)$ time and $O(1)$ extra space, without changing the lists.

16. • The span of day $i$ in a list of prices is the number of consecutive days ending at day $i$ whose price is at most the price of day $i$. Compute all spans in $\Theta(n)$ time with a [monotonic stack](/monotonic-stack/), and give them for $\langle 31, 41, 59, 26, 53, 58, 97, 93 \rangle$.

17. • For the $f$ and $x_0$ of Exercise 11, count the evaluations of $f$ made by Floyd's method to find $\mu$ and $\lambda$ (all three phases), and by [Brent's algorithm](/brent-cycle-detection/) as its entry gives it. How many does Brent's first part use?

18. • Put the keys 5, 3, 8, 1, 9, 2, in this order, into an empty [binary search symbol table](/binary-search-symbol-table/). How many keys does each put shift? Over all orders of $n$ distinct keys, which order makes the most shifts and how many?

19. • A [gap buffer](/gap-buffer/) has $cap = 8$ and holds ABCDEF with $g = 6$ and $e = 8$. Apply MOVE-TO(2), then insert X, Y and Z. Give $g$, $e$ and $cap$ at the end, the text held, and the number of items moved by MOVE-TO and GROW together.

20. • Push $1, 2, 3, 4$ onto a [stack](/stack/) in this order, with pops mixed in, and write down the popped items. Which of $4\,1\,2\,3$, $2\,4\,3\,1$, $3\,1\,2\,4$ and $1\,3\,2\,4$ can come out? How many of the 24 permutations can?

21. • Two [doubly linked lists](/doubly-linked-list/) each have a [sentinel node](/sentinel-node/) and are circular through it. Append all of the second list to the first in $O(1)$ time, leaving the second list empty. How many link fields change? What does the same task cost for two singly linked lists with a head pointer only?

22. • A log keeps the last $N = 1000$ events in a circular buffer that overwrites the oldest item when full. Events $1, 2, \ldots, 2500$ arrive, starting from $h = 0$. In which cell is event 2500, which event is the oldest kept, what is $h$, and how many writes overwrite an item?

23. • A [sparse vector](/sparse-vector/) stored as an array of (index, value) pairs sorted by index can compute a dot product by a merge. Give the merge, its cost, and the dot product of $u = \{2{:}\,3,\ 5{:}\,{-1},\ 9{:}\,4,\ 14{:}\,2\}$ and $w = \{1{:}\,7,\ 5{:}\,2,\ 9{:}\,1,\ 12{:}\,5,\ 14{:}\,{-3}\}$.

24. ★ In an XOR linked list you hold the addresses of four nodes $p, a, b, q$, where $a \ldots b$ is a run of the list, $p$ comes just before $a$ and $q$ just after $b$. Reverse the run in $O(1)$ time, whatever its length. Which fields change, and by what?

25. ★ Build a [deque](/deque/) from two stacks (and a third for scratch) so that every operation costs $O(1)$ amortized. Prove the bound with a potential function.

26. ★ The rule COUNT of a [self-organizing list](/self-organizing-list/) keeps the items in order of access count. Start from $x_1, \ldots, x_n$ with equal counts and request $x_1$ $kn$ times, then $x_2$ $k(n-1)$ times, and so on down to $x_n$ $k$ times. Find the exact cost of COUNT and of move-to-front, and conclude that COUNT is not $c$-competitive for any constant $c$.

27. ★ Store a resizable array in blocks of sizes $1, 2, 3, \ldots$, with an index of pointers to the blocks. Show that $n$ items use $n + O(\sqrt{n})$ cells, give the block and the offset of item $i$ by a formula, and show that append costs $O(1)$ amortized.

28. ★ A structure supports insert, find-min and delete-min on items that can only be compared. Show that the three cannot all cost $O(1)$ amortized. A [stack with minimum](/min-stack/) has push, pop and min in $O(1)$: say exactly why it does not contradict this.

29. ★ Prove that the first phase of Floyd's method stops after $\nu$ steps, where $\nu$ is the least multiple of $\lambda$ with $\nu \ge \max(\mu, 1)$, and that $\nu \le \mu + \lambda$. Then prove that the second phase takes exactly $\mu$ steps.
