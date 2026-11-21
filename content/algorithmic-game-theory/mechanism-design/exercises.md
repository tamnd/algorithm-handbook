1. ◦ Three bidders with values 8, 6 and 2 take part in a [Vickrey auction](/vickrey-auction/). Who wins, at what price, and what is each bidder's utility? Compute the utility of bidder 2 if it bids 9 instead, and of bidder 1 if it bids 5 instead, the others bidding truthfully.

2. ◦ The bridge of the opening costs 90, split equally, so the residents' net values are $40 - 30$, $50 - 30$ and $10 - 30$. Run the [Clarke pivot rule](/clarke-pivot-rule/) on the net values: is the bridge built, and which resident pays a tax beyond its share? Is the mechanism [budget balanced](/budget-balance/)?

3. ◦ A single-parameter rule gives bidder $i$ the allocation $x(z) = 0$ for $z < 2$, $x(z) = 1/2$ for $2 \le z < 5$ and $x(z) = 1$ for $z \ge 5$, the others' bids fixed. Use [Myerson's lemma](/myerson-lemma/) with $h_i = 0$ to find the payment at the bids 1, 3 and 6.

4. ◦ A rule sells one item to a single bidder if and only if its bid lies in $[3, 7]$. Show that it is not a [monotone allocation rule](/monotone-allocation-rule/), and show directly that no payment rule with payment 0 for a losing bid makes it truthful.

5. ◦ Five agents on a line have peaks 1, 4, 6, 9 and 15. Where does the median mechanism put the facility, and what are its social cost and its maximum cost? Compare both with the optimum for each objective.

6. ◦ The mechanism that puts the facility at the midpoint of the leftmost and rightmost reports minimizes the maximum cost. With peaks 0, 4 and 10, show that the agent at 0 gains by reporting $-2$. So this mechanism is not strategyproof; compare with [facility location](/facility-location-mechanism/) mechanisms that are.

7. ◦ In the prosecutor example of [Bayesian persuasion](/bayesian-persuasion/), let the prior of guilt be $2/5$ and let the judge convict if and only if its belief in guilt is at least $2/3$. Find the optimal scheme and the conviction rate.

8. ◦ Three machines and three jobs: machine 1 needs time 1 for each job, machine 2 time 2 and machine 3 time 3. Run the VCG mechanism for [truthful scheduling](/truthful-scheduling-unrelated-machines/). Give the allocation, the payments, the utility of machine 1, the makespan and the optimal makespan.

9. ◦ A buyer's value and a seller's cost are independent and uniform on $[0, 1]$. The mechanism "trade at price $1/2$ if $c \le 1/2 \le v$" is DSIC, ex post IR and budget balanced. Compute its expected gains from trade and compare them with $1/6$, the gains of efficient trade, and with $9/64$, the best that the [Myerson-Satterthwaite theorem](/myerson-satterthwaite-theorem/) entry finds under its constraints.

10. • Two items X and Y are sold to three unit-demand bidders with values $(8, 5)$, $(6, 1)$ and $(3, 4)$ for (X, Y). Find the efficient [assignment](/assignment-problem/), the [VCG](/vcg-mechanism/) payments and the revenue.

11. • Two agents decide on a public project with no cost. Each agent's value is $-3$ or $1$, independently with probability $1/2$, and the project is built when the sum is at least 0. Compute the expected externality terms $h(-3)$ and $h(1)$ of the [AGV mechanism](/agv-mechanism/), the interim utility of each type under truth telling, and the interim utility of each type if it lies. Which types fail interim [individual rationality](/individual-rationality/)?

12. • One agent has type $s$ or $t$ and the rule gives outcome A to $s$ and B to $t$. The values are $v_s(A) = 5$, $v_s(B) = 3$, $v_t(A) = 4$ and $v_t(B) = 6$. Find all pairs of payments $(p_A, p_B)$ that make the rule truthful, and check that the width of the interval for $p_A - p_B$ is the length of the 2-cycle.

13. • One agent has three types with values $t^1 = (6, 2, 0)$, $t^2 = (3, 5, 1)$ and $t^3 = (0, 3, 4)$ for outcomes $(a, b, c)$, and the rule gives $a$ to $t^1$, $b$ to $t^2$ and $c$ to $t^3$. Check [cycle monotonicity](/cycle-monotonicity/) on all cycles, and compute payments as shortest-path distances from $t^1$ with the lengths $c(s, t) = t(f(t)) - t(f(s))$.

