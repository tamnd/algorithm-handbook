## What to remember

- **Two goals for a cake.** A division is proportional when $V_i(X_i) \ge 1/n$ for every agent and
  envy-free when $V_i(X_i) \ge V_i(X_j)$ for all $i$ and $j$. When the whole cake is given out, envy-free
  implies proportional, and for two agents the two coincide.
- **Costs are counted in queries.** In the Robertson-Webb model a protocol asks $\mathrm{Eval}_i(x, y)$ and
  $\mathrm{Cut}_i(x, t)$, and all other work is free. Divide and choose uses 2 queries, the Dubins-Spanier
  knife $n(n + 1)/2 - 1$ cuts, the last diminisher at most $n^2 - 1$ queries, and Even-Paz at most
  $2n\lceil \lg n \rceil - n$.
- **Proportional division is $\Theta(n \log n)$.** Even-Paz reaches the upper bound, and Edmonds and Pruhs
  prove that every deterministic proportional protocol needs $\Omega(n \log n)$ queries.
- **Envy-free division is far harder.** Selfridge-Conway handles three agents with at most 5 cuts.
  Brams-Taylor is finite for every $n$ but has no bound in $n$ alone; Aziz-Mackenzie is bounded by
  $n^{n^{n^{n^{n^n}}}}$ queries, against a lower bound of $\Omega(n^2)$. With connected pieces and
  $n \ge 3$, no finite protocol guarantees envy-freeness.
- **Indivisible goods need relaxed goals.** Envy-free allocations may not exist, and deciding whether one
  exists is NP-complete. EF1 asks $v_i(A_i) \ge v_i(A_j) - \max_{g \in A_j} v_i(g)$ for additive values;
  round-robin and envy-cycle elimination always reach it.
- **Maximin shares cannot always be met.** The share satisfies $\mathrm{MMS}_i \le v_i(M)/n$. Some instances
  with three agents have no allocation that gives every agent its share, but a $3/4$ fraction is always
  reachable in polynomial time.
- **Nash welfare buys fairness with efficiency.** With additive values every maximum Nash welfare allocation
  is EF1 and Pareto optimal. It is APX-hard to compute; the Barman-Krishnamurthy-Vaish market algorithm finds
  an EF1 and Pareto optimal allocation in pseudo-polynomial time.
- **EFX is open.** Removing any good, not just the best, must remove the envy. EFX allocations exist for two
  agents and for three additive agents; for four or more additive agents existence is open.
- **Rent division has an exact answer with money values.** An envy-free pair of rooms and prices exists
  exactly for the maximum-weight assignments, with prices from the dual of the assignment problem, found in
  $O(n^3)$ time.

| Method | Setting | Guarantee | Cost |
|---|---|---|---|
| [Divide and choose](/divide-and-choose/) | cake, 2 agents | envy-free | 2 queries |
| [Dubins-Spanier](/dubins-spanier-moving-knife/) | cake, $n$ agents | proportional, connected | $n(n+1)/2 - 1$ cuts |
| [Last diminisher](/last-diminisher/) | cake, $n$ agents | proportional, connected | $\Theta(n^2)$ queries |
| [Even-Paz](/even-paz-algorithm/) | cake, $n$ agents | proportional, connected | at most $2n\lceil \lg n \rceil - n$ queries |
| [Selfridge-Conway](/selfridge-conway-procedure/) | cake, 3 agents | envy-free | at most 5 cuts and 12 evals |
| [Aziz-Mackenzie](/aziz-mackenzie-protocol/) | cake, $n$ agents | envy-free | bounded by a tower of six $n$ |
| [Adjusted winner](/adjusted-winner/) | 2 agents, divisible goods | envy-free, equitable, Pareto optimal | at most one good split |
| [Round-robin](/round-robin-allocation/) | goods, additive | EF1 | $O(nm \log m)$ time |
| [Envy-cycle elimination](/envy-cycle-elimination/) | goods, monotone | EF1 | $O(mn^3)$ value queries |
| [Maximum Nash welfare](/maximum-nash-welfare/) | goods, additive | EF1 and Pareto optimal | APX-hard |
| [Barman-Krishnamurthy-Vaish](/ef1-and-pareto-optimal-algorithm/) | goods, additive | EF1 and Pareto optimal | pseudo-polynomial |
| [Approximate MMS](/approximate-mms-allocation/) | goods, additive | $3/4$ of each maximin share | polynomial |
| [Su's algorithm](/su-rental-harmony-algorithm/) | rent, room choices | envy-free within $R/N$ per room | at most $\binom{N+n-1}{n-1}$ questions |

: The main methods of the chapter. Queries are Robertson-Webb queries; $n$ is the number of agents, $m$ the
number of goods, $R$ the rent and $N$ the grid size.

## Choosing a method

For a divisible resource and proportional shares, use Even-Paz: it is optimal up to a constant factor and
gives connected pieces. For two agents who want no envy, divide and choose is enough, and adjusted winner
adds equitability and efficiency when the agents state points for a few divisible goods. Envy-free cake
cutting for three agents is practical with Selfridge-Conway; for more agents the bounded protocols are of
theoretical interest only.

For indivisible goods with additive values, round-robin is the simplest way to get EF1, but it can waste
value. When efficiency matters, aim for maximum Nash welfare, the rule that the Spliddit service uses:
solve it exactly for small instances, and use the Barman-Krishnamurthy-Vaish algorithm when values are small
integers. For general monotone valuations, envy-cycle elimination still gives EF1. When agents care about a
guaranteed level rather than comparisons, target a fraction of the maximin share. For rent with money
values, compute a maximum-weight assignment and choose among the envy-free prices with one linear
program.
