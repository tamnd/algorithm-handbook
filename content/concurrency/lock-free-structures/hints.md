1. 6 end at 4, 32 at 3 and 32 at 2. It never ends below 2. Every write stores a value read plus one, so every written value is at least 1. Take the thread that makes the last write: its second read comes after its own first write, so it reads at least 1 and writes at least 2. With CAS, a write happens only if the counter still holds the value read, so each of the four successful CAS steps adds exactly 1.

3. H1 is linearizable in the order enq(x), enq(y), deq returning x, deq returning y. H2 is not: enq(x) ends before enq(y) starts, so x is ahead of y, but y is dequeued over $[3, 4]$, and x is still in the queue until time 6 at the earliest.

5. seq $= [5, 5, 3, 4]$, enqPos $= 5$, deqPos $= 2$. enq(f) has position 5, finds seq $= 5$ in cell 1, and returns OK. enq(g) has position 6, finds seq $= 3$ in cell 2, so $d = -3 < 0$ and it returns FULL. The queue holds c, d, e and f.

8. The SEARCH of insert(9) passes node 7 because its next pointer is marked, so right is tail and leftNext is 7. Its CAS(3.next, 7, tail) succeeds and unlinks 7. Then INSERT makes CAS(3.next, tail, n9), which succeeds. The list is head, 3, 9, tail. The CAS of delete(7) in line L18 fails, since 3.next is now node 9. Its SEARCH(7) finds 3 and 9 already adjacent and changes nothing. delete(7) returns true.

10. A CAS fails only if another thread's CAS succeeded between this thread's read and its CAS, and after a failure the thread reads again. Order the threads by the time of their successful CAS. The $i$-th can fail only because of the $i - 1$ successes before its own, each at most once, so it makes at most $i$ attempts. Sum over $i$. For the schedule, let all remaining threads read, let one succeed, and let all the others fail.

11. Let a dequeue read Head and Tail, both the dummy D, and then read D.next as NULL in line L13. Now run a whole enqueue of x. The dequeue resumes: Head is still D in line L14, and its local copies give $h = t$ in line L15 and nx $=$ NULL in line L16. It returns EMPTY although x was enqueued before the return.

14. Token A passes the balancer to wire 0 and stalls before it takes a value. Token B goes to wire 1, takes 1 and returns. Token C starts after that, goes to wire 0 and takes 0. A then takes 2. C started after B ended but got the smaller value. In a quiescent state, $m$ tokens have passed and the wires got $\lceil m/2 \rceil$ and $\lfloor m/2 \rfloor$ of them, so the values handed out are exactly $0, \ldots, m - 1$.

16. With two threads, the first gets 0 and the second gets the other thread's bit. With three, thread 2 gets 3 after thread 0 then thread 1, and also after thread 1 then thread 0, so it cannot tell who went first. Additions commute, so Theorem B of the [read-modify-write](/read-modify-write/) entry applies to every FAA protocol.

19. Three pairs. The thief wins the CAS on top: the owner gets EMPTY and the thief gets x. The thief reads top and bottom before the owner's line L6 and then loses the CAS: the owner gets x and the thief gets ABORT. The owner finishes first: the owner gets x and the thief sees top $=$ bottom and gets EMPTY. In every case top $=$ bottom $= 6$ at the end.

21. With $N = 1$ the state "full, for the consumer of $pos$", seq $= pos + 1$, is the same as the state "free, for the producer of $pos + 1$", seq $= pos + 1$ too. So enq(b) claims the full cell, overwrites a, and sets seq to 2; enqPos $-$ deqPos becomes $2 > N$. The deq at position 0 sees $d = 2 - 1 = 1 > 0$, reads deqPos again, gets 0, and loops for ever. The three states $pos$, $pos + 1$ and $pos + N$ are distinct only when $N \ge 2$.

22. The owner's write of bottom $= 1$ in line L6 waits in its store buffer, and its read of top in line L7 returns 0. The thief still sees bottom $= 2$. It steals x0 with a CAS from 0 to 1, then x1 with a CAS from 1 to 2. The owner has $t = 0 < b = 1$, so it returns x1 in line L10 with no CAS. When the buffer drains, top $= 2$ and bottom $= 1$.

23. With increments of 1, each register only grows, so the sum read lies between the counter's value at the start of the read and at the end, and a counter that grows by 1 at a time held every value in between. For $n = 3$: the reader, thread 2, reads $c_0 = 0$; thread 0 adds 1; thread 1 adds 2; the reader reads $c_1 = 2$ and $c_2 = 0$ and returns 2. The counter went 0, 1, 3. A snapshot returns all the registers as they were at one moment.

24. The iterations do not overlap in time, and an iteration fails only if some register was written between its two reads in that iteration. So at most $k$ iterations fail, and each costs $2n$ reads. To reach the bound, make exactly one write between the two reads of one register in each of the first $k$ iterations. The bound grows with $k$, and nothing bounds $k$.

25. Let thread 0 scan. In iteration $i$, for $i = 1, \ldots, n - 1$, thread $i$ runs one whole update between its two reads of $R[i]$. In iteration $n$, thread 1 does so again; it has moved twice, and the scan returns the view of that second update. Each failed iteration must set exactly one new entry of moved, so at least $n$ updates are needed.
