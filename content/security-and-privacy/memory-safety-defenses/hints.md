1. The chunk has $16 + 24 + 16 = 56$ bytes, $b = 16$, and the shadow of its seven granules is RZ, RZ, 0, 0, 5, RZ, RZ. The verdicts are: pass ($0 + 3 < 5$), error ($4 + 1 = 5 \ge 5$), pass ($4 < 5$), pass (shadow 0), error (redzone) and error (redzone).

2. $e = 6$, the block is $[128, 192)$ and 24 bytes are padding. $k = 63$ gives 191, in the block; $k = 64$ and $k = 71$ give 192 and 199, marked, since both are below $192 + 8 = 200$; $k = 72$ is an error; $k = -8$ gives 120, marked; $k = -9$ is an error. The store at 168 is not reported: it lies in the padding, which baggy bounds counts as part of the block.

4. The domain is $[12288, 16383]$. Address sandboxing gives 12388, 15904 and 16383. Segment matching traps on 100 ($100 \gg 12 = 0$) and on 20000 ($20000 \gg 12 = 4$) and lets 16383 through.

5. $t$ is 1 after the call of F, stays 1 at `setjmp`, becomes 2 and 3 at the calls of G and H, and RESTORE sets it back to 1. F's return pops $S[0] = r_1$, which matches, and leaves $t = 0$. Without RESTORE, $t = 3$ at F's return, the check compares $S[2] = r_3$ with $r_1$ and faults with a return address mismatch: a false alarm on a correct program.

7. The in-set of $B$ is $\{104, 108\}$. After the free, 104 holds 0, 108 still holds 5 because 5 is not in $[200, 208)$, and the global at 16 still holds 200. That last pointer stays dangling, because stores outside heap objects are not traced.

9. Fat pointers pass both loads, since the bounds are checked only at the access and 74 is in $[64, 80)$. Jones-Kelly checking turns $p + 20$ and $p + 30$ into ILLEGAL and reports an error at the next ADD, so both are false alarms. Baggy bounds marks 84, which is less than 8 bytes past the end; the next ADD recovers the reference address 76 and returns 74, and the load passes. It rejects 94 at once, which is a false alarm.

10. (a) Only SoftBound, whose FIELD narrows the bounds to `name`; the other two see one object. (b) Jones-Kelly checking (ADD gives ILLEGAL) and SoftBound; AddressSanitizer finds the address addressable. (c) None of the three. Lock-and-key checking reports it, because the new allocation has a different key, and so would a fat pointer with capability numbers.

13. Consecutive sites share a target, so the build joins all sites and targets into one class and $T^*(s_i) = \{t_1, \ldots, t_{m+1}\}$. The check accepts $m(m+1)$ pairs; for $m = 10$, that is 110 against 20.

17. Without renewal, $q$ distinct probes succeed with probability $q / 2^{16}$, so $q = 32768$. With renewal the probability is $1 - (1 - 2^{-16})^q$, which first reaches $1/2$ at $q = 45426$, close to $2^{16} \ln 2$.

20. Take a path $s = u_0, t_1, u_1, t_2, \ldots, t_j = x$ in the graph of allowed edges. Each edge $(u, t)$ is an allowed pair, so $\ell(t) = e(u)$, and along the path $e(u_0) = \ell(t_1) = e(u_1) = \cdots = \ell(x)$.

21. $m - 1$ copies: a second copy of each of $t_2, \ldots, t_m$ makes the allowed sets pairwise disjoint. If $s_{j-1}$ and $s_j$ shared one copy of $t_j$, they would be in one class, and $s_j$ would accept the copy of $t_{j-1}$ that $s_{j-1}$ uses, which the policy forbids; so each of the $m - 1$ shared targets needs two copies.

22. $B + 2^e$ is a multiple of 16, so a pointer in $[B + 2^e, B + 2^e + 8)$ is in the low half of its slot and moves to $[B + 2^e - 8, B + 2^e)$, inside the block because $2^e \ge 16$. A pointer in $[B - 8, B)$ is in the high half of the slot before $B$ and moves to $[B, B + 8)$. With a 9-byte window, $r = B + 2^e + 8$ is in the high half of its slot and moves to $B + 2^e + 16$, outside the block.

23. While allocation $A$ is live, its lock location is not free, so only ALLOC of $A$ has written it and it holds $A$'s key $\kappa$. After the free, it holds INVALID or the key of a later allocation, and every later key is larger than $\kappa$. With the wrapping counter, $\kappa$ comes back at the $(2^b - 1)$-th allocation after $A$, and a stale $p$ passes if that allocation also gets $A$'s lock location: 65535 allocations for $b = 16$.

24. The crashes for each byte are uniform on $\{0, \ldots, 255\}$, so the expected total $S$ is $7 \cdot 127.5 = 892.5$ and the maximum is 1785. $S$ has the same distribution as $1785 - S$, so $P(S \le 892) = P(S \ge 893) = 1/2$. Whole-word guessing with 893 attempts succeeds with probability $893 / 2^{56} \approx 1.24 \times 10^{-14}$. A fresh canary in each child makes the learned bytes worthless, and each attempt succeeds with probability $2^{-56}$ again.
