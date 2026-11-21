## What to remember

- Finding a Nash equilibrium is a total search problem: an answer always exists and is easy to check. Its hardness is measured by PPAD, not by NP.
- A two-player zero-sum game is one linear program and its dual, and the value and optimal strategies come out in polynomial time. The sequence form does the same for zero-sum game trees with perfect recall.
- Correlated equilibria are the distributions $p$ on profiles with $Up \ge 0$: one LP with $|S|$ variables and $\sum_i k_i(k_i - 1)$ incentive inequalities, which can also maximize welfare. For succinct games the ellipsoid against hope finds one in time polynomial in the description.
- In a nondegenerate bimatrix game every equilibrium has supports of equal size, so support enumeration lists all equilibria. The Lemke-Howson algorithm follows a path of pivots to one equilibrium, which proves that their number is odd. Savani and von Stengel built games on which every Lemke-Howson path is exponentially long.
- Two-player Nash is PPAD-complete (Chen, Deng and Teng), also for $1/n^{\Theta(1)}$-approximation, and $\varepsilon$-Nash with three or more players is PPAD-complete (Daskalakis, Goldberg and Papadimitriou). This is evidence, not proof, that no polynomial algorithm exists. Deciding whether an equilibrium with a given property exists, such as a payoff of at least $k$ for player 1, is NP-complete.
- For constant $\varepsilon$, a $1/2$-approximate equilibrium takes $O(m + n)$ time (DMP), and every $\varepsilon$ takes $n^{O(\log n / \varepsilon^2)}$ time (Lipton, Markakis and Mehta). Under an exponential time hypothesis for PPAD, some constant $\varepsilon$ needs $n^{\log^{1-o(1)} n}$ time (Rubinstein).
- When every player has external regret $o(T)$, the empirical distribution of play converges to the coarse correlated equilibria, not to Nash equilibria. With swap regret $o(T)$, as in regret matching or the Blum-Mansour reduction, it converges to the correlated equilibria. In zero-sum games the average strategies of no-regret players approach optimal ones.
- Fictitious play converges in two-player zero-sum games (Robinson 1951) but cycles in a $3 \times 3$ game of Shapley. Best-response dynamics reaches a pure equilibrium in every finite potential game, possibly after exponentially many steps.

## The methods side by side

| Method | Problem | Time | Output |
|---|---|---|---|
| Support enumeration | bimatrix, $m \times n$ | $O(2^{m+n}(mn + \min(m, n)^3))$ | all equilibria (nondegenerate) |
| Lemke-Howson | bimatrix, $m \times n$ | $O(2^{m+n}(m+n)^3)$ | one equilibrium (nondegenerate) |
| Lemke | LCP of size $n$ | $O(2^n n^3)$ | a solution or a ray, for suitable $M$ |
| LP | zero-sum, $m \times n$ | $\mathrm{poly}(m, n, L)$ | value and optimal strategies |
| Sequence-form LP | zero-sum tree, $N$ nodes | $\mathrm{poly}(N, L)$ | optimal behaviour strategies |
| CE LP | $n$ players, $k$ strategies | $\mathrm{poly}(n, k^n, L)$ | a CE, also of best welfare |
| Ellipsoid against hope | succinct game | $\mathrm{poly}(n, k, L)$ | some CE |
| Multiple LPs | Stackelberg, $m \times n$ | $\mathrm{poly}(m, n, L)$ | optimal commitment |
| DMP | bimatrix | $O(m + n)$ | $1/2$-Nash |
| Lipton-Markakis-Mehta | bimatrix, $n \times n$ | $n^{O(\log n / \varepsilon^2)}$ | $\varepsilon$-Nash |
| Regret matching | $n$ players, $T$ rounds | $O(nkT)$ | approximate CE on average |
| Blum-Mansour | $k$ actions, $T$ rounds | $O(Tk^3)$ | swap regret $o(T)$ |
| Optimistic Hedge | $k$ actions, $T$ rounds | $O(kT)$ | regret $O(n \log k \log^4 T)$ in games |

: Worst-case costs from the entries; $L$ is the bit length of the input. Savani and von Stengel's games make both Lemke-Howson and support enumeration take exponential time. The learning methods give approximate equilibria whose error falls as $T$ grows.

## Choosing a method

- If the game is zero-sum, solve the LP of the minimax theorem; for a game tree with perfect recall, use the sequence form, not the normal form, which is exponentially larger.
- If any correlated equilibrium will do, or the best one for welfare, solve the CE LP. For a game with many players given succinctly, use the ellipsoid against hope or, for an approximate answer, regret matching.
- For one Nash equilibrium of a bimatrix game of moderate size, run Lemke-Howson from several starting labels. For all of them, use support enumeration or vertex enumeration of the best-response polytopes.
- If an error of $1/2$ is acceptable, the DMP algorithm gives it at once.
- For an equilibrium with a property, such as the best welfare, expect NP-hardness and exponential search, unless the game is zero-sum or a correlated equilibrium is enough.
- For a game played many times by simple agents, no-regret rules give a coarse correlated equilibrium on average, and no-swap-regret rules a correlated one.
