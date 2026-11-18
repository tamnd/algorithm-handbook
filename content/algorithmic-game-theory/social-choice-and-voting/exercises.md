1. ◦ Seven voters rank four candidates: three vote $a, b, d, c$, two vote $c, a, b, d$ and two vote $c, d, b, a$. Compute the [Borda count](/borda-count/) of each candidate and the Borda order.

2. ◦ For the profile of Exercise 1, write the six pairwise counts $w_{xy}$. Is there a Condorcet winner? A Condorcet loser? Where does Borda put each of them?

3. ◦ Compute the [Kendall tau distance](/kendall-tau-distance/) between the rankings $a, b, c, d, e$ and $c, a, e, b, d$ by listing the discordant pairs.

4. ◦ Five items $p, q, r, s, t$ appear in three partial lists: $(p, q, r)$, $(r, s)$ and $(q, p, t, s)$. Give each missing item its shared points as in the Borda count entry, and compute the totals. Check that every list hands out 15 points.

5. • Find the [Kemeny ranking](/kemeny-rank-aggregation/) of the profile of Exercise 1 and its cost, and prove that it is the only one by the lower bound $\sum_{\{x, y\}} \min(w_{xy}, w_{yx})$. What is the cost of the Borda order?

6. • In the profile of Exercise 1, Borda elects $a$. Show that one voter of the type $c, a, b, d$ can make $c$ the Borda winner by casting a different ballot, and give the new scores.

7. • Three voters rank $a, b, c, d$, then $b, c, d, a$, then $c, d, a, b$. Find the pairwise majorities and a majority cycle. Run KwikSort with the pivot always the first remaining item in alphabetical order, and compute the cost of its output. Then compute the Borda scores from the pairwise counts alone, by the pairwise form of the score.

8. • For the profile of Exercise 7, prove that $b, c, d, a$ is the only Kemeny ranking and that its cost is 6. Which of the three input rankings would the best-input method return?

9. ★ Split the items into two nonempty sets $X$ and $Y$ such that, for every $x \in X$ and $y \in Y$, a strict majority of the voters ranks $x$ above $y$. Prove that every Kemeny ranking puts all of $X$ above all of $Y$. Deduce that a Condorcet winner is first and a Condorcet loser is last in every Kemeny ranking.

10. ★ A tournament on $n$ items picks a direction for every pair. Prove that every tournament is the strict majority relation of some profile of $n(n-1)$ rankings. (This is McGarvey's theorem.)
