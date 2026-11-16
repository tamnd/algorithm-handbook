## What to remember

- A problem is in NP when every yes-instance has a [certificate](/certificate/) of length polynomial in $|x|$ that a deterministic [polynomial-time verifier](/polynomial-time-verifier/) accepts, and no certificate makes it accept a no-instance. Only yes answers need short proofs. The complements of NP problems form coNP, and the tautology problem is [coNP-complete](/co-np-complete/).
- A problem $B$ is [NP-hard](/np-hard/) when $A \le_p B$ for every $A$ in NP, by Karp reductions: polynomial-time maps $f$ with $x \in A \iff f(x) \in B$. It is [NP-complete](/np-complete/) when it is also in NP. To prove hardness, reduce a known NP-complete problem *to* the new one, never the other way.
- If one NP-complete problem is in P, then P = NP. So "no polynomial-time algorithm" always means "none unless P = NP". Whether P = NP is open, and hardness is a statement about the worst case only.
- The [Cook-Levin theorem](/cook-levin-theorem/) writes a run of $T$ steps as a CNF formula with $O(T^2)$ variables and $O(T^3)$ clauses, which makes SAT NP-complete. [Karp's 21 problems](/karps-21-np-complete-problems/) and the [Garey-Johnson compendium](/garey-johnson-compendium/) grow from it by reductions.
- Encoding matters. A number $N$ takes about $\lg N$ bits in binary and $N$ symbols in [unary](/unary-encoding/). An algorithm in time polynomial in the input length and the largest number, such as the $O(nt)$ [subset sum](/subset-sum-problem/) table, runs in [pseudo-polynomial time](/pseudo-polynomial-time/). It is not polynomial in the binary length.
- [Weakly NP-hard](/weak-np-hardness/) problems, such as subset sum, [partition](/partition-problem/) and knapsack, have pseudo-polynomial algorithms. [Strongly NP-hard](/strong-np-hardness/) problems stay NP-hard when every number is bounded by a polynomial in the length, so they have no pseudo-polynomial algorithm unless P = NP. Problems without numbers, such as [three-dimensional matching](/three-dimensional-matching/), are strongly NP-complete as soon as they are NP-complete.
- Small changes cross the line. Bipartite matching is in P and 3DM is NP-complete. Exact cover by 3-sets is in P with at most two occurrences of each element and NP-complete with exactly three. [Scheduling with release times and deadlines](/scheduling-with-release-times-and-deadlines/) is strongly NP-complete, but it is in P with preemption. These boundaries hold unless P = NP.
- If P ≠ NP, NP is not split into P and the NP-complete problems: [Ladner's theorem](/ladners-theorem/) gives problems strictly between them. By [Mahaney's theorem](/mahaneys-theorem/), a sparse NP-hard set under Karp reductions would give P = NP.

## The main problems side by side

| Problem | Hardness | Pseudo-polynomial algorithm | Exact algorithm from the entries | A case in P |
|---|---|---|---|---|
| [SAT](/sat/) | NP-complete (Cook-Levin) | no numbers | [DPLL](/dpll/), [CDCL](/cdcl/), exponential worst case | [2-SAT](/2-sat/), [Horn-SAT](/horn-sat/) |
| [Subset sum](/subset-sum-problem/) | NP-complete, weak | $O(nt)$ | $O(2^{n/2} n)$ by [Horowitz-Sahni](/horowitz-sahni-algorithm/) | $t$ polynomial in $n$ |
| [Partition](/partition-problem/) | NP-complete, weak | $O(nA)$, $A = \sum a_i$ | $O(2^{n/2} n)$ by meet in the middle | unary input |
| [3DM](/three-dimensional-matching/) | NP-complete, strong | no numbers | $O^*(4^q)$ over subsets | two dimensions ([bipartite matching](/bipartite-matching/)) |
| [X3C](/exact-cover-by-3-sets/) | NP-complete, strong | no numbers | $O^*(2^{3q})$ over subsets | at most two occurrences of each element |
| [Release times and deadlines](/scheduling-with-release-times-and-deadlines/) | NP-complete, strong | none unless P = NP | $O(2^n n)$ over subsets | preemption ([EDF](/earliest-deadline-first/)), equal lengths |

: Problems of the chapter. Times are worst-case bounds on a word RAM, as the entries give them. Every "NP-complete" row means that no polynomial-time algorithm exists unless P = NP. Subset sum also has a randomized $\tilde O(n + t)$ algorithm (Bringmann 2017).

## Using the chapter

When you meet a new problem and suspect it is hard:

- First write it as a decision problem and show that it is in NP. Name the certificate and the time to check it.
- Then pick a source problem that looks like it. Use 3-SAT for logic and choices, 3DM or X3C for packing and covering, partition or subset sum for numbers, and the [compendium](/garey-johnson-compendium/) for anything else. Reduce from the source to your problem. Check both directions of the "if and only if", and check that the map takes polynomial time.
- If the problem has numbers, ask whether it is strongly or weakly hard. A reduction from partition or subset sum proves ordinary NP-hardness only, not strong hardness. In that case a dynamic program over the numbers, or an [FPTAS](/fptas/), may still be practical.
- A hardness proof does not say that your inputs are hard. SAT and integer programming solvers often solve large practical instances, but their speed is measured, not proved. Look for structure in your inputs, approximation algorithms with proved ratios, or exponential algorithms with small bases.
