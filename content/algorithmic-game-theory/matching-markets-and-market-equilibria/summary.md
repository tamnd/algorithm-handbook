## What to remember

- **Stable matchings have structure.** They form a distributive lattice with the two proposer-optimal matchings at the ends, and every stable matching matches the same agents. With couples a stable matching may not exist, and deciding whether one does is NP-complete.
- **Deferred acceptance is safe for one side only.** Truth is a dominant strategy for every proposer, but no stable mechanism makes truth dominant for both sides. In school choice, student-proposing deferred acceptance is stable and strategyproof for students but not Pareto efficient; top trading cycles is efficient and strategyproof but not stable; the Boston mechanism is neither stable nor strategyproof.
- **Without money, order and chance decide.** Serial dictatorship is Pareto optimal and strategyproof, and every Pareto optimal matching comes from some order. Random serial dictatorship adds equal treatment but is not ordinally efficient. Probabilistic serial is ordinally efficient and sd-envy-free but only weakly strategyproof. For $n \ge 4$ no rule is ordinally efficient, strategyproof and equal-treatment at once.
- **Top trading cycles solves the housing market.** With strict rankings its allocation is the unique strict core allocation and the unique competitive allocation, with prices $r - k + 1$ for the houses of the $k$-th of $r$ cycles. It runs in $O(n + L)$ time and is strategyproof.
- **Kidney exchange is easy only at the extremes.** Swaps only ($L = 2$) is maximum matching, and unbounded cycles is the assignment problem, but every fixed bound $L \ge 3$ makes the problem NP-hard.
- **Competitive equilibria are efficient and exist under convexity.** With local nonsatiation every equilibrium allocation is Pareto optimal. With continuity, convexity, local nonsatiation and positive endowments an equilibrium exists.
- **Linear Fisher markets are a convex program.** The equilibrium maximizes $\sum_i e_i \log \sum_j u_{ij} x_{ij}$ subject to $\sum_i x_{ij} \le 1$, with prices as dual variables; at equilibrium a buyer spends only on goods of maximum bang per buck $u_{ij}/p_j$. Prices and utilities are unique. DPSV needs a polynomial number of max flows, Orlin's algorithm is strongly polynomial, and proportional response has potential gap at most $\mathrm{KL}(b^* \| b^0)/T$ after $T$ rounds.
- **Richer utilities are hard.** For exchange markets with separable piecewise-linear concave utilities, even two segments per good, finding an equilibrium is PPAD-complete, and so is the Fisher market with these utilities.
- **Gross substitutes is the line for indivisible goods.** With gross substitutes valuations a Walrasian equilibrium exists. For unit-demand bidders the DGS auction ends at the minimum Walrasian prices, which equal the VCG payments; the Kelso-Crawford process allows bundles and ends within $m\delta$ of the optimum.

| problem | method | guarantee | time |
|---|---|---|---|
| two-sided matching | deferred acceptance | stable, truthful for proposers | $O(n^2)$ |
| best stable matching by total rank | rotations and min cut | egalitarian | $O(n^4)$ |
| house allocation | serial dictatorship | Pareto optimal, strategyproof | $O(m + n^2)$ |
| random house allocation | probabilistic serial | ordinally efficient, sd-envy-free | $O(m(n + m))$ |
| housing market | top trading cycles | unique strict core, strategyproof | $O(n + L)$ |
| kidney exchange, $L \ge 3$ | cycle formulation, branch and price | optimal | exponential in the worst case |
| linear Fisher market | Orlin's algorithm | exact | $O(n^2 \log n\,(m + n \log n))$ |
| linear Fisher market | proportional response | potential gap $O(1/T)$ | $O(nm)$ per round |
| unit-demand auction | DGS auction | minimum Walrasian prices | pseudo-polynomial |
| SPLC exchange market | none known | PPAD-complete | none polynomial unless PPAD is in P |

: Main problems, methods, guarantees and running times. For Orlin's algorithm, $n$ counts buyers and goods and $m$ is the number of pairs with $u_{ij} > 0$.

## Choosing a method

For a two-sided market where one side must be safe from manipulation, use deferred acceptance with that side proposing; by the [rural hospitals theorem](/rural-hospitals-theorem/), no other stable matching fills more positions. In school choice, deferred acceptance respects priorities, and top trading cycles favours efficiency for students.

For objects without money, use serial dictatorship when a natural order exists, random serial dictatorship when it must be fair and simple to explain, and probabilistic serial when efficiency of the lottery matters more than strict truthfulness. If agents own the objects, as in a housing market, use top trading cycles.

For divisible goods and money, solve the Fisher market as the Eisenberg-Gale program, or run proportional response when a simple distributed method is enough. For fair division with cardinal utilities, a [competitive equilibrium from equal incomes](/competitive-equilibrium-from-equal-incomes/) gives an envy-free and Pareto optimal allocation; for course seats, use [approximate CEEI](/approximate-ceei/).
