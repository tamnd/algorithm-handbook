1. ◦ Two map tasks hold the documents "to be or not to be" and "to do is to be". Run [word count](/word-count/), with one pair per word and one byte per character of key and value. How many pairs and bytes does the shuffle carry without a [combiner](/combiner/), and with one combiner pass per map task? What is the reducer size $q$ in each case, and what is the output?

2. ◦ The key a has the values 2 and 3 at one map task and 3 and 4 at another. For each reduce function, say whether it can be used unchanged as a [combiner](/combiner/), and give the result with and without it: (a) the maximum, (b) the sum of the squares, (c) the number of distinct values. For the ones that fail, change the job so that a combiner works.

3. ◦ The keys $3, 14, 15, 9, 26, 5, 35, 8, 97, 32$ go to $R = 3$ reduce tasks. Give the task of each key under the range [partitioner](/partitioner/) with split points 10 and 30, so that $\pi(k)$ is the number of split points at most $k$, and under $\pi(k) = k \bmod 3$. Give the loads of the three tasks in each case, and say which partitioner gives sorted output when the tasks are read in order.

4. ◦ A job has 8 map tasks and 2 reduce tasks, and all the map tasks have finished. Worker B ran map tasks 2 and 6 and is running reduce task 0. Worker C has finished reduce task 1. Then B fails. Under [fault tolerance by re-execution](/fault-tolerance-by-recomputation/), which tasks run again, and why is reduce task 1 not one of them?

5. ◦ A [barrier](/barrier-synchronization/) for $p = 1000$ processes uses a combining tree, which takes $2\lceil \log_k p \rceil$ rounds with fan-in $k$. Find the rounds for $k = 2$, 10 and 32. How many rounds and how many messages does the dissemination barrier need for the same $p$?

6. ◦ Four BSP processors send these numbers of words in a superstep. P0 sends 3 to P1 and 1 to P2, and keeps 5 for itself. P1 sends 2 to P2 and 2 to P3. P2 sends 4 to P0. P3 sends 1 to each of P0, P1 and P2. Find the $h$ of this [h-relation](/h-relation/), the processor that sets it, the total $V$, and the cost of the [superstep](/superstep/) with $w = 100$, $g = 3$ and $L = 20$.

7. ◦ In the [BSP model](/bsp-model/) with $p = 32$, $g = 2$ and $L = 20$, find the cost of the direct broadcast of one word and of the tree broadcast. For $p = 32$, for which values of $L$ is the tree cheaper, as a function of $g$?

8. ◦ A Spark program computes `lines.flatMap(split).map(w -> (w, 1)).reduceByKey(+).filter(c >= 10).map(swap).groupByKey()`. Which dependencies of these [resilient distributed datasets](/resilient-distributed-datasets/) are wide, how many stages does the scheduler make, and which transformations run in each stage?

9. ◦ In the [MRC model](/mrc-model/), $n = 10^{12}$ numbers are summed by a tree of partial sums, and each machine adds up at most $s$ numbers in a round. How many rounds are needed for $s = 10^4$ and for $s = 10^6$? Write each $s$ as $n^{1 - \epsilon}$ and check the count against $\lceil 1/(1 - \epsilon) \rceil$.

10. • A job has ten keys with the counts $50, 30, 25, 20, 20, 15, 10, 10, 10, 10$ and $R = 3$ reduce tasks. Find the lower bound $\max(N/R, c_{\max})$ of [data skew](/data-skew/). Find the largest load of [list scheduling](/list-scheduling/) when the keys come in increasing order of count, and when they come in decreasing order, breaking ties by the lowest task number. Show that no assignment that keeps keys whole has a largest load below 70.

11. • A job sends $N = 10^6$ pairs to $R = 50$ reduce tasks. One key has $c = 200{,}000$ pairs, and the other pairs spread evenly over the tasks. Find the largest load and the best speedup over one task. With salting into $S$ salts, each salted key on its own task, find the smallest $S$ that brings the largest load of the first round down to $N/R$, and the number of extra pairs in the second round. What does a combiner on each of $M = 100$ map tasks give instead?

12. • In [distributed sorting](/distributed-sorting/) with $R = 3$ and $a = 4$, the sample is $41, 7, 88, 23, 65, 12, 90, 34, 56, 71, 3, 49$. Find the split points $y_j = S[ja]$ and the task of each of the keys $5, 18, 23, 40, 41, 55, 60, 70, 72, 95$. Then find the $a$ that the sample-size theorem asks for with $n = 10^8$, $R = 100$, $\varepsilon = 0.2$ and $\delta = 0.05$, the sample size, and the promised largest bucket.

