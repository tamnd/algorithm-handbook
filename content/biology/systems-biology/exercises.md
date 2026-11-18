1. ◦ A network has the reactions $A + B \to C$ (rate constant $k_1$), $C \to A + B$ ($k_2$) and $C \to D$ ($k_3$). Write its [stoichiometric matrix](/stoichiometric-matrix/) with species in the order $A, B, C, D$, give its rank, find two independent conservation laws, and write the [mass action](/mass-action-kinetics/) ODE.

2. ◦ For the [Hill function](/hill-equation/) $x^n/(K^n + x^n)$ with $K = 1$, find the inputs at which the response is 10% and 90% for $n = 2$ and for $n = 4$. By what factor must the input grow to go from 10% to 90% in each case?

3. ◦ An enzyme follows [Michaelis-Menten kinetics](/michaelis-menten-kinetics/) with $V_{\max} = 10$ and $K_M = 2$. Give the rate at $S = 2$ and at $S = 6$, and the substrate level at which the rate is 90% of $V_{\max}$.

4. ◦ An immigration-death network has $\emptyset \to A$ with propensity 2 and $A \to \emptyset$ with propensity $0.5\,x$. The state is $x = 4$. Run one step of the [direct method](/gillespie-algorithm/) with $U_1 = 0.5$ and $U_2 = 0.7$: give the time step, the reaction that fires and the new state.

5. ◦ A synchronous Boolean network has the update rules $x_1' = x_2 \wedge \neg x_3$, $x_2' = x_1 \vee x_3$ and $x_3' = x_1$. Draw its state transition graph on the 8 states, list its attractors, and give the size of each basin.

6. ◦ A metabolic network has an uptake $v_1$ into $A$ with $0 \le v_1 \le 10$, reactions $A \to B$ ($v_2$), $A \to C$ ($v_3$), $C \to B$ ($v_5$, with $v_5 \le 3$), and a biomass drain $B \to$ ($v_4$). All fluxes are nonnegative. Solve the [flux balance](/flux-balance-analysis/) problem that maximizes $v_4$. Is the optimal flux vector unique?

7. ◦ Three genes are jointly normal with correlations $\rho_{XY} = 0.8$, $\rho_{YZ} = 0.7$ and $\rho_{XZ} = 0.56$, and the mutual information of a pair is $-\tfrac12 \ln(1 - \rho^2)$. Which edge does [ARACNE](/aracne/) remove with tolerance $\tau = 0$? Is it removed with $\tau = 0.5$?

8. ◦ A pure death reaction $A \to \emptyset$ has propensity $x$. From $x = 5$, [tau-leaping](/tau-leaping/) with $\tau = 1$ fires a Poisson number of reactions with mean 5. What is the probability that the count goes negative in this leap?

9. ◦ A birth process $\emptyset \to A$ with propensity 1 starts at 0. The [finite state projection](/finite-state-projection/) keeps the states $0, \ldots, 5$. What is its error at $t = 2$?

10. • For the network of exercise 6, run [flux variability analysis](/flux-variability-analysis/) at the optimum: give the range of every flux. How many LPs does FVA solve here?

11. • Compute the deficiency $\delta = c - l - s$ of the network $A + B \rightleftharpoons C \rightleftharpoons D$, and of the network $A \rightleftharpoons B$, $2A \rightleftharpoons A + B$. What does the [deficiency zero theorem](/deficiency-zero-theorem/) say about the first one? Describe its positive compatibility classes.

12. • The network $A \rightleftharpoons 2A$ has forward rate constant $k_1$ and backward rate constant $k_2$ under mass action. Check that it is weakly reversible with deficiency 0, and confirm the conclusion of the theorem by solving its ODE for the equilibria and their stability.

13. • A network has an uptake $\to A$ ($v_1$), reactions $A \to B$ ($v_2$), $A \to C$ ($v_3$), $B \to C$ ($v_6$), and drains $B \to$ ($v_4$) and $C \to$ ($v_5$), all irreversible. Find all its [elementary flux modes](/elementary-flux-mode/), and show that every steady flux vector is a nonnegative combination of them.

