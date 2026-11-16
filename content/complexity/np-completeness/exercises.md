1. ◦ An instance of [subset sum](/subset-sum-problem/) has the numbers $5, 9, 14$ and the target $t = 23$. (a) How many symbols does the instance take when each of the four numbers is written in [unary](/unary-encoding/), with one separator between consecutive numbers? How many binary digits do the four numbers take, without separators? (b) Run the dynamic program that keeps the set of reachable sums, and give the set after each number. Is the answer yes?

2. ◦ For each problem, give a [certificate](/certificate/) for its yes-instances that a polynomial-time verifier can check, or say why none is known: (a) the graph has a [Hamiltonian cycle](/hamiltonian-cycle-problem/); (b) the graph has no Hamiltonian cycle; (c) the integer $N$, written in binary, is composite; (d) the integer $N$, written in binary, is prime.

3. ◦ True or false, with a one-line reason. (a) Every [NP-hard](/np-hard/) problem is in NP. (b) If some [NP-complete](/np-complete/) problem is in P, then P = NP. (c) If some NP-hard problem has a pseudo-polynomial algorithm, then P = NP. (d) [2-SAT](/2-sat/) is NP-complete. (e) A Karp reduction from a problem $A$ to [SAT](/sat/) proves that $A$ is NP-hard. (f) Since SAT is NP-complete, most CNF formulas are hard to decide.

4. ◦ Apply the reduction from [3-SAT](/3-sat/) to subset sum, as the subset sum entry gives it, to $\varphi = (x_1 \lor x_2 \lor \neg x_3) \land (\neg x_1 \lor \neg x_2 \lor x_3)$. Write the ten numbers and the target. Which numbers does the assignment $x_1 = x_2 = x_3 = 1$ select? How many subsets reach the target?

5. ◦ Subset sum has $n$ numbers, each at most the target $t$, written in binary. Classify each running time as polynomial, pseudo-polynomial but not polynomial, or neither: (a) $O(nt)$; (b) $O(n^2 \log t)$; (c) $O(2^{n/2} n)$; (d) $O(n t^2)$; (e) $O(t^{\lg t})$; (f) $\tilde O(\sqrt{n}\, t)$. Use the definition in [pseudo-polynomial time](/pseudo-polynomial-time/).

6. ◦ Use the reduction from subset sum to [partition](/partition-problem/) that adds the two numbers $2A - t$ and $A + t$, where $A$ is the sum of the numbers. Apply it to the numbers $4, 6, 9$ with $t = 13$, and then with $t = 12$. For each, write the partition instance and give a split into two equal halves, or show that there is none.

7. ◦ An instance of [three-dimensional matching](/three-dimensional-matching/) has $W = \{1, 2, 3\}$, $X = \{a, b, c\}$, $Y = \{x, y, z\}$ and the seven triples $(1, a, x)$, $(2, b, y)$, $(3, c, z)$, $(1, b, z)$, $(2, a, z)$, $(3, a, y)$, $(1, c, y)$. (a) Find a matching of size 3 and show that it is the only one. (b) Delete the triple $(3, c, z)$. Show that no matching of size 3 is left.

8. ◦ Two jobs share one machine: $J_1$ has length 4, release time 0 and deadline 10, and $J_2$ has length 2, release time 1 and deadline 3. (a) Without preemption, give all feasible integer start times, as in [scheduling with release times and deadlines](/scheduling-with-release-times-and-deadlines/). (b) Show that the rule "never leave the machine idle while a released job waits" fails here. (c) With preemption, give the schedule of [earliest deadline first](/earliest-deadline-first/).

9. ◦ A set of binary strings is sparse when it has at most $p(n)$ strings of length at most $n$, for some polynomial $p$. Which of these are sparse? (a) Strings with exactly three 1s. (b) Strings with as many 0s as 1s. (c) Binary representations of primes. (d) The strings $1^{2^k}$ for $k \ge 0$. (e) Encodings of satisfiable CNF formulas.

10. • Show that if P = NP, then every language in NP other than $\emptyset$ and $\{0,1\}^*$ is NP-complete under Karp reductions. Why are these two languages never NP-complete?

11. • You have a procedure that answers the decision question "does $G$ have a clique of size at least $k$?". Use it to find a [maximum clique](/maximum-clique/) of a graph with $n$ vertices. Bound the number of calls. See [optimization-to-decision reduction](/optimization-to-decision-reduction/).

