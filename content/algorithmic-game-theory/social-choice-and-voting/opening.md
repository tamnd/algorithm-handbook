An election with more than two candidates needs a rule. Each voter ranks the candidates, and the rule turns the rankings into a winner, or into one ranking of all candidates. The same problem appears outside politics: a search engine that merges the result lists of several systems, a panel that combines the orderings of its judges, and a sports league that ranks teams from the results of many races all aggregate rankings. Different rules can give different answers on the same ballots, and the choice matters.

With two candidates, majority rule is the natural answer. With three or more, majorities can cycle: a majority prefers $a$ to $b$, another prefers $b$ to $c$, and a third prefers $c$ to $a$. Every rule must then give up something. This chapter starts with two rules at opposite ends. The Borda count is fast and simple but can pass over a candidate whom a majority prefers to every rival. The Kemeny rule always respects such a candidate and has a clean definition as a median ranking, but computing it is NP-hard.

## What the chapter covers

The chapter has one group.

1. **Combining rankings.** The [Borda count](/borda-count/) gives $n$ points to the top of each list, $n - 1$ to the second, and so on, with an equal share for items missing from a partial list, and sorts by total points in $O(nk + n \log n)$ time. Its score equals a count of pairwise wins, it is monotone, and it never ranks a Condorcet loser first on full lists, but it is not Condorcet consistent and it is open to manipulation by strategic lists. [Kemeny rank aggregation](/kemeny-rank-aggregation/) finds the ranking with the smallest total Kendall tau distance to the inputs. The entry gives the pairwise form of the cost, an exact $O(2^n n^2)$ dynamic program, approximation algorithms with ratios 2, $11/7$ and $4/3$ and a PTAS, the NP-hardness results for few voters, and the link with weighted feedback arc set.

## A first reading

Read the [Borda count](/borda-count/) first, including the two examples: the merged search lists, and the five-voter profile where Borda and the Condorcet winner disagree. Then read [Kemeny rank aggregation](/kemeny-rank-aggregation/) through its examples and the section on known algorithms. The hardness results for few voters and the reductions can wait.

## Before you start

You need [rank aggregation](/rank-aggregation/) from Volume 35, the general problem that both entries solve, and the [Kendall tau distance](/kendall-tau-distance/) and [Spearman's footrule](/spearman-footrule/) from Volume 6. The hardness of Kemeny aggregation uses the [feedback arc set problem](/feedback-arc-set-problem/) of Volume 7 and the notion of an [NP-hard](/np-hard/) problem from Volume 39. The exact algorithm is a [bitmask DP](/bitmask-dp/) from Volume 2, and one approximation is an [assignment problem](/assignment-problem/) from Volume 7.

Most of the chapter is not written yet. The planned entries cover preference profiles and social welfare functions; Condorcet winners, the Condorcet paradox and the Smith set; plurality, approval, instant-runoff and single transferable vote, and the Copeland, Schulze, ranked pairs, Slater and Dodgson rules; the theorems of Arrow, Gibbard and Satterthwaite, May, and the median voter theorem with single-peaked preferences; manipulation, control and bribery; KwikSort; proportional representation in committees and participatory budgeting; and apportionment by the methods of Hamilton, D'Hondt, Sainte-Laguë and Huntington-Hill.