13. • Run [sorting by regular sampling](/parallel-sorting-by-regular-sampling/) on $p = 3$ processors that hold $[4, 9, 13, 1, 17, 6]$, $[2, 11, 15, 8, 3, 18]$ and $[5, 7, 10, 12, 14, 16]$. Give the samples, the splitters, the size of each bucket and the $h$ of the third superstep. Compare the largest bucket with the bound $2m - m/p - p + 1$.

14. • Six processes run the dissemination [barrier](/barrier-synchronization/). Give the partners of process 0 in each round and the set of processes it knows of after each round. If the processes arrive at the times $0, 0, 0, 0, 0, 7$ and each message takes one time unit, when does each process leave? How many messages are sent?

15. • A [map-side join](/map-side-join/) copies a relation of $s = 2{,}000$ tuples to every map task, and the large relation has $r = 200{,}000$ tuples. Compare its communication with that of the [reduce-side join](/reduce-side-join/) for $M = 50$ and $M = 150$ map tasks. For which $M$ are they equal?

16. • In [iterative MapReduce](/iterative-mapreduce/), how many rounds does PageRank with $\alpha = 0.9$ need for an error of $\epsilon = 0.01$, and for $\epsilon = 10^{-4}$? The minimum-label method for connected components runs on the path $4 - 1 - 5 - 3 - 0 - 6 - 2 - 7$, with $n + 2m$ records per round. After which round are the labels final, after which round does the driver stop, and how many records are sent in all?

17. • Run the shortest-path program of the [Pregel model](/pregel-model/) from vertex 0 on the edges $0 \to 1$ (weight 1), $0 \to 2$ (5), $1 \to 2$ (1), $1 \to 3$ (6), $2 \to 3$ (1), $2 \to 4$ (7) and $3 \to 4$ (2), with no combiner. Give the values after each superstep, the number of messages sent in each, and the number of supersteps. Check the count against $S = H + 2$ and the messages against $(H + 1)m$.

18. • In the model of [speculative execution](/speculative-execution/), a job has $n = 50$ tasks, a task is slow with probability $\pi = 0.02$, and a slow task takes $s = 4$. Find the expected job time without backups and with backups. What is the expected number of slow tasks?

19. • The [Shares join](/hypercube-shares-join/) computes $R(A, B) \bowtie S(B, C) \bowtie T(C, D)$ with $r = 10^6$, $s = 2 \cdot 10^6$, $t = 4 \cdot 10^6$ and $k = 64$ reducers. Find the shares, which tuples are copied and how often, and the communication. Compare with the shares $x_B = x_C = 8$.

20. • In the [gather-apply-scatter model](/gas-model/), machine 0 holds the edges $\{0,1\}, \{0,2\}, \{1,2\}$, machine 1 holds $\{0,3\}, \{0,4\}, \{3,4\}$, and machine 2 holds $\{0,5\}, \{4,5\}$. Find $A(v)$ for each vertex, the replication factor, and the bound on the words sent in one iteration with all vertices active. What replication factor does a random placement of the 8 edges on $p = 3$ machines give in expectation, and what fraction of the edges crosses between machines in a random edge cut?

21. ★ In a combining tree [barrier](/barrier-synchronization/) for $p = 4096$, a node with fan-in $k$ handles its $k$ children one after another, so each of the $2\lceil \log_k p \rceil$ rounds takes $k$ time units. Find the integers $k$ that make the barrier fastest, and the time. Where is the minimum of the real function $k/\ln k$?

22. ★ Placing keys on reduce tasks in decreasing order of count gives at most $(4/3 - 1/(3R))$ times the best largest load. Show that the bound is tight: run the rule on the counts $3, 3, 2, 2, 2$ with $R = 2$ and on $5, 5, 4, 4, 3, 3, 3$ with $R = 3$, and give a family of counts for every $R$ with the ratio $(4R - 1)/(3R)$.

23. ★ The triangle $R(A, B) \bowtie S(B, C) \bowtie T(C, A)$ has $r = t = 10^6$ and $s = 8 \cdot 10^6$, and runs as a [Shares join](/hypercube-shares-join/) on $k = 1000$ reducers. Find the real shares and the communication. Then find the integer shares with product exactly 1000 that cost least, and compare both with the shares $10, 10, 10$.

24. ★ Strings of $b = 20$ bits must be paired at Hamming distance 1 in one round. Use the [lower bound](/mapreduce-communication-lower-bounds/) $r \ge b/\log_2 q$ for $q = 2^{10}$ and $q = 2^5$, and check that the splitting algorithm meets it, with the number of reducers. Then let $q$ be at most $2^8$. What does the bound give, and what is the least $r$ that the splitting algorithm reaches?

25. ★ Show that the median has no [combiner](/combiner/). (a) Give two jobs, each with two splits of three values, where every split has the same median and count in both jobs but the overall medians differ. (b) Show that for every value $x$ of a split $X$ of distinct values, some second split $Y$ makes $x$ the median of $X \cup Y$, so a combiner output that does not determine all of $X$ cannot be correct.