12. • Two CNF formulas are equivalent when they have the same value under every assignment. Show that deciding whether two CNF formulas are equivalent is [coNP-complete](/co-np-complete/). Start from the fact that CNF unsatisfiability is coNP-complete.

13. • In zero-sum subset, the input is a list of integers of either sign, and the question is whether some nonempty sublist sums to 0. Prove that the problem is NP-complete, by a reduction from subset sum. Then give an algorithm that runs in time polynomial in $n$ and the largest absolute value of the input.

14. • Count the subsets of $(2, 3, 5, 7, 8, 10)$ with sum 15 by the [counting dynamic program](/counting-subset-sum/). Give the final table $c[0..15]$ and list the subsets. Why is this program pseudo-polynomial, and not polynomial?

15. • In the two-machine version of [makespan minimization](/makespan-minimization/), jobs have integer lengths, and the question is whether two identical machines can finish all of them by time $D$. (a) Show that this decision problem is NP-complete. (b) Run the [longest-processing-time-first](/longest-processing-time-first/) rule on the lengths $7, 5, 4, 4, 3, 3$ and compare its makespan with the optimum. (c) Give a pseudo-polynomial algorithm for the decision problem.

16. • In equal $k$-partition, the input is $n$ positive integers with sum $A$, and the question is whether they split into $k$ groups with sum $A/k$ each. (a) For a fixed $k$, give an algorithm that runs in time $O(n (A/k)^{k-1})$. (b) Show that when $k$ is part of the input, the problem is NP-complete in the strong sense. You may use that 3-partition is NP-complete in the strong sense, with $B/4 < a_i < B/2$ for all $i$.

17. • The greedy rule for three-dimensional matching scans the triples in a given order and keeps each one that is disjoint from all those kept before. Prove that it keeps at least a third as many triples as a maximum matching. Give an instance with four triples where it keeps only one triple and the maximum is 3.

18. • Fix an enumeration $\varphi_0, \varphi_1, \ldots$ of all CNF formulas in which $\varphi_n$ has $O(\log n)$ bits and can be computed from $n$ in time polynomial in $n$. Let $L = \{1^n : \varphi_n \text{ is satisfiable}\}$. Show that $L$ is in P. Explain why this does not contradict the NP-completeness of SAT.

19. • In the reduction from 3-SAT to three-dimensional matching as the entry on three-dimensional matching gives it, the formula has $n$ variables and $m$ clauses with three literals each. Count $q$ and the number of triples. Give both numbers for $n = 3$ and $m = 2$. Explain why the reduction needs exactly $m(n - 1)$ pairs of garbage elements.

20. • Classify each problem as in P or coNP-complete, and prove it: (a) satisfiability of DNF formulas; (b) whether a CNF formula is a tautology; (c) whether a DNF formula is a tautology. For the normal forms, see [conjunctive normal form](/conjunctive-normal-form/).

21. ★ Let FACTOR be the problem of deciding, for integers $N$ and $k$ in binary, whether $N$ has a divisor $d$ with $2 \le d \le k$. Show that FACTOR is in NP and in coNP. Use [Pratt certificates](/pratt-certificate/) or the [AKS test](/aks-primality-test/). What would it mean if FACTOR were NP-complete?

22. ★ HALF-CLIQUE asks whether a graph with $n$ vertices has a clique of size at least $n/2$, with $n$ even. Prove that it is NP-complete, by a reduction from the clique problem with the bound $k$ given in the input. Treat the cases $k \le n/2$ and $k > n/2$ separately.

23. ★ For the reduction from 3-SAT to three-dimensional matching, show that the number of perfect matchings of the instance is $(m(n-1))! \sum_a \prod_{j=1}^{m} t_j(a)$. Here the sum runs over the satisfying assignments $a$, and $t_j(a)$ is the number of true literals of clause $j$ under $a$. Evaluate it for $(x_1 \lor \neg x_2 \lor x_3) \land (\neg x_1 \lor x_2 \lor \neg x_3)$.

24. ★ Prove that the reduction from 3-partition to scheduling with release times and deadlines is correct: the jobs have a feasible schedule if and only if the numbers split into triples with sum $B$ each. Which direction uses the bounds $B/4 < a_i < B/2$? Explain why the transformation proves strong NP-completeness, while the reduction from partition does not.

25. ★ A set is tally when it is a subset of $1^*$. Prove that if some tally set $T$ is NP-hard under Karp reductions, then P = NP. Follow the self-reduction tree of SAT, and use the reduction from SAT to $T$ to prune it. This is Berman's theorem, a special case of [Mahaney's theorem](/mahaneys-theorem/).
