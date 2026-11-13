1. ◦ Use the [blocks world](/blocks-world/) with a hand: $\mathit{pickup}(x)$ needs $\mathit{clear}(x)$, $\mathit{ontable}(x)$ and $\mathit{handempty}$; $\mathit{stack}(x, y)$ needs $\mathit{holding}(x)$ and $\mathit{clear}(y)$; $\mathit{unstack}(x, y)$ needs $\mathit{on}(x, y)$, $\mathit{clear}(x)$ and $\mathit{handempty}$. Start from the state with C on A and A and B on the table, and apply $\mathit{unstack}(C, A)$, $\mathit{stack}(C, B)$, $\mathit{pickup}(B)$ as [STRIPS](/strips/) actions. Write the state after each action, and name the first action that cannot be applied and the precondition it lacks.

2. ◦ In the encoding of Exercise 1, $\mathit{stack}(x, y)$ adds $\mathit{on}(x, y)$, $\mathit{clear}(x)$ and $\mathit{handempty}$ and deletes $\mathit{holding}(x)$ and $\mathit{clear}(y)$. [Regress](/goal-regression/) the goal $\{\mathit{on}(A, B), \mathit{on}(B, C)\}$ through $\mathit{stack}(A, B)$ and through $\mathit{stack}(B, C)$. Is each result true in some state that can be reached from a legal blocks state?

3. ◦ A task has $I = \{p\}$, $G = \{g_1, g_2\}$ and three unit-cost actions: $a$ needs $p$ and adds $q$; $b$ needs $q$, adds $g_1$ and deletes $q$; $c$ needs $q$ and adds $g_2$. Compute [$h^{\max}$](/h-max-heuristic/), [$h^{\mathrm{add}}$](/h-add-heuristic/), $h^{+}$ and $h^*$ at $I$, and give an optimal plan. Which of the four values are lower bounds on $h^*$ for every task?

4. ◦ A hand can hold one object. $\mathit{pick}_x$ needs $\mathit{he}$ (hand empty) and $x_t$ (x on the table), adds $h_x$ and deletes $\mathit{he}$ and $x_t$; $\mathit{box}_x$ needs $h_x$, adds $x_b$ (x in the box) and $\mathit{he}$, and deletes $h_x$; the same for $y$. From $\{\mathit{he}, x_t, y_t\}$ with goal $\{x_b, y_b\}$, build the [planning graph](/planning-graph/) with [mutexes](/mutex-relation/). At which level do both goals first appear, and at which level are they first not mutex?

5. ◦ Give the complexity class for which each problem is complete: (a) whether a propositional STRIPS task has a plan; (b) whether it has a plan of at most $k$ actions, $k$ in unary; (c) the same with $k$ in binary; (d) whether a delete-free task with positive preconditions and goals has a plan; (e) whether such a task has a plan of at most $k$ actions, $k$ in binary; (f) whether a [conformant plan](/conformant-planning/) exists for a compact model.

6. ◦ A [stochastic shortest path](/stochastic-shortest-path/) problem has states $s_1$, $s_2$ and a goal. In $s_1$, action $a$ costs 1 and leads to $s_2$, and $b$ costs 4 and leads to the goal. In $s_2$, $c$ costs 1 and leads to the goal with probability 0.8 and back to $s_1$ with probability 0.2, and $d$ costs 2 and leads to the goal. Run three rounds of synchronous value iteration from $V = 0$. Then solve the [Bellman equation](/bellman-equation/) for $V^*$ and give the optimal policy.

7. ◦ A [partial-order plan](/partial-order-plan/) has five steps and the orderings $1 \prec 2$, $1 \prec 3$, $2 \prec 4$ and $3 \prec 4$; step 5 is not ordered with any of them. How many linearizations does it have?

8. ◦ A tiger is behind the left or the right door, each with probability $1/2$. Listening reports the correct side with probability 0.85. Compute the [belief](/belief-space/) that the tiger is on the left after hearing "left" once and twice. How many "left" reports in a row are needed before the belief exceeds 0.99?

9. ◦ In the plane, an obstacle is a square of side 2. Give the area of the [C-obstacle](/configuration-space/) for a disc robot of radius 1, and for an axis-parallel unit square robot that translates without rotating, with its center as the reference point.

10. ◦ A corridor has cells 1 to 4 with walls at both ends; $L$ moves one cell left and $R$ one cell right, and a move into a wall leaves the robot where it is. The robot does not know its cell and cannot sense. Give a shortest conformant plan that ends in cell 3.

11. • The $n$-bit counter has facts $\mathit{on}_i$ and $\mathit{off}_i$ for $i = 1, \dots, n$. Action $\mathit{inc}_i$ needs $\mathit{off}_i$ and $\mathit{on}_1, \dots, \mathit{on}_{i-1}$, adds $\mathit{on}_i$ and $\mathit{off}_1, \dots, \mathit{off}_{i-1}$, and deletes its preconditions. All bits start off and the goal is all bits on. Compute $h^{\max}$, $h^{\mathrm{add}}$, $h^{+}$ and $h^*$ at the start for $n = 3$, then give each as a function of $n$.

12. • A state $s$ has two actions to the goal: *safe* costs 3 and always arrives; *risky* costs 1 and arrives with probability $1/2$, and otherwise stays in $s$. Run value iteration from $V(s) = 0$, give $V_k(s)$ in closed form, and find the first $k$ with $V^*(s) - V_k(s) \le 0.01$. Which action is optimal?

13. • A [probabilistic roadmap](/probabilistic-roadmap/) works in a free space of area 1 in the plane, and a path of length $1.5$ has clearance $\rho = 0.05$. Use the failure bound $\lceil 2L/\rho \rceil e^{-\sigma \rho^d n}$ with $\sigma = \zeta_d / (2^d \mu(\mathcal{C}_{free}))$ to find the number of samples $n$ that brings it below 0.01. What does the bound say for $n = 1000$?