14. • Three bidders have independent types, each H or L with probability $1/2$. A symmetric interim rule gives each type H a winning probability $q(H)$ and each type L a probability $q(L)$. Use [Border's theorem](/border-theorem/) to find the largest feasible $q(H)$, and then the largest $q(L)$ given that $q(H)$. Find an auction that attains both.

15. • Two bidders have values 1 or 2 with $\pi(1, 1) = \pi(2, 2) = 2/5$ and $\pi(1, 2) = \pi(2, 1) = 1/10$. Start from the Vickrey auction with random tie-breaking and add the side bet $z(r_j)$ of the [Cremer-McLean theorem](/cremer-mclean-theorem/). Find $z(1)$ and $z(2)$, the total revenue, and check that each type's expected utility from truth telling is 0 and from lying is negative.

16. • With three agents, let $F(R)$ be the top outcome of agent 1. Show that $F$ is [Maskin monotonic](/maskin-monotonicity/), that it violates no veto power, and that a simple mechanism implements it in Nash equilibrium. What does this say about the converse of the sufficiency part of Maskin's theorem?

17. • Show that the [Borda count](/borda-count/), used as a correspondence with ties kept, is not Maskin monotonic. Use three voters with $a > b > c$, $a > b > c$, $b > c > a$, and let voter 3 change to $b > a > c$.

18. • Two bidders bid for one item in an [affine maximizer](/affine-maximizer/) with weights $w = (1, 2)$, no constants, and the Clarke-style $h_i$. Who wins and what does the winner pay at the bids $(9, 4)$ and at $(7, 4)$? Check that each price is the threshold bid that [Myerson's lemma](/myerson-lemma/) gives.

19. • Two bidders want items A and B. Bidder 1 values A, B and AB at 5, 1 and 6; bidder 2 at 4, 3 and 7. A [maximal-in-range mechanism](/maximal-in-range-mechanism/) uses the range "AB to bidder 1", "AB to bidder 2" and "B to bidder 1, A to bidder 2". Find its outcome, its VCG payments on the range, its welfare, and the optimal welfare.

20. • Apply the alternating-sum argument of the [Green-Laffont theorem](/green-laffont-theorem/) to three agents and a binary public project with net values in $\{-2/3, 1/3\}$. Compute the alternating sum of $(n - 1)\max(0, W)$ over the cube, and conclude that no Groves mechanism is strongly budget balanced on it.

21. ★ A seller's cost is uniform on $[0, 1]$ and a buyer's value is uniform on $[0, 2]$, independently. Evaluate the bound of the Myerson-Satterthwaite theorem on $\mathbb{E}[p_b - r_s]$. Then compute the deficit of the VCG mechanism (trade when $v > c$, the buyer pays $c$, the seller receives $v$), the largest entry fees $K_b$ and $K_s$ that keep it interim IR, and check that the remaining deficit meets the bound.

22. ★ Apply the AGV mechanism to bilateral trade with value and cost independent and uniform on $[0, 1]$. Find $h_b(v)$ and $h_s(c)$, the interim utilities $U_b(v)$ and $U_s(c)$, and the worst-off type on each side. Show that the sum of the two worst interim utilities is $-1/6$, and explain why this agrees with the Myerson-Satterthwaite bound.

23. ★ A receiver has three actions with utilities 0, $(2, -1)$ and $(3, -3)$ in the states (good, bad). The sender gets 0, 1 and 3 from the three actions whatever the state, and the prior of good is $1/4$. Find the receiver's best action as a function of its belief, the sender's value $\hat v(\mu)$, its concave closure at $1/4$, and an optimal signaling scheme.

24. ★ One item is sold to $n$ bidders with values in $[0, \infty)$ by a DSIC mechanism that always gives it to a highest bidder, with a fixed tie-breaking order. Use Myerson's lemma to show that the payments have the form of a [Groves mechanism](/groves-mechanisms/). This is a single-parameter case of the uniqueness theorem of Green and Laffont.

25. ★ In exercise 11, the payments are computed for the probability $1/2$ of value 1. Suppose the true probability is $p$ for each agent, while the payments stay the same. For which $p$ is truth telling still a Bayes-Nash equilibrium? What does this say about [Bayesian incentive compatibility](/bayesian-incentive-compatibility/) and the prior?
