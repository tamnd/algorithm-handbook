1. ◦ Split $[0, 1]$ into four equal segments. Agent 1 has densities proportional to $(1, 2, 3, 2)$ on them and agent 2 to $(3, 1, 1, 3)$, each scaled so that the whole cake is worth 1. Run [divide and choose](/divide-and-choose/) with agent 1 as the cutter. Where is the cut, which piece does agent 2 take, and what is that piece worth to agent 2?

2. ◦ For $n = 6$ agents, how many Robertson-Webb queries does the [Dubins-Spanier moving knife](/dubins-spanier-moving-knife/) make? How many does the [Even-Paz algorithm](/even-paz-algorithm/) make, and how many of them are cuts? Between which two numbers does the count of the [last diminisher](/last-diminisher/) lie?

3. ◦ Split $[0, 1]$ into four equal segments, and let three agents have densities proportional to $(1, 2, 1, 0)$, $(0, 1, 1, 2)$ and $(2, 0, 1, 1)$. Run the Dubins-Spanier protocol with ties to the smaller index. Give each agent's piece and its value to its owner. Which agents envy whom?

4. ◦ Two agents value four goods $a, b, c, d$ at $(5, 4, 3, 1)$ and $(2, 3, 4, 6)$. Agent 1 gets $\{a\}$ and agent 2 gets $\{b, c, d\}$. Is the allocation envy-free, [EF1](/envy-freeness-up-to-one-good/), [EFX](/envy-freeness-up-to-any-good/)?

5. ◦ Three agents value six goods $a, \dots, f$ at $(6, 9, 2, 5, 1, 4)$, $(8, 7, 1, 3, 5, 2)$ and $(7, 3, 6, 2, 4, 1)$. Run [round-robin allocation](/round-robin-allocation/) in the order 1, 2, 3. Give the bundles and the full table of each agent's value for each bundle. Is the result envy-free? Is it EF1?

6. ◦ An agent values six goods at $7, 5, 4, 3, 2, 1$. What is its [maximin share](/maximin-share/) for $n = 3$? For $n = 2$?

7. ◦ Two tenants share a rent of 800 in the quasi-linear model of [rental harmony](/rental-harmony/). Tenant $a$ values rooms 1 and 2 at 500 and 300, tenant $b$ at 450 and 350. Which assignment can be envy-free? For that assignment, which prices $p_1$ of room 1 make it envy-free, and which one gives the two tenants equal utility?

8. ◦ An open necklace has the beads R R B R B B R B. Show that two thieves cannot share it fairly with one cut, and give a fair split with two cuts, as the [necklace splitting theorem](/necklace-splitting-theorem/) promises.

9. ◦ Two agents share five chores $a, \dots, e$ with costs $(4, 1, 3, 2, 5)$ and $(2, 3, 1, 4, 2)$. In round-robin for [chores](/chore-division/), each agent in turn takes its cheapest remaining chore, ties to the earlier letter, starting with agent 1. Give the bundles and their costs to both agents. Is the result envy-free? Is it envy-free up to one chore?

10. • Prove that for two agents and a division of the whole cake, a division is [proportional](/proportional-division/) exactly when it is [envy-free](/envy-freeness/). Show by an example that the two notions differ for three agents.

11. • Split $[0, 1]$ into four equal segments, and let four agents have densities proportional to $(1, 1, 2, 0)$, $(3, 1, 0, 0)$, $(0, 0, 1, 3)$ and $(1, 2, 1, 0)$. Run the Even-Paz algorithm as its entry gives it. Give the marks and the cut of each call, the final pieces with their values to their owners, and the number of cut and eval queries. Is the result envy-free?

12. • Split $[0, 1]$ into six equal segments. Agent 1 is uniform, agent 2 has densities proportional to $(4, 1, 1, 2, 1, 3)$ and agent 3 to $(1, 1, 4, 3, 1, 2)$. Run the [Selfridge-Conway procedure](/selfridge-conway-procedure/) with the conventions of its entry, ties to the leftmost piece. Give the trimmed piece, the trimmings, who cuts the trimmings, the final pieces and the $3 \times 3$ table of values. Check that the result is envy-free.

