1. ◦ Four bidders in a [Vickrey auction](/vickrey-auction/) bid $7, 12, 9, 4$. Who wins and what does the winner pay with no reserve price? With a reserve of $10$? With a reserve of $13$?

2. ◦ Three bidders have values drawn independently from $F(v) = v^2$ on $[0, 1]$. Use $\beta(v) = \mathbb{E}[Y_1 \mid Y_1 < v]$ from the [first-price equilibrium](/first-price-auction-equilibrium/) to find the equilibrium bid. Compute the expected revenue of the first-price auction and check that it equals the expected second-highest value.

3. ◦ A value is uniform on $[1, 3]$. Find its [virtual valuation](/virtual-valuation/) and the monopoly [reserve price](/reserve-price/). What does a seller earn by posting that price to one such buyer? What is the monopoly reserve when the value is uniform on $[2, 3]$ instead?

4. ◦ A value is $1$, $3$ or $4$ with probabilities $1/2$, $1/4$ and $1/4$. Compute the discrete virtual values, say whether the distribution is [regular](/regular-distribution/), and find the best price to post to one buyer and its expected revenue.

5. ◦ Six package bids are made on items $a, b, c, d$: $\{a, b\}$ for 6, $\{c, d\}$ for 5, $\{b, c\}$ for 9, $\{a\}$ for 2, $\{d\}$ for 3 and $\{a, b, c, d\}$ for 12, each by a different bidder. Solve the [winner determination problem](/winner-determination-problem/) by hand.

6. ◦ A [position auction](/position-auction/) has three slots with click-through rates $10, 6, 2$, and four bidders with values per click $5, 4, 3, 1$ who bid their values. Compute what each winner pays per slot under the [generalized second-price auction](/generalized-second-price-auction/) and under VCG.

7. ◦ Run [McAfee's trade reduction mechanism](/mcafee-trade-reduction/) on buyers with values $9, 8, 6, 3$ and sellers with costs $2, 4, 5, 7$. Then run it on buyers $9, 8, 6, 5$ and sellers $2, 4, 5, 8$. In each case give the trades, the prices and what the auctioneer keeps.

8. ◦ Bidder 1 has a value uniform on $[0, 1]$ and bidder 2 a value uniform on $[0, 2]$. Run [Myerson's optimal auction](/myerson-optimal-auction/) on the bids $(0.8, 1.1)$, $(0.4, 1.5)$ and $(0.3, 0.8)$: who wins and what does the winner pay?

9. ◦ A bidder values item $a$ at 4, item $b$ at 3 and the pair at 9. What does it answer to a [demand query](/demand-query/) at prices $(3, 2)$? At $(5, 5)$? At $(5, 1)$?

10. ◦ Three bidders with values uniform on $[0, 1]$ take part in an [all-pay auction](/all-pay-auction/). Give the symmetric equilibrium bid and check that the expected revenue is $1/2$.

11. • For the distribution of Exercise 4 and two bidders, show that the optimal expected revenue is $\mathbb{E}[\max(\varphi(v_1), \varphi(v_2), 0)] = 19/8$. Then show that a second-price auction with reserve 3 and random tie-breaking earns only $37/16$, although it gives the item to the same bidders. Where does the difference come from?

12. • Compute the [VCG](/vcg-mechanism/) payment of each winner in Exercise 5.

13. • In Exercise 6, show that bidding its value is not a best response for the bidder with value 5. Which bid does better, and by how much?

14. • A [uniform price auction](/uniform-price-auction/) sells $3$ identical units, and the price is the highest losing bid. Bidder A has marginal values $10$ and $7$ for its first and second unit; bidders B, C and D each want one unit, at values $6$, $5$ and $1$. Find the outcome when all bid truthfully. Show that A gains by bidding only for one unit.

15. • Two bidders with values uniform on $[0, 1]$ take part in a [first-price auction](/first-price-auction/) with reserve price $1/2$. Show that $\beta(v) = (v^2 + 1/4)/(2v)$ is the equilibrium bid for $v \ge 1/2$, and find the expected revenue without integrating.

16. • In a [common value auction](/common-value-auction/), $n$ bidders see the signals $V + e_i$, with the errors $e_i$ independent and uniform on $[-1, 1]$. Each bids its signal in a second-price auction. Find the expected profit of the winner as a function of $n$. For which $n$ does the winner lose money on average?

17. • Three buyers have values uniform on $[0, 1]$. Solve the ex ante relaxation of [sequential posted pricing](/sequential-posted-pricing/), give the prices it suggests and compute the revenue they earn. Compare the ratio with the guarantee $1 - (1 - 1/n)^n$ and with the revenue of Myerson's auction.

18. • Three items have values i.i.d., each $1$ or $2$ with probability $1/2$, for one additive buyer. Compute the best revenue from [selling the items separately](/simple-versus-optimal-multi-item/) and from selling them as one bundle.

19. • Run the [LOS mechanism](/single-minded-bidder-mechanism/) on five single-minded bidders: A wants $\{1, 2\}$ for 8, B wants $\{2, 3, 4, 5\}$ for 10, C wants $\{3\}$ for 4, D wants $\{4, 5\}$ for 5 and E wants $\{5\}$ for 3. Give the order, the winners, their payments, and the optimal welfare.

20. • For the auction of Exercise 6, write down the bids of the [envy-free equilibrium](/gsp-envy-free-equilibrium/) that gives the VCG outcome. Check that each winner pays its VCG price and that the bidder with value 5 has no profitable deviation.

21. • Write the valuation of Exercise 9 in the OR and in the XOR [bidding languages](/bidding-languages/) with as few atoms as you can. Show that two atoms are not enough in either language.

22. ★ Bidders know each other's values $v_1 \ge v_2 \ge \dots \ge v_n$ and play a first-price auction. Show that in every mixed Nash equilibrium the expected welfare is at least $v_1/2$. (Consider bidder 1 deviating to the bid $v_1/2$.)

23. ★ With $n$ bidders whose values are i.i.d. uniform on $[0, 1]$, show that the optimal expected revenue is $\frac{n-1}{n+1} + \frac{1}{(n+1)2^n}$. Then check the [Bulow-Klemperer theorem](/bulow-klemperer-theorem/) for this distribution and every $n \ge 1$ by direct computation.

24. ★ Show that the generalized second-price auction is not truthful for any number $k \ge 2$ of slots and any click-through rates $\alpha_1 > \alpha_2 > 0$: give values for three bidders at which the top bidder gains by bidding below its value.

25. ★ A seller with cost $s$ and a buyer with value $b$ use a deterministic mechanism that is truthful in dominant strategies, trades exactly when $b \ge s$, and charges nothing to either side when there is no trade. Use [Myerson's lemma](/myerson-lemma/) to show that when trade happens the buyer pays $s$ and the seller receives $b$. What does the mechanism need from outside? Relate this to the [Myerson-Satterthwaite theorem](/myerson-satterthwaite-theorem/).

26. ★ Show that winner determination is solvable in polynomial time when every bid names at most two items. (Reduce to [maximum weight matching](/maximum-weight-matching/) in a graph whose vertices are the items, plus extra vertices for the bids on one item.)