14. • In the toggle switch model $u' = \alpha/(1 + v^2) - u$, $v' = \alpha/(1 + u^2) - v$ with $\alpha = 3$, find the three equilibria and classify each by the eigenvalues of the Jacobian. For the outer pair, show first that $uv = 1$ and $u + v = 3$.

15. • In a [feed-forward loop](/feed-forward-loop/) of type C1, $Y$ is made at rate $\beta_Y$ and lost at rate $\alpha_Y = 0.5$ per hour, so its steady level is $Y_{\mathrm{st}} = \beta_Y/\alpha_Y$, and $Z$ reads $Y$ with threshold $K_{YZ} = Y_{\mathrm{st}}/4$. Compute the delay of the ON step with an AND input, and the delay of the OFF step with an OR input when the signal is removed after $Y$ has reached $Y_{\mathrm{st}}$.

16. • Write the [chemical master equation](/chemical-master-equation/) of $A \to \emptyset$ with propensity $c\,x$ from $n_0$ molecules. Check that the binomial law with $n_0$ trials and success probability $e^{-ct}$ solves it.

17. • Wild-type fluxes on a network with $v_1 = v_2 + v_3$ are $w = (10, 7, 3)$, with $0 \le v_1 \le 10$. Reaction 2 is knocked out. Find the flux vector that [MOMA](/minimization-of-metabolic-adjustment/) predicts, and compare it with the FBA prediction that maximizes $v_1$.

18. • A network has uptake $\to A$ with $v_1 \le 10$, reaction $A \to 2\,\mathrm{BIO}$, reaction $A \to \mathrm{BIO} + P$, and drains for BIO (growth) and $P$. The cell maximizes growth. Which single deletion does [OptKnock](/optknock/) choose to maximize the secretion of $P$, and what are the growth and the secretion after it?

19. • A pure death reaction $A \to \emptyset$ with propensity $c\,x$ starts at $x = 100$, with $c = 1$. Compare the mean count after one tau-leap of length $\tau = 0.1$ with the exact mean at $t = 0.1$. Show that the gap is $O(\tau^2)$.

20. ★ Show that the [first reaction method](/first-reaction-method/) and the direct method sample the same law for one step: the minimum of independent exponential times with rates $a_1, \ldots, a_m$ is exponential with rate $a_0 = \sum_j a_j$, the index of the minimum is $j$ with probability $a_j/a_0$, and the two are independent.

21. ★ In the [next reaction method](/next-reaction-method/), a reaction whose propensity changes from $a$ to $a'$ at time $t$ has its stored firing time replaced by $t + (a/a')(\tau - t)$. Show that, given the past, the new remaining time is exponential with rate $a'$, so no new random number is needed.

22. ★ Without any limit on the in-degree, reduce SAT to the existence of a fixed point of a synchronous Boolean network: given a CNF formula $\varphi$ over $x_1, \ldots, x_n$, use the rules $x_i' = x_i$ and $y' = \varphi(x) \vee \neg y$. Prove that the network has a fixed point exactly when $\varphi$ is satisfiable.

23. ★ A chain $A_0 \to A_1 \to \cdots \to A_n$ has two parallel irreversible reactions for each step, an uptake into $A_0$ and a drain from $A_n$. Show that it has exactly $2^n$ elementary flux modes, so that no enumeration method runs in time polynomial in the size of the network.

24. ★ A protein-only repressilator has $x_i' = \alpha/(1 + x_{i-1}^n) - x_i$ for $i = 1, 2, 3$, indices mod 3. Let $g$ be the size of the slope of the repression at the symmetric equilibrium. Show that the Jacobian there has eigenvalues $-1 - g\omega$ with $\omega^3 = 1$, and that the equilibrium is unstable exactly when $g > 2$.