13. • Three agents value five goods $a, \dots, e$ at $(2, 5, 2, 4, 9)$, $(9, 8, 3, 6, 1)$ and $(4, 7, 9, 5, 8)$. Run [envy-cycle elimination](/envy-cycle-elimination/) with the goods in alphabetical order. Say when a rotation happens and along which cycle. Give the final bundles, and show that the result is EF1 but not envy-free.

14. • Two agents value four goods $a, b, c, d$ at $(5, 3, 2, 4)$ and $(6, 1, 4, 4)$. Run round-robin with agent 1 first and ties to the earlier letter. Show that the result is EF1 but not EFX.

15. • Two agents value four goods $a, b, c, d$ at $(4, 2, 1, 8)$ and $(2, 4, 1, 6)$. Find the [maximum Nash welfare allocation](/maximum-nash-welfare/) and its product, and show that it is unique. Is it envy-free, EF1, EFX?

16. • Two parties spread 100 points over five goods: party A gives $(35, 25, 25, 10, 5)$ and party B gives $(20, 30, 10, 25, 15)$. Run the [adjusted winner procedure](/adjusted-winner/). Which good is split, in what shares, and how many points does each party end with? How many points does A give to B's share?

17. • Three agents value six goods $a, \dots, f$ at $(6, 5, 4, 3, 2, 1)$, $(1, 2, 3, 4, 5, 6)$ and $(4, 4, 4, 2, 2, 2)$. Find the maximin share of each agent. Does round-robin in the order 1, 2, 3 give every agent at least its share?

18. • Three tenants share a rent of 1200 in the quasi-linear model. Their values for rooms 1, 2, 3 are $(600, 400, 300)$, $(500, 450, 300)$ and $(400, 400, 400)$. Find the maximum-weight assignment. Show that equal prices of 400 are not envy-free for it. Find the envy-free prices that maximize the smallest utility, and explain why no envy-free prices give a larger smallest utility.

19. • Agent 1 is uniform on $[0, 1]$. Agent 2 has densities proportional to $(0, 0, 1, 3)$ on the four quarters. Show that no [consensus halving](/consensus-halving/) uses one cut, and find every halving with two cuts.

20. • Three agents value four goods $a, b, c, d$ at $(6, 4, 3, 5)$, $(3, 3, 1, 2)$ and $(2, 1, 4, 5)$. The allocation $\{a\}$, $\{b\}$, $\{c, d\}$ has prices $(6, 4, 4, 5)$. Check the conditions used by the [Barman-Krishnamurthy-Vaish algorithm](/ef1-and-pareto-optimal-algorithm/): each agent holds only goods of maximum bang per buck, and the spending is EF1 in prices. Deduce from them, without searching, that the allocation is EF1 and Pareto optimal, and check EF1 directly.

21. ★ Prove the closed form $T(n) - n = 2n\lceil \lg n \rceil - 2^{\lceil \lg n \rceil + 1} + n$ for the number of queries of the Even-Paz algorithm, for $n \ge 2$, where $T(1) = 0$ and $T(k) = 2k + T(\lfloor k/2 \rfloor) + T(\lceil k/2 \rceil)$.

22. ★ All agents have the same additive valuation $v$, and the goods are numbered so that $v(g_1) \ge v(g_2) \ge \dots \ge v(g_m)$. Show that envy-cycle elimination never rotates bundles on this input, that it gives each good to an agent of smallest current value, and that its result is EFX, even when some goods have value 0.

23. ★ Use exercise 22 to prove that every instance with two agents and additive valuations has an EFX allocation, and give an $O(m \log m)$ algorithm that finds one.

24. ★ In the quasi-linear rental model, let $p$ be envy-free for one maximum-weight assignment $\sigma$. Prove that $p$ is envy-free for every maximum-weight assignment $\tau$, and that each tenant gets the same utility under $(\sigma, p)$ and $(\tau, p)$.

25. ★ A necklace has $2a$ red and $2b$ blue beads in some order. Prove that two thieves can always share it fairly with at most two cuts, one thief taking a run of $a + b$ consecutive beads, and give an $O(a + b)$ algorithm that finds the cuts.
