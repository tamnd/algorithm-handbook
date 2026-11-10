## What to remember

- A **local optimum** depends on the neighborhood: a larger neighborhood has the same or fewer. For random distinct values on $\{0,1\}^n$ with single flips, there are $2^n/(n+1)$ local minima on average.
- **Hill climbing** stops in the first local optimum it reaches, after a number of moves that can be exponential. If one run succeeds with probability $p$, **random restarts** with $R \ge \ln(1/\delta)/p$ runs all fail with probability at most $\delta$.
- The **Metropolis criterion** accepts a rise $\Delta$ with probability $\min(1, e^{-\Delta/T})$. With a symmetric proposal it makes the Boltzmann distribution $\pi_T(x) \propto e^{-f(x)/T}$ stationary.
- **Simulated annealing** finds a global minimum with probability tending to 1 if and only if $\sum_k e^{-d^*/T_k} = \infty$ (Hajek), so $T_k = c/\ln(k+1)$ works exactly when $c \ge d^*$, the depth of the deepest trap. Practical schedules fall faster and carry no guarantee.
- **Tabu search** forbids the attributes of the last $t$ moves. With single flips and aspiration by objective, it cannot return to a solution within $t + 1$ moves; longer cycles remain possible.
- A **genetic algorithm** with [elitism](/elitism/) and a mutation rate strictly between 0 and 1 finds an optimum of a finite problem with probability tending to 1, with no bound on the time. The $(1+1)$ EA needs expected $\Theta(n \log n)$ iterations on OneMax.
- **Comparison-based methods** ([tournament selection](/tournament-selection/), evolution strategies, CMA-ES, differential evolution) depend only on the order of the values of $f$, so they behave the same on $g \circ f$ for any strictly increasing $g$. [Roulette-wheel selection](/roulette-wheel-selection/) and the Metropolis criterion do not.
- The **no free lunch theorem**: over a set of functions closed under permutation of the inputs, and only over such sets, every search algorithm has the same distribution of observed values. A claim that one method is better must name its class of functions.

## The main methods side by side

| Method | State | Leaves a local optimum by | Time | Extra space |
|---|---|---|---|---|
| [Hill climbing](/hill-climbing/) | one solution | it does not | $O(kNT)$ | $O(s)$ |
| [Random-restart hill climbing](/random-restart-hill-climbing/) | one solution | a new random start | $O(RH)$ | $O(s)$ |
| [Simulated annealing](/simulated-annealing/) | one solution | random acceptance of rises | $O(kc)$ | $O(s)$ |
| [Late acceptance](/late-acceptance-hill-climbing/) | one solution | comparison with an old cost | $O(Ke + L)$ | $O(L + s)$ |
| [Tabu search](/tabu-search/) | one solution | best admissible move, tabu list | $O(Kd(e + t))$ | $O(s + t)$ |
| [Iterated local search](/iterated-local-search/) | one local optimum | perturbation and new descent | $O(K(H + P) + H)$ | $O(s)$ |
| [Genetic algorithm](/genetic-algorithm/) | $N$ strings | selection, crossover, mutation | $O(gN(n + c))$ | $O(Nn)$ |
| [(1+1)-ES](/evolution-strategies/) | one point of $\mathbb{R}^n$ | Gaussian steps, 1/5 rule | $O(k(n + c))$ | $O(n)$ |
| [CMA-ES](/cma-es/) | a Gaussian | samples from a learned covariance | $O(g(ln^2 + lc + n^3))$ | $O(n^2 + ln)$ |
| [Differential evolution](/differential-evolution/) | $p$ points | difference vectors | $O(gp(n + c))$ | $O(pn)$ |
| [Particle swarm](/particle-swarm-optimization/) | $N$ particles | pull toward best points | $O(TN(n + c))$ | $O(Nn)$ |
| [Ant colony (MMAS)](/ant-colony-optimization/) | pheromone on the edges | random construction | $O(Tmn^2)$ | $O(n^2)$ |

: The main metaheuristics, with the costs their entries give for a given number of steps $k$, $K$, $T$ or $g$. Each entry defines its symbols: $c$ and $e$ are costs of one evaluation, $s$ the size of a solution, $H$ the time of one local search. None of the methods has a useful bound on the number of steps for a general function.

## Choosing a method

- Write a good neighborhood and a fast evaluation of a move first. Every method spends most of its time there, and the neighborhood often matters more than the method.
- For a discrete problem with a cheap move, start with simulated annealing with a geometric schedule, or late acceptance, which has one parameter. If good local optima are far apart, try iterated local search or tabu search.
- When a good greedy construction exists, try GRASP or ant colony optimization, which randomize the greedy choice.
- For a continuous problem without gradients in up to a few hundred dimensions, use CMA-ES. Differential evolution is simpler to write and does well on separable problems.
- Use a genetic algorithm when crossover can combine good parts of two solutions, and add local search to each child, as the memetic algorithm does.
- Compare methods with the same budget of evaluations on instances like yours. Treat a method described by a metaphor with care: several swarm methods of this chapter are older methods under new names.
