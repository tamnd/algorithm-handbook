1. ◦ Six processes on a one-way ring hold the identifiers 4, 1, 6, 3, 5, 2, and each sends to the next one in this list, the last to the first. Run Chang-Roberts. How many election messages are sent, how many messages in all with the announcement, and which identifier wins?

2. ◦ For Chang-Roberts on a one-way ring of $n = 6$ processes, give the largest and the smallest number of election messages over all orders of the identifiers 1 to 6, and the average over all $720$ orders as an exact fraction.

3. ◦ FloodMax runs on a $3 \times 3$ grid of processes. The identifiers, row by row, are 9, 1, 2 / 3, 4, 5 / 6, 7, 8. (a) With the diameter bound $d = 4$, how many rounds and how many messages does it take? (b) With $d = 3$, how many messages are sent, and how many processes end up believing that they are the leader?

4. ◦ Run Franklin's algorithm on the two-way ring 2, 9, 4, 7, 1, 8, 3, 6, where the last process is a neighbour of the first. List the candidates that survive each round, and give the number of election messages and the total with the announcement.

5. ◦ Hirschberg-Sinclair runs on a ring of $n = 12$ processes. How many phases does it have, what is the bound $8n \lceil \lg n \rceil - 2n$ on its election messages, and what is the time bound $2(2^L - 1) + n$ with $L = \lceil \lg n \rceil$?

6. ◦ Six processes 1 to 6 run the bully algorithm, and process 6 has crashed. Count as follows: every live process at or above the one that notices the crash sends ELECTION to every higher process, live or not; every live process answers OK to every ELECTION from a lower one; the winner sends COORDINATOR to every lower process. How many messages are sent if process 3 notices the crash, and how many if process 5 does?

7. ◦ Saturation runs on a tree of $n = 10$ processes, and $k = 3$ of them start on their own. How many WAKE messages, reports and announcements are sent? How many messages are sent in all if every process starts on its own?

8. ◦ In one round of Itai-Rodeh on a ring of $n = 4$, all four processes are active and each draws an identifier uniformly from $\{1, 2, 3, 4\}$. What is the probability that the largest draw is unique? Compare it with $(1 - 1/n)^n$.

9. ◦ Each network below is anonymous, with ports numbered at each process. For which of them can a deterministic algorithm elect a leader for every port numbering, and for which for no port numbering? (a) a path of 3 processes; (b) a path of 2 processes; (c) a star with 4 leaves; (d) a path of 5 processes; (e) an oriented ring of 6 processes.

10. ◦ TimeSlice runs on a synchronous ring of $n = 4$ processes with identifiers 7, 3, 12, 5. Which identifier wins, how many messages are sent, and after how many rounds is the election over?

11. • On a one-way ring of $n = 6$, how many of the $720$ orders of the identifiers 1 to 6 give the best case of Chang-Roberts? Over a random order, what is the expected number of hops of the message from the second-largest identifier, and of the message from the smallest one?

12. • On a two-way ring the identifiers $1, 2, \ldots, n$ appear in order round the ring. How many election messages does Franklin's algorithm send? How many does Chang-Roberts send if messages travel in the direction in which the identifiers increase, and how many if they travel the other way? Check your formulas at $n = 8$.

13. • Run Hirschberg-Sinclair on the ring 1, 2, ..., 8 in order. For each phase give the candidates, the probe messages and the reply messages, and give the total.

14. • Run Peterson's algorithm on the one-way ring 2, 9, 4, 7, 1, 8, 3, 6, with $p_0$ holding 2 and $p_i$ sending to $p_{i+1}$. How many messages are sent before a process receives its own value, and which process is the leader in Lynch's form? Then give the total for Dolev-Klawe-Rodeh, including the found message, and the process that becomes the leader there.

15. • Eight processes 1 to 8 run the bully algorithm with the counting rule of exercise 6. Processes 7 and 8 have crashed, and process 2 notices. Count the ELECTION, OK and COORDINATOR messages.

16. • Saturation runs on a star with a centre and 6 leaves, and only the centre starts on its own. Count the messages of each kind, check the total against $3n + k - 4$, and name the two saturated processes.

17. • OptFloodMax sends in a round only if its largest known identifier changed in the previous round, and every process sends in round 1. On a two-way ring of 6 processes with identifiers 1 to 6 in order round the ring and $d = 3$, how many messages does it send, and how many does FloodMax send?

18. • (a) Burns's bound for uniform asynchronous rings of size $n = 2^m$ is $T(n) = \frac{n}{4}(\log_2 n + 1)$ messages for finding the maximum and $T(n) - 2n$ for election. Evaluate both at $n = 16$, and find the smallest power of two for which the election bound is positive. (b) The Frederickson-Lynch bound says that a comparison-based synchronous algorithm sends more than $\frac{n}{4} H_{n/4}$ messages on a suitable ring of size $n = 2^m \ge 4$. What is the least number of messages it allows at $n = 16$?

19. • On a complete network of $n = 16$ processes, evaluate the all-to-all count $n(n-1)$, the Korach-Kutten-Moran bound $4 n H_n$, the Afek-Gafni bound $4n \lceil \log_2 n \rceil + n - 1$ and the bound $5n(\lfloor \log_2 n \rfloor + 1) + 6m + n - 1$ for the phased form of Awerbuch's algorithm. What is the smallest power of two at which the Afek-Gafni bound is below $n(n-1)$?

20. • A leader has been elected on a two-way ring that is not oriented, and the processes do not know $n$. Give a method by which the leader learns $n$ and every process learns which of its two ports points clockwise. How many messages does it use?

21. • FloodMax runs on a path of $n = 9$ processes with the diameter bound $d = 2$, below the true diameter 8. What is the largest number of processes that can end up as leaders, and which order of identifiers reaches it?

22. ★ The bit-reversal ring of size $n = 2^k$ places at position $i$ the number whose $k$-bit binary form is that of $i$ reversed. Show that Franklin's algorithm on it sends exactly $2nk + 2n$ election messages, so that its upper bound is reached for every power of two.

23. ★ Run Itai-Rodeh on a ring of $n = 3$. In each round every active process draws uniformly from $\{1, 2, 3\}$, the processes with the largest draw stay active, and the round is the last one if that draw is unique. Find the exact expected number of rounds. Do the same for $n = 2$ and compare both with the bound $(1 - 1/n)^{-n}$.

24. ★ Show that no deterministic algorithm on anonymous oriented synchronous rings lets every process output the ring size $n$, even when all processes start in the same round.

25. ★ Four anonymous processes $a, b, c, d$ form a path in this order. The two inner processes number their ports 1 and 2 in some way; the ends have one port each. Of the four possible port numberings, for which can a deterministic algorithm elect a leader?

26. ★ Find the largest number of election messages Hirschberg-Sinclair sends on a ring of 4 processes with identifiers 1 to 4, and say which of the 24 orders reach it.
