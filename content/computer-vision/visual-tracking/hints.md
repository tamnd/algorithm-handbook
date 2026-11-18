1. With $T = 0.5$: frame 2 cannot keep $(o_2, h_2)$ at IoU 0.4, so $o_2$ takes $h_3$, a switch, and $h_2$ is a false positive; frame 3 has a miss and the false positive $h_4$. That is 1 miss, 2 false positives and 1 switch in 6 objects: $\mathrm{MOTA} = 1/3$ and $\mathrm{MOTP} = 3.75/5 = 0.75$. With $T = 0.35$, frame 2 keeps $(o_2, h_2)$ and $h_3$ is the false positive; the switch moves to frame 3. MOTA stays $1/3$, and MOTP falls to $3.25/5 = 0.65$.

2. The matching $o_1 \to h_1$, $o_2 \to h_2$ gives $\mathrm{IDTP} = 11$; the next best gives 9. Then $\mathrm{IDP} = 11/19$, $\mathrm{IDR} = 11/18$ and $\mathrm{IDF1} = 22/37 \approx 0.595$.

4. $S^{-1} = \frac18 \begin{pmatrix} 3 & -2 \\ -2 & 4 \end{pmatrix}$, so $d^2 = 6$ for $(4, 4)$, which passes, and $d^2 = 12$ for $(4, -2)$, which fails. The Euclidean distances are 5.66 and 4.47, the other way round. The box is $|\nu_x| \le 6.07$, $|\nu_y| \le 5.26$, and both offsets lie in it. The area is $\pi \gamma \sqrt{\det S} \approx 81.8$.

7. The order by $w/\sigma$ is 0.15, 0.06, 0.005, and $|108 - 100| = 8 \le 10$, so the first component matches. The weights become 0.604, 0.297 and 0.099, $\rho \approx 1.35 \cdot 10^{-4}$ and the mean moves to about 100.001. The first two weights pass 0.7, so $B = 2$ and the pixel is background. The value 135 matches nothing, since $35 > 10$, $15 > 12.5$ and $75 > 50$; the third component becomes $(0.05, 135, 900)$, the others are scaled to $0.6 \cdot 0.95 / 0.9 \approx 0.633$ and $0.317$, and the pixel is foreground.

10. The kernel values are $5/9, 8/9, 1, 8/9, 5/9$, so $p = (13/35, 22/35)$ and the coefficient is about 0.924. The weights are $\sqrt{q_u / p_u}$: 1.421 for A and 0.631 for B, and $y_1 \approx 2.499$. The window moves toward the pixels of bin A, which the candidate has too little of.

12. A pair contributes $p_D L / \lambda = 40 L$ and a miss 0.2. The events weigh 0.04 (no pair), 1.6, 0.4, 0.8, 0.8 (one pair), 32 ($A z_1, B z_2$) and 8 ($A z_2, B z_1$); the sum is 43.64. Then $\beta_{A1} \approx 0.770$, $\beta_{A2} \approx 0.192$, $\beta_{A0} \approx 0.038$, $\beta_{B1} \approx 0.202$, $\beta_{B2} \approx 0.752$ and $\beta_{B0} \approx 0.047$. Alone, B would split evenly, 0.488 each: A's strong claim on $z_1$ pushes B to $z_2$.

13. Round one: the high boxes are the first and the third; A takes the first at IoU $9/11$. Round two: B meets the low box $(22,0,32,10)$ at IoU $2/3 \ge 0.5$ and takes it. C finds nothing and becomes lost; the box of score 0.05 is below $s_{\min}$. The box at $(60, 0)$ has score $0.8 \ge 0.7$ and starts an unconfirmed track. Without the second round, B is lost as well.

15. The cheapest is $(1, 2, 3)$ with cost 6. Its parts are: row 1 not in column 1 (best $(2, 1, 3)$, cost 10), and row 1 in column 1 with row 2 not in column 2 (best $(1, 3, 2)$, cost 16); the third part is empty. Pop 10 and split its part: row 1 in column 3 (best $(3, 2, 1)$, cost 13) and row 1 in column 2 with row 2 not in column 1 (best $(2, 3, 1)$, cost 16). Pop 13. The order is 6, 10, 13.

16. The first path is $s, b, c, d, t$ with cost $-3.3$. The second takes $c$ from $b$ by the reverse link: $s, a, c$, back to $b$, then $b \to e$, with cost $1 - 2 + 0.5 - 0.3 + 1.0 - 2 + 1 = -0.8$. The third would cost $+0.8$, so the method stops with $(a, c, d)$ and $(b, e)$ and a total of $-4.1$. $F = 0, -3.3, -4.1, -3.3$, which is convex.

19. $G = \begin{pmatrix} 10 & 3 \\ 3 & 2 \end{pmatrix}$ with eigenvalues 11 and 1, and $\sum (I - J) \nabla J = (12, 4)$, so $d = (12/11, 4/11)$. The smaller eigenvalue 1 is below 2, so the window fails the test: it is nearly an edge.

23. Choose the $k$ tracks that are detected, the $k$ measurements they take, and a bijection between them. For the recursion, the last track is either missed or takes one of the $m$ measurements. $E(5, 5) = 1546$ against $5! = 120$, and $E(10, 10) = 234\,662\,231$ against $3\,628\,800$.

24. If every detection is used, the number of tracks is the number of detections minus the number of links, so the cost is a constant plus $\sum (c_{ij} - c_{\text{en}} - c_{\text{ex}})$ over the links. A detection's incoming link and outgoing link lie in different frame pairs, so the pairs do not interact. In the example, frame pair (0, 1) takes $a_1 b_1$, saving 3 against 2.9; then $b_1 c_1$ is taken, and $c_2$ starts a track, for a total of 14. The optimum is $(a_2, b_1, c_1)$ and $(a_1, c_2)$, with cost 10.3.

25. The points are spaced $1/N$ apart, so an interval of length $\pi_k$ holds $\lfloor N \pi_k \rfloor$ or $\lceil N \pi_k \rceil$ of them; as $u$ is uniform, the mean is $N \pi_k$. For $N = 4$, the counts are $(2, 2, 0)$ with probability $1/5$ and $(2, 1, 1)$ with probability $4/5$. The variances are 0, 0.16 and 0.16, against $N \pi (1 - \pi) = 1$, 0.84 and 0.64 for multinomial draws.

26. The map $g(x) = x r / (x + r) + q$ is increasing with $g'(x) = r^2 / (x + r)^2$, which is at most $r^2 / (q + r)^2 < 1$ for $x \ge q$, and $g(x) \ge q$ for every $x \ge 0$. So $g$ is a contraction after one step. Its fixed point solves $x^2 - q x - q r = 0$. For $q = 1$ and $r = 2$, $P^- = 2$, the gain is $1/2$, $S = 4$ and the gate is $|\nu| \le \sqrt{6.635 \cdot 4} \approx 5.15$.

27. After two frames the weight of A after its match is $\alpha + (1 - \alpha)^2 w$, where $w$ is its value two frames before, a contraction with factor $(1 - \alpha)^2$. The fixed point is $1/(2 - \alpha)$, and the other weight is $(1 - \alpha)$ times it; any third weight decays like $(1 - \alpha)^t$. With equal variances the matched component comes first. If $T < 1/(2 - \alpha)$ it alone is enough; otherwise the first two together have weight near 1, which exceeds $T$.
