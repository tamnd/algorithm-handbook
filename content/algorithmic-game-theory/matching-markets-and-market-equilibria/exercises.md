1. ◦ Agent 1 owns one unit of good $x$ and has utility $x^{1/3} y^{2/3}$. Agent 2 owns one unit of good $y$ and has utility $x^{1/2} y^{1/2}$. A Cobb-Douglas agent spends on each good the share of her income given by its exponent. With $p_x = 1$, find the equilibrium price of $y$ and the two bundles, and check that both markets clear.

2. ◦ In an exchange market, agent 1 owns one unit of good 1 and has utility $2 y_1 + y_2$, and agent 2 owns one unit of good 2 and has utility $y_1 + 3 y_2$. Find every equilibrium price ratio $p_1 / p_2$ and the allocations. Compare with the example of the [Arrow-Debreu market](/arrow-debreu-market/) entry, where the prices are unique.

3. ◦ A Fisher market has three buyers with budget 1 each and two goods. The utilities are $u_1 = (2, 1)$, $u_2 = (1, 1)$ and $u_3 = (1, 3)$. Show that the prices $(3/2, 3/2)$ are the equilibrium prices: give the money that each buyer spends on each good, check the bang per buck of every buyer, and compute the utilities.

4. ◦ A bidder values the pair $\{a, b\}$ at 3 and each single item at 0. Find her demand at prices $(1, 1)$ and at prices $(1, 3)$, and say which condition of [gross substitutes](/gross-substitutes/) fails. Do the same for an additive bidder who values each item at 2.

5. ◦ Six agents own houses $h_1, \dots, h_6$. Agent 1 ranks $h_2, h_3, h_1, h_4, h_5, h_6$; agent 2 ranks $h_3, h_1, h_2, h_4, h_5, h_6$; agent 3 ranks $h_1, h_2, h_3, h_4, h_5, h_6$; agent 4 ranks $h_1, h_5, h_6, h_4, h_2, h_3$; agent 5 ranks $h_4, h_2, h_6, h_5, h_1, h_3$; agent 6 ranks $h_5, h_4, h_6, h_1, h_2, h_3$. Run [top trading cycles](/top-trading-cycles/), list the cycles of each round, and give prices that make the allocation competitive.

6. ◦ Three agents and three objects. Agent 1 ranks $a, b, c$, agent 2 ranks $b, a, c$, and agent 3 ranks $b, c, a$. Run serial dictatorship for each of the six orders and give the probabilities of [random serial dictatorship](/random-serial-dictatorship/). Then run [probabilistic serial](/probabilistic-serial/) on the same lists. Which agents prefer which lottery in the sense of stochastic dominance?

7. ◦ Six patient-donor pairs have the compatibility arcs $1 \to 2$, $2 \to 1$, $2 \to 3$, $3 \to 4$, $4 \to 2$, $4 \to 5$, $5 \to 6$, $6 \to 4$ and $6 \to 1$. Find the largest number of transplants by disjoint cycles of length at most 2, at most 3, and of any length.

8. ◦ Three men and three women have the lists $m_1$: $w_1, w_2, w_3$; $m_2$: $w_2, w_1, w_3$; $m_3$: $w_3, w_1, w_2$; $w_1$: $m_2, m_3, m_1$; $w_2$: $m_1, m_3, m_2$; $w_3$: $m_1, m_2, m_3$. Run deferred acceptance with the men proposing and with the women proposing. How many stable matchings are there, and which pair is in all of them?

9. ◦ Four students and three schools; $s_1$ and $s_3$ have one seat and $s_2$ has two. Student $i_1$ ranks $s_3, s_1, s_2$, student $i_2$ ranks $s_1, s_3, s_2$, and students $i_3$ and $i_4$ rank $s_1, s_2, s_3$. The priorities of $s_1$ and of $s_2$ are $i_1, i_3, i_4, i_2$, and those of $s_3$ are $i_2, i_1, i_4, i_3$. Compute the matchings of student-proposing deferred acceptance, top trading cycles and the [Boston mechanism](/boston-mechanism/).

10. ◦ Two agents and two objects. Agent 1 has utilities $(1, 0)$ and agent 2 has $(5, 2)$. Find a [Hylland-Zeckhauser](/hylland-zeckhauser-mechanism/) equilibrium whose smallest price is 0, and explain why with two objects the cardinal values play no role.

11. • In a Fisher market, buyer $i$ has budget $e_i$ and utility $\prod_j x_{ij}^{a_{ij}}$ with $a_{ij} \ge 0$ and $\sum_j a_{ij} = 1$. Show that the [Eisenberg-Gale program](/eisenberg-gale-program/) splits into one problem per good, that its solution is $x_{ij} = a_{ij} e_i / \sum_k a_{kj} e_k$, and that the prices are $p_j = \sum_i a_{ij} e_i$. Check the formulas on the market with $e = (1, 2)$, $a_1 = (1/2, 1/2)$ and $a_2 = (1/4, 3/4)$.

12. • Run [proportional response dynamics](/proportional-response-dynamics/) on the market of Exercise 3, starting with every buyer bidding $1/2$ on each good. Give the prices, the allocation and the new bids, and then the prices of the next round. Why does buyer 2 keep her bids in the first round?

