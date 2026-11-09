1. (a) Not linearizable, since enq$(x)$ ends before deq() starts; sequentially consistent, by the order deq(), enq$(x)$; not quiescently consistent, since a quiescent point lies between the two calls. (b) Not linearizable, since $B$ ends before $C$ starts but got the larger value; sequentially consistent and quiescently consistent, by the order $C$, $A$, $B$, which is allowed because $A$ is pending the whole time. (c) All three: the two enqueues overlap, so enq$(y)$ may come first.

2. $(0, 0)$, $(0, 1)$ and $(1, 1)$ are allowed. $(1, 0)$ is forbidden: if thread 2 reads $y = 1$, the write of $y$ came before, and the write of $x$ came before that in thread 1's order, so the later read of $x$ returns 1.

4. Locals $[2, 4, 2, 3]$, global 15, true count 26. An approximate read returns 15, an error of 11, below $p(S - 1) = 16$. The global lock was taken 3 times: once by core 0 and twice by core 2.

6. $rev$ gives $1;\ 2, 3;\ 4, 6, 5, 7;\ 8, 12, 10, 14, 9, 13, 11, 15$, so the 11th item goes to slot 14. The inserts use slots 1, 2, 3, 4 and 6 and leave slots 1 to 6 as $1, 6, 2, 8, -, 3$; slot 5 stays empty. The delete-min takes 3 from slot $rev(5) = 6$, puts it at the root, returns 1, and swaps 3 with the child 2. The slots are then $2, 6, 3, 8$.

7. The six tokens go to wires $0, 1, 2, 3, 0, 1$ and get $0, 1, 2, 3, 4, 5$. Then the toggles are 0 at the root and 1 at both children. Token 3 goes left and token 8 right; at the children the toggles send them to wires 2 and 3, values 6 and 7. Token 2 goes left twice, to wire 0, and gets 8.

9. $C$ returns 0, $D$ returns 1, $A$ returns 2 and $B$ returns 3. Each of $A$ and $C$ carries a batch of 2 to the root, so the root is changed twice for four increments. Linearize $C$ and $D$ at $C$'s root step, and $A$ and $B$ at $A$'s.

12. Enqueues $a$ to $d$ take tickets 0 to 3 and cells 0 to 3. The two dequeues take tickets 0 and 1, return $a$ and $b$, and move cells 0 and 1 to rounds 4 and 5. Enqueues $e$ and $f$ get tickets 4 and 5 and use cells 0 and 1. Enqueue $g$ gets ticket 6 and finds $c$ still in cell 2; since $6 - 2 \ge R$, it closes the ring and links a new ring with $g$ in cell 0. The dequeues return $c, d, e, f$ with tickets 2 to 5; ticket 6 finds cell 2 empty, kills it, sees tail $7 \le 7$ and reports empty, the drain uses ticket 7, and the head moves to the new ring, which returns $g$. The head counter of the first ring ends at 8.

15. First call: the pairs of heaps return 1, 1 and 2, so the expected rank is $4/3$. Second call: whatever the first call removed, the three pairs again give ranks 1, 2 and 1, so the expected rank is again $4/3$.

18. Cut $H$ at its quiescent points into epochs. A quiescent point of $H$ is one of each $H|o$, so the order $S_o$ for object $o$ lists the calls of $o$ epoch by epoch. Build $S$ epoch by epoch, and inside an epoch put the pieces of the $S_o$ one object after another. For sequential consistency the orders inside threads link calls on different objects and can form a cycle, as in the example of two queues.

19. Each thread writes its proposal to its own register and then calls getAndIncrement() once; the one that gets 0 decides its own proposal, the other decides the other's. If a thread gets 1, a call that returned 0 must exist and must have been invoked before this call returned, since otherwise a quiescent point would put it later; so its register was already written.

20. Number the tops $1, \ldots, c$ by rank. With two distinct choices, the rank is at least $r$ exactly when both choices lie in $\{r, \ldots, c\}$, which has probability $\binom{c - r + 1}{2} / \binom{c}{2}$. Sum over $r$ and use $\sum_{j} \binom{j}{2} = \binom{c + 1}{3}$.

21. Let the queue hold $x$. The dequeuer reads that $x$ has no successor, so the queue becomes empty and it must set tail to nil. The enqueuer links $y$ after $x$ and sets tail to $y$. If the dequeuer reads the next field of $x$ before the enqueuer links $y$, and writes nil to head and tail after the enqueuer is done, $y$ is lost.

22. One increment on one core, and then quiet: the local count is 1 and the global count 0, so the read returns 0. For $S = 1$ every increment moves its unit to the global count at line L5, under the global lock, so the read sees exactly the increments linearized before it.
