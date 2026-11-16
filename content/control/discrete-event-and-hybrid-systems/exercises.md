1. ◦ The machine of [discrete-event system](/discrete-event-system/) has states $I$, $W$, $D$, the transitions $I \xrightarrow{a} W$, $W \xrightarrow{b} I$, $W \xrightarrow{f} D$, $D \xrightarrow{r} I$, initial state $I$ and marked state $I$. List the strings of $L(G)$ of length 4 and say which of them are in $L_m(G)$.

2. ◦ For the same machine, with $a$ and $r$ controllable, is the prefix-closed specification "the machine is never repaired" (the strings of $L(G)$ without $r$) [controllable](/controllable-language/)? Is "the machine never finishes" (the strings without $b$)? For the controllable one, is the closed loop under the supervisor that enforces it nonblocking?

3. ◦ In [max-plus algebra](/max-plus-algebra/), let $A = \begin{bmatrix} 2 & 5 \\ 1 & 3 \end{bmatrix}$. Compute $x(1)$, $x(2)$ and $x(3)$ for $x(k+1) = A \otimes x(k)$ from $x(0) = (0, 0)$. Find the maximum cycle mean of $A$ and an eigenvector.

4. ◦ In Example 2 of [timed event graph](/timed-event-graph/) (holding times 3 on machine 1, 4 on machine 2, 3 and 4 on the moves, 0 on the pallet return), put two pallets on the line instead of one, so the return place holds 2 tokens. What is the cycle time, and which circuit is critical? Does a third pallet help?

5. ◦ A plant has the transitions $0 \xrightarrow{f} 1$, $1 \xrightarrow{a} 2$, $2 \xrightarrow{b} 4$, $4 \xrightarrow{a} 4$ after the fault and $0 \xrightarrow{a} 3$, $3 \xrightarrow{b} 5$, $5 \xrightarrow{b} 5$ without it. The events $a$ and $b$ are observable and the fault $f$ is not. Check the two assumptions of [diagnosability](/diagnosability/), and find the smallest delay $n_f$.

6. ◦ Let $A_1 = \begin{bmatrix} -1 & 10 \\ 0 & -1 \end{bmatrix}$ and $A_2 = \begin{bmatrix} -1 & 0 \\ 10 & -1 \end{bmatrix}$. Both are Hurwitz. Show in one line that the switched system $\dot x = A_\sigma x$ has no [common quadratic Lyapunov function](/common-lyapunov-function/).

7. ◦ Find the [joint spectral radius](/joint-spectral-radius/) of $\left\{\begin{bmatrix} 0.5 & 3 \\ 0 & 0.9 \end{bmatrix}, \begin{bmatrix} 0.8 & -2 \\ 0 & 0.3 \end{bmatrix}\right\}$. Is the discrete-time switched system GUES under arbitrary switching?

8. ◦ A ball dropped from 1 m with $g = 9.81\ \mathrm{m/s^2}$ first hits the ground at $t_1 \approx 0.4515$ s. With a coefficient of restitution $e = 0.8$ instead of the $0.5$ of [Zeno behavior](/zeno-behavior/), at what time have all of its infinitely many bounces taken place?

9. ◦ Following the table of [mixed logical dynamical system](/mixed-logical-dynamical-system/), write the two inequalities for $[x \le 2] \Leftrightarrow [\delta = 1]$ when $x \in [-3, 5]$, and check them for $\delta = 0$ and $\delta = 1$. A PWA model with 2 modes is used in [hybrid MPC](/hybrid-mpc/) with horizon $N = 10$: how many QPs does full enumeration of the mode sequences solve?

10. • Run the [supremal controllable sublanguage](/supremal-controllable-sublanguage/) fixed point on the plant $0 \xrightarrow{a} 1$, $1 \xrightarrow{u} 2$, $2 \xrightarrow{b} 0$, $0 \xrightarrow{c} 3$, $3 \xrightarrow{u} 4$, $4 \xrightarrow{v} 5$, $5 \xrightarrow{d} 0$, $4 \xrightarrow{b} 0$, with $\Sigma_{uc} = \{u, v\}$ and marked state 0. The specification is the plant without the $v$ transition, all states marked. Give the states removed in each round, the result as a regular expression, and the events the supervisor disables.

11. • Show that the intersection of two prefix-closed controllable languages is controllable. Then explain where the argument fails for the languages $K_1 = \{a, aub\}$ and $K_2 = \{a, auc\}$ of [controllable language](/controllable-language/).

12. • Two machines of type 1 (places $p_1$ idle, $p_2$ busy) and two of type 2 ($p_3$ idle, $p_4$ busy) share a power supply: a busy machine of type 1 draws 2 units, one of type 2 draws 1, and 2 units are available, so $2\mu_2 + \mu_4 \le 2$. The transitions are $t_1: p_1 \to p_2$, $t_2: p_2 \to p_1$, $t_3: p_3 \to p_4$, $t_4: p_4 \to p_3$ and $\mu_0 = (2, 0, 2, 0)$. Build the monitor place by [supervision based on place invariants](/supervision-based-on-place-invariants/), and count the reachable markings of the plant and of the closed loop.