13. • For the Cobb-Douglas market of Exercise 11, the excess demand of good $j$ is $z_j(p) = \sum_i a_{ij} e_i / p_j - 1$. Discrete [tatonnement](/tatonnement/) sets $p_j \leftarrow p_j + \lambda z_j(p)$ with a fixed step $\lambda > 0$. For which $\lambda$ does it converge from every start close enough to the equilibrium? Run it with $\lambda = 2.1$ from $(3/2, 3/2)$ and describe what happens.

14. • Three buyers with budget 1 each share two goods, with $u_1 = (4, 1)$ and $u_2 = u_3 = (1, 1)$. Find the [competitive equilibrium from equal incomes](/competitive-equilibrium-from-equal-incomes/), check that it is envy-free, and compare its Nash welfare $u_1 u_2 u_3$ with that of the equal split. Is the allocation unique?

15. • Four agents and four objects. Agent 1 ranks $a, b, c, d$, agent 2 ranks $a, c, b, d$, agent 3 ranks $b, a, c, d$, and agent 4 ranks $b, a, d, c$. Compute the probabilistic serial assignment by hand and the random serial dictatorship assignment over all 24 orders, by program. Find two agents who can trade probability shares of the RSD assignment so that both gain in the sense of stochastic dominance.

16. • Four unit-demand bidders and three items have the values $(5, 3, 2)$, $(9, 1, 7)$, $(8, 3, 1)$ and $(9, 2, 1)$ for bidders 1 to 4. Find the final prices and an assignment of the [Demange-Gale-Sotomayor auction](/demange-gale-sotomayor-auction/), and check that every winner pays her VCG payment.

17. • Four men and four women have the lists $m_1$: $w_2, w_3, w_4, w_1$; $m_2$: $w_4, w_2, w_3, w_1$; $m_3$: $w_3, w_2, w_4, w_1$; $m_4$: $w_1, w_2, w_4, w_3$; $w_1$: $m_3, m_4, m_1, m_2$; $w_2$: $m_4, m_3, m_2, m_1$; $w_3$: $m_2, m_4, m_1, m_3$; $w_4$: $m_1, m_4, m_3, m_2$. Find all stable matchings with their egalitarian costs and regrets (the largest rank anyone gets). Which is the [egalitarian stable matching](/egalitarian-stable-matching/)? Draw the lattice.

18. • In the school choice problem of Exercise 9, find a student who gains under the Boston mechanism by reporting a false list. Which of the three matchings has justified envy, and which pairs cause it? Show that one of them Pareto dominates the deferred acceptance matching for the students.

19. • Five pairs sit on a ring, and each pair is compatible in both directions with its two neighbours. Find the most transplants with cycles of length at most 2, at most 3, and of any length. Then solve the LP relaxation of the [cycle formulation](/kidney-exchange-cycle-formulation/) for length at most 2, and prove its value with a dual solution.

20. • Agents 1 and 2 rank $a, b$, agent 3 ranks $b, c$, and agent 4 ranks $c, d$; no agent accepts other posts. Find all [popular matchings](/popular-matching/). Then let agent 3 rank $a, b$ instead and show that no popular matching exists.

21. • Prove that every Pareto optimal matching of the [house allocation problem](/house-allocation-problem/) has at least half as many pairs as a maximum matching. Give an instance and an order for which serial dictatorship gets exactly half.

22. • In the market of Exercise 8, under men-proposing deferred acceptance, find a woman who gains by leaving some men off her list. Explain why this does not contradict the theorem on the [strategyproofness of deferred acceptance](/deferred-acceptance-strategyproofness/), and relate it to [Roth's impossibility theorem](/roth-impossibility-theorem/).

23. • In a housing market, agent 1 is indifferent between $h_1$ and $h_2$, and agent 2 ranks $h_1$ above $h_2$. Show that the allocation without trade, with prices $p(h_1) = 2$ and $p(h_2) = 1$, is competitive: each agent gets a best house among those it can afford. Show that it is not Pareto optimal, and find the step of the proof of the [first welfare theorem](/first-welfare-theorem/) that fails.

24. ★ In a marriage market with strict lists, each agent votes for the matching that gives it the better partner, being unmatched is worst, and an agent with the same partner in both does not vote. Prove that a stable matching gets at least as many votes as any other matching, so every stable matching is popular.

25. ★ For cycles of length at most 2, the cycle formulation is the matching LP of the graph of mutual compatibilities, with weight 2 per swap. Prove that its LP value is at most $3/2$ times the integer optimum, and that the example of the cycle formulation entry, three pairs that are all mutually compatible, reaches $3/2$.

26. ★ In an exchange market with two agents and two goods, agent $i$ owns one unit of good $i$ and has linear utility with all $u_{ij} > 0$. Let $\alpha = u_{11}/u_{12}$ and $\beta = u_{21}/u_{22}$. Prove that an equilibrium exists. Show that the equilibrium price ratios $p_1 / p_2$ form the interval $[\beta, \alpha]$ without trade when $\beta \le \alpha$, and are the single value $\mathrm{median}(\alpha, 1, \beta)$ when $\beta > \alpha$.

27. ★ In a school choice problem every school ranks the students in the same order $\sigma$. Prove that student-proposing deferred acceptance and top trading cycles both give the serial dictatorship matching with order $\sigma$. Give an instance with three students and three schools of one seat each in which the Boston mechanism gives a different matching.

28. ★ Construct a stable marriage instance in which no egalitarian stable matching has the minimum regret among stable matchings.
