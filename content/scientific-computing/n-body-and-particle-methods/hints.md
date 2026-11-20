1. The pair distances are 1, 2 and $\sqrt5$, so $U = -(2 + 1 + 1/\sqrt5) = -3.447214$. The forces are $F_1 = (2, 0.5)$, $F_2 = (-2.089443, 0.178885)$ and $F_3 = (0.089443, -0.678885)$. Each pair force enters twice with opposite signs, so the sum is zero to rounding.

2. CIC gives 0.7 to node 3 and 0.3 to node 4. TSC gives 0.02, 0.66 and 0.32 to nodes 2, 3 and 4. The 2D weights are products of the 1D ones: 0.175 to $(3, 5)$, 0.525 to $(3, 6)$, 0.075 to $(4, 5)$ and 0.225 to $(4, 6)$.

4. The digits from the top bit down are 6, 5 and 3, so the key is octal 1653, or 939. The parent drops the last digit: octal 165, or 117. The children are $8 \cdot 939 + c$ for $c = 0, \dots, 7$, which is 7512 to 7519. The key has 10 bits, and $(10 - 1)/3 = 3$ is its level.

5. The angle is $2\arctan(\Omega h / 2)$. At $\Omega h = 1$ it is 0.927295, 7.3% short, so a gyration takes 6.78 steps. At $\Omega h = 0.1$ it is 0.0999168, short by $8.3 \times 10^{-4}$ in relative terms. The rotation is exact, so the speed does not change.

8. The leapfrog is stable for $\omega_p h < 2$. At $h = 0.2$ one period $2\pi$ takes 31.4 steps. Here $\lambda_D = 0.05$, and $4\pi / 0.05 = 251.3$, so at least 252 cells are needed.

10. Sum the two exact terms, $\frac{1/2}{1.5} + \frac{1/2}{2.5}$, and expand $\frac{1}{d - b} + \frac{1}{d + b}$ in general. The error is $b^2 / (d (d^2 - b^2))$, and the ratio of the bound to it reduces to $(d + b)/d$.

11. The monopole sits at $(3, 0)$ and gives $A$ the force $1/9$ from each unit of mass. The exact force on $B$ from $A$ has the $x$-component $-3/(9.25)^{3/2}$, and the forces between $B$ and $C$ cancel in the sum. The total is the gap between $2/9$ and $6/(9.25)^{3/2}$, about $0.0089$ in $x$, so the momentum drifts at that rate.

16. The error scales as $h^2$, so the number of steps scales as the square root of the error ratio. The ratio is 1170 for the position, which gives $20\sqrt{1170} = 684.1$, so 685 steps. For the energy, $40\sqrt{2.1 \times 10^{-4}/1.9 \times 10^{-6}} = 421$.

18. Map the interaction list to a square of children. Each box sees the $6 \times 6$ block of children of its parent's $3 \times 3$ neighbourhood, minus its own $3 \times 3$ neighbours, with both blocks clipped at the edges. Summing over all boxes factors into a product over the two axes. Along one axis the parent blocks give $6n - 8$ in total and the neighbour blocks $3n - 2$, so the total is $(6n - 8)^2 - (3n - 2)^2$.

19. Equate $v^2/r$ with the softened acceleration $G M r/(r^2 + \epsilon^2)^{3/2}$. The speed peaks at $r = \sqrt2\,\epsilon$, where $v^2 = 2/(3\sqrt3) = 0.3849$ in units of $G M/\epsilon$. The period ratio is $((r^2 + \epsilon^2)/r^2)^{3/4}$, which is $2^{3/4} = 1.682$ at $r = \epsilon$ and 1.0075 at $10\epsilon$. Inside a few $\epsilon$ the orbits are those of a different force law.

20. Solve $x^2 = 0.01 (1 - x)$ for $x = \sqrt3\theta$. The root is $x = 0.0951$, so $\theta = 0.0549$. The bound is 0.562 at $\theta = 0.3$ and 5.60 at $\theta = 0.5$. It assumes that the mass sits as far from the centre of mass as the cell allows, $\sqrt3$ times the side, and that the error points the worst way. In a real sum most cells are far from that case, and the errors of many cells partly cancel.

21. Differentiate: the two terms from $\operatorname{erfc}$ and from the factor $u$ cancel, which leaves $f'(u) = -\frac{u^2}{2\sqrt\pi} e^{-u^2/4} < 0$. The values are 0.918891, 0.572407 and 0.017533, and bisection gives $f = 10^{-3}$ at $u = 5.70$.