14. • Run one trial of [RTDP](/real-time-dynamic-programming/) on the problem of Exercise 6 from $V = 0$, starting at $s_1$, with greedy actions. The outcomes are: back to $s_1$ on the first visit to $s_2$, and the goal on the second. Give each backup. Compare the values with $V^*$.

15. • The [bug algorithms](/bug-algorithms/) meet two obstacles of perimeters 4 and 6, and the start is at distance $D = 10$ from the goal. The line from start to goal crosses the first boundary twice and the second four times. Give the proved bounds on the path length of Bug1 and Bug2. Which bound is smaller here, and why can the order change on other maps?

16. • A partial plan has the steps Start, which adds $a$; $S_1$, which needs $a$, adds $b$ and deletes $a$; $S_2$, which needs $a$ and adds $c$; and Finish, which needs $b$ and $c$. Its [causal links](/causal-link/) are $\mathrm{Start} \xrightarrow{a} S_1$, $\mathrm{Start} \xrightarrow{a} S_2$, $S_1 \xrightarrow{b} \mathrm{Finish}$ and $S_2 \xrightarrow{c} \mathrm{Finish}$. Find every threat, say whether promotion or demotion resolves it, and give the linearizations before and after.

17. • In [plan recognition](/plan-recognition/) with $\beta = 1$ and a uniform prior over goals $G_1$, $G_2$, $G_3$, the cheapest plans that embed the observations $O$ cost 10, 14 and 11, and the cheapest plans that avoid them cost 12, 10 and 11. Compute $P(O \mid G)$ for each goal and the posterior $P(G \mid O)$.

18. • A nondeterministic domain has states $s_0$, $s_1$, the goal $g$ and a dead end $d$. In $s_0$, action $a$ leads to $g$ or $s_1$. In $s_1$, $b$ leads to $s_0$, and $c$ leads to $s_1$ or $d$. Does a weak, a strong, or a strong cyclic plan from $s_0$ exist, in the sense of [planning as model checking](/planning-as-model-checking/)? Give the plans that exist.

19. • [Ground](/grounding/) two blocks-world domains with $n$ blocks. The first has the four schemas of Exercise 1. The second has one schema $\mathit{move}(b, x, y)$, where $b$ is a block, $x$ and $y$ are blocks or the table, and $b$, $x$, $y$ are distinct. Count the ground actions of each as a function of $n$, and give the counts for $n = 3$ and $n = 4$.

20. • In [temporal planning](/temporal-planning/), a truck must load (2 time units), charge (4) and then drive (5) and unload (1); drive needs both load and charge to have ended, and load and charge may overlap. Give the shortest makespan and the makespan of the best sequential plan. Then take a door that stays open only while the durative action *hold* (5 units) runs, and a durative action *carry* (2 units) that needs the door open throughout. Explain why no plan without overlapping actions exists.

21. • A robot runs the plan *pick*, *go*, *drop*. Here *pick* needs $\mathit{athome}$ and $\mathit{pkghome}$, adds $\mathit{holding}$ and deletes $\mathit{pkghome}$; *go* needs $\mathit{athome}$, adds $\mathit{atoffice}$ and deletes $\mathit{athome}$; *drop* needs $\mathit{atoffice}$ and $\mathit{holding}$ and adds $\mathit{pkgoffice}$. The goal is $\{\mathit{pkgoffice}\}$. Compute the regressed conditions $K_0, \dots, K_3$ of the suffixes, and say what an [execution monitor](/execution-monitoring/) does in the observed states $\{\mathit{athome}, \mathit{holding}\}$, $\{\mathit{atoffice}, \mathit{holding}\}$ and $\{\mathit{atoffice}, \mathit{pkghome}\}$.

22. • In the planning graph of Exercise 4, explain from the mutex rules why $x_b$ and $y_b$ are mutex at level 2 and still mutex at level 3. Why does every plan for this task have 4 actions, and why does it also have 4 parallel steps?

23. • A two-state POMDP with horizon 1 has the actions $A$, $B$, $C$ with rewards $(1, -1)$, $(-1, 2)$ and $(0.5, 0.5)$ in the states $(s_1, s_2)$. With $b = P(s_1)$, write the optimal value $V_1(b)$ and the interval of beliefs where $C$ is best. [Point-based value iteration](/point-based-value-iteration/) on the points $b = 0.1$ and $b = 0.9$ keeps one vector per point. Which vectors does it keep, and how far below $V_1$ is its value at worst?

24. ★ Prove that plan existence is decidable in polynomial time for STRIPS tasks in which no action has a precondition and the goal is a set of positive facts. (Bylander states this case; the [plan existence page](/strips-plan-existence-pspace-complete/) lists it without proof.)

25. ★ In the corridor of Exercise 10 with $n$ cells, prove that the shortest conformant plan from total uncertainty to cell $j$ has $n - 1 + \min(j - 1, n - j)$ actions.

26. ★ Show that a Bellman backup keeps the values of RTDP at most $V^*$ when they start at most $V^*$. Then give a two-state problem and a start $h$ that overestimates at one state, on which RTDP settles on a policy that is not optimal at the start state.

27. ★ In the model of Exercise 17, let $\beta \to \infty$ with a uniform prior. Describe the limit of the posterior $P(G \mid O)$ in all cases: some goal has $\Delta(G, O) > 0$; none does but some has $\Delta = 0$; and all have $\Delta < 0$.

28. ★ Prove that the C-obstacle of a disc robot of radius $r$ around a convex polygon with area $A$ and perimeter $P$ has area $A + P r + \pi r^2$. Check the formula against Exercise 9.
