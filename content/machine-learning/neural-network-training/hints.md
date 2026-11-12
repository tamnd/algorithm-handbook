1. Forward: $z_1 = 0.5$, $a_1 = 0.5$, $\hat y = 1.5$, loss $0.125$. Backward: $\delta_2 = \hat y - y = 0.5$, so $\partial/\partial w_2 = \delta_2 a_1 = 0.25$ and $\partial/\partial b_2 = 0.5$. Then $\delta_1 = w_2 \delta_2 \cdot \mathrm{relu}'(z_1) = 1.5$, so $\partial/\partial w_1 = \delta_1 x = 3$ and $\partial/\partial b_1 = 1.5$.

3. Xavier: standard deviation $\sqrt{2/2048} = 0.03125$ and $a = \sqrt{6/2048} \approx 0.0541$. He: $\sqrt{2/1024} \approx 0.0442$ and $a = \sqrt{6/1024} \approx 0.0765$. Xavier has half the He variance, and each layer multiplies the mean square by $n\sigma^2/2$, so the last layer is smaller by $2^{-20} \approx 9.5 \times 10^{-7}$.

6. The mean is 5 and the biased variance 5, so $\hat x = (-3, -1, 1, 3)/\sqrt 5$ and $y = 2\hat x + 1 \approx (-1.683, 0.106, 1.894, 3.683)$. At inference the variance is $\frac43 \cdot 5 = 20/3$, and the output for 10 is $2 \cdot 5/\sqrt{20/3} + 1 \approx 4.873$.

8. After $r$ rounds a fraction $0.8^r$ is left. Since $0.8^{10} \approx 0.107$ and $0.8^{11} \approx 0.086$, it takes 11 rounds, and about 8.6% of the weights remain.

10. $P = 784 \cdot 512 + 512 \cdot 256 + 256 \cdot 10 = 535{,}040$, so backpropagation needs at most $1{,}605{,}120$ multiply-adds. Forward differences need $(P + 1)P \approx 2.86 \times 10^{11}$, about $178{,}000$ times more. The Jacobian takes 1000 forward-mode runs, one per input direction, or 10 reverse sweeps, one per output.

11. The states are $h = (1, 0.5, 0.25)$. With $\delta_3 = h_3 = 0.25$ and $\delta_{t-1} = w\,\delta_t$, the terms $\delta_t h_{t-1}$ are $0.125$, $0.125$ and $0$, so $\partial L/\partial w = 0.25$. Check: $h_3 = w^2$, so $\partial L/\partial w = h_3 \cdot 2w = 0.25$. Truncation keeps only the first term, $0.125$, half the true value.

13. Find the least $r$ with $\binom{c + r}{c} \ge 1000$. For $c = 5$: $\binom{12}{5} = 792$ and $\binom{13}{5} = 1287$, so $r = 8$. For $c = 10$: $\binom{13}{10} = 286$ and $\binom{14}{10} = 1001$, so $r = 4$.

14. For the first matrix $R = (5, 10)$, $C = (3, 12)$ and $\mathbf{1}^\top R = 15$, which gives $V$ back exactly, because $V$ has rank one. For $I_2$ every entry of $\hat V$ is $1/2$: the row and column sums are kept, the diagonal structure is lost. Adam keeps $2 \cdot 4096^2 = 33{,}554{,}432$ numbers, 128 MiB; the factored moment keeps 8192 numbers, 32 KiB.

16. Cross-entropy: $0.1054$ and $2.3026$; focal: $0.01 \cdot 0.1054 \approx 0.00105$ and $0.81 \cdot 2.3026 \approx 1.865$. The easy group sums to $100.5$ against $12.04$ for the hard group under the cross-entropy, and to $0.0101$ against $5.90$ under the focal loss.

19. Half the smallest subnormal is $2^{-25} \approx 2.98 \times 10^{-8}$, so $10^{-8}$ rounds to 0. Scaled by $2^{16}$ it is about $6.55 \times 10^{-4}$, above $2^{-14} \approx 6.10 \times 10^{-5}$, a normal number. The scale $2^{12}$ gives $40{,}960$ and $2^{13}$ gives $81{,}920 > 65504$, so the answer is $2^{12}$.

22. The moments are $v = 50, 25.5, 13.25, 7.125$, and $\hat v_t = 50$ throughout. Adam's steps are $0.1414, 0.0198, 0.0275, 0.0375$; AMSGrad's are $0.1414, 0.0141, 0.0141, 0.0141$. Adam's effective rate $\alpha/\sqrt{v_t}$ grows as the large gradient leaves the average; the maximum stops that.

24. Here $Z = 3 + e^w = 6$ and $p(v = 1) = (1 + e^w)/Z$, so the gradient is $\sigma(w) - e^w/Z = 3/4 - 1/2 = 1/4$. For CD-1, $h_0 = 1$ with probability $3/4$, and then $v_1 = 1$ with probability $\sigma(w h_0)$, so $P(v_1 = 1) = \frac34 \cdot \frac34 + \frac14 \cdot \frac12 = 11/16$. The update is $3/4 - \frac{11}{16} \cdot \frac34 = 15/64$, a bias of $-1/64$.

25. (a) The Fisher block has $(1024 \cdot 4096)^2 = 2^{44} \approx 1.76 \times 10^{13}$ entries; the factors have $1024^2 + 4096^2 = 17{,}825{,}792$. (b) Divide the rows by 4 and 1, then the columns by 1 and 2: $X = \begin{pmatrix} 1 & 0.25 \\ 1 & 3 \end{pmatrix}$, and $G X \bar A^\top$ gives back $\nabla_W h$.

26. The gradient in $(w, v)$ is $(v x, \mathrm{relu}(w x))$, which is $(2, 1)$ at $x = 1$ and $(6, 3)$ at $x = 3$, so $\Theta(1, 1) = 5$, $\Theta(1, 3) = 15$ and $\Theta(3, 3) = 45$. The step gives $(w, v) = (0.96, 1.98)$. Then $f(1)$ moves by $-0.0992$ against the prediction $-0.1$, and $f(3)$ by $-0.2976$ against $-0.3$; the gaps are of order $\eta^2$.

27. Multiply both filters by $s$ and set $x = \eta s$: the ratio is $(1 - (1 - x)^t)(1 + tx)/(tx)$, which is $2$ at $x = t = 1$. As $x \to 0$ with $tx = u$, $(1 - x)^t \to e^{-u}$ and the ratio tends to $(1 - e^{-u})(1 + u)/u$. Its maximum is about $1.298$, near $u \approx 1.79$.