13. • In the mutual exclusion example of [supervision based on place invariants](/supervision-based-on-place-invariants/), suppose $t_1$ (process 1 enters its critical section) is uncontrollable. Show that the monitor for $\mu_2 + \mu_4 \le 1$ is not admissible, find the least restrictive behavior that still meets the constraint, and give a monitor place that enforces it.

14. • Let $\Sigma = \{a, b, u\}$ with $u$ unobservable, $L(G)$ the prefix closure of $\{ab, uaa\}$, and $K = \{\varepsilon, a, ab, u\}$. Show that $K$ is not [normal](/normal-language/) with respect to $L(G)$, and compute $\sup N(K)$ with the formula of Brandt et al.

15. • Build the [diagnoser](/diagnoser-automaton/) of the plant of Exercise 5 with lines L1 to L9 of the entry. How many states and transitions does it have, and after which observation does it report the fault?

16. • Change the plant of Exercise 5 so that state 4 has the self-loop $b$ instead of $a$. Run the [twin plant test](/twin-plant-diagnosability-test/): list the verifier states and edges, and give the flagged cycle and a pair of strings it stands for.

17. • Let $B = \begin{bmatrix} \varepsilon & 4 & \varepsilon \\ 1 & \varepsilon & 6 \\ \varepsilon & 2 & 1 \end{bmatrix}$, with an arc $j \to i$ of weight $B_{ij}$. List the elementary circuits and their means, and find the eigenvalue and an eigenvector given by the [max-plus eigenvalue theorem](/max-plus-eigenvalue-theorem/). Compare with what [Karp's algorithm](/karp-minimum-mean-cycle/) computes.

18. • Find the joint spectral radius of $\left\{\begin{bmatrix} 0 & 2 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}\right\}$ from the bounds with products of length 1 and 2. Both matrices are nilpotent; what does the answer say about switching between them?

19. • For the two modes of Exercise 6, switch periodically with each mode active for $h$ seconds. Explain why the state grows for small $h$, using $e^{A_2 h} e^{A_1 h} = e^{(A_1 + A_2)h} + O(h^2)$, and estimate the growth factor per period for $h = 0.1$.

20. • Let $A_1 = \begin{bmatrix} -1 & 2 \\ -8 & -1 \end{bmatrix}$ and $A_2 = \begin{bmatrix} -1 & 8 \\ -2 & -1 \end{bmatrix}$. Show that $P_1 = \mathrm{diag}(4, 1)$ and $P_2 = \mathrm{diag}(1, 4)$ satisfy $A_p^\top P_p + P_p A_p = -2 P_p$, and use Part 2 of the [dwell-time theorem](/dwell-time-theorem/) to give an average dwell time that ensures GUES.

21. • The plant $\dot x_1 = x_2$, $\dot x_2 = -x_1$ starts in the unit disk, and the unsafe set is $x_1 \ge 2$. Show that $B(x) = x_1^2 + x_2^2 - 2$ is a [barrier certificate](/barrier-certificate/), and that no function $B(x) = x_1 - c$ is one.

22. • For $\dot x = -2x + u$ with $|u| \le 1$ and $x(0) = 0$, compute the [reachable set](/reachable-set-computation/) at time $t$, its value at $t = 0.5$, and the set of states reachable at some time $t \ge 0$.

23. ★ Let $K \subseteq L(G)$ be prefix-closed, with no marking. Show that $\sup C(K)$ is the set of $s \in K$ such that no prefix $s'$ of $s$ has an uncontrollable continuation $t \in \Sigma_{uc}^*$ with $s't \in L(G) - K$. Turn this into one backward search on the product automaton, and show that it takes $O(nq)$ time.

24. ★ In a timed event graph where every place holds 0 or 1 token and every circuit holds at least one, show that the maximum cycle mean of $A = A_0^* \otimes A_1$ equals the largest ratio, over the circuits of the net, of the sum of holding times to the number of tokens.

25. ★ Let $A_1$ and $A_2$ be Hurwitz and commute. Let $P_1$ solve $A_1^\top P_1 + P_1 A_1 = -I$ and $P_2$ solve $A_2^\top P_2 + P_2 A_2 = -P_1$. Prove that $x^\top P_2 x$ is a common quadratic Lyapunov function, as in the example of [common Lyapunov function](/common-lyapunov-function/).

26. ★ The entry [common Lyapunov function](/common-lyapunov-function/) says that $A_1 = \begin{bmatrix} -1 & -1 \\ 1 & -1 \end{bmatrix}$, $A_2 = \begin{bmatrix} -1 & -10 \\ 0.1 & -1 \end{bmatrix}$ give a GUES switched system with no CQLF. Prove the GUES part: write $\dot\theta$ and $\frac{d}{dt}\ln r$ in polar coordinates for each mode, show that both modes turn the state the same way, and bound the change of $\ln r$ over one turn under the worst switching.

27. ★ Prove that a finite set of upper triangular $2 \times 2$ matrices $\begin{bmatrix} a_i & b_i \\ 0 & c_i \end{bmatrix}$ has joint spectral radius $r = \max_i \max(|a_i|, |c_i|)$, by bounding the entries of a product of length $k$.
