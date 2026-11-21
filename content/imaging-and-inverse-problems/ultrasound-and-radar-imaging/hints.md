1. The depth is $z = ct/2 = 1540 \cdot 26 \times 10^{-6}/2 = 20.0$ mm. An echo from 150 mm needs $2 \cdot 0.150/1540 = 194.8$ µs, so the PRF is at most $5133$ Hz.

2. The levels in dB are $-6.02$, $-26.02$ and $-60$, the last one clipped to $-60$. The gray levels are $\lfloor 255 \cdot 0.8997 + 0.5\rfloor = 229$, $\lfloor 255 \cdot 0.5663 + 0.5 \rfloor = 144$ and $0$.

5. The wrapped values are $(0, 1.5, 3.0, -1.7832, -0.2832, 1.2168)$. Every wrapped difference is $1.5$, so integration gives back $(0, 1.5, 3.0, 4.5, 6.0, 7.5)$. For $(0, 3.5)$, the wrapped value is $3.5 - 2\pi = -2.7832$, its wrapped difference is also $-2.7832$, and integration returns $-2.7832$: the true step is above $\pi$, so Itoh's condition fails and the result is off by $2\pi$.

6. $v_a = c\,\mathrm{PRF}/(4f_0) = 1540 \cdot 4000/(12 \times 10^6) = 0.513$ m/s. At $0.3$ m/s the Doppler shift is $2vf_0/c = 1168.8$ Hz, and the phase step is $2\pi \cdot 1168.8/4000 = 1.836$ rad. A velocity of $0.7$ m/s aliases to $0.7 - 2v_a = -0.327$ m/s.

7. $|\sum s_i|^2 = 16$ and $M\sum|s_i|^2 = 4 \cdot 6 = 24$, so $\mathrm{CF} = 2/3$. Delay-and-sum gives $4$, and the weighted value is $8/3 = 2.67$.

10. $L_s = 0.03 \cdot 10^4/1.5 = 200$ m, so the integration time is $L_s/V = 1$ s. The Doppler bandwidth is $2V/L = 266.7$ Hz, and the FM rate $2V^2/(\lambda R_0)$ is $266.7$ Hz/s, consistent with $266.7$ Hz over 1 s. The migration is $\sqrt{R_0^2 + 100^2} - R_0 = 0.50$ m, about $L_s^2/(8R_0)$. The range resolution is $c/(2B) = 0.5$ m, so the migration is one resolution cell and must be corrected.

11. The products are $\bar 1 \cdot i = i$, $\bar i \cdot (-1) = i$ and $\overline{(-1)} \cdot 1 = -1$, so $R_1 = -1 + 2i$ with $\arg R_1 = 2.034$ rad. Then $v = 1540 \cdot 4000 \cdot 2.034/(4\pi \cdot 5 \times 10^6) = 0.199$ m/s, below $v_a = 0.308$ m/s.

13. $R^{-1} = \frac17\begin{pmatrix} 2 & -1 \\ -1 & 4\end{pmatrix}$, so $R^{-1}a = \frac17(1, 3)$ and $a^{\mathsf H}R^{-1}a = 4/7$. The weights are $w = (1/4, 3/4)$, with $w^{\mathsf H}a = 1$. The Capon power is $1/(a^{\mathsf H}R^{-1}a) = 7/4$; delay-and-sum gives $a^{\mathsf H}Ra/4 = 8/4 = 2$. Capon puts more weight on the quieter channel.

16. The wrapped differences around the first loop are $2.1$, $2.0832$, $2.6$ and $-0.5$, with sum $2\pi$: a residue of charge $+1$. The second loop has the differences $1, 1, -1, -1$, with sum $0$. Only the first loop holds a residue, and the algorithm must join it by a cut to a residue of charge $-1$ or to the border.

17. The signed square roots are $r = (1, 2, -3, 4)$. The six pair terms are $2, -3, 4, -6, 8, -12$, with sum $-7$. The formula gives $((\sum r)^2 - \sum r^2)/2 = (16 - 30)/2 = -7$. Delay-and-sum gives $12$.

21. The sum of $L$ independent exponentials of mean 1 is gamma with $P(S > s) = e^{-s}\sum_{k<L} s^k/k!$. With $L = 4$ and $s = 2L = 8$, the probability is $e^{-8}(1 + 8 + 32 + 85.33) = 4.24\%$, against $13.5\%$ for one look. A simulation with seed 21 and 200 000 runs gives $4.28\%$.

22. With the matrix inversion lemma, $R^{-1} = I - P\,bb^{\mathsf H}/(1 + 2P)$. Then $a^{\mathsf H}R^{-1}a = 2 - 2P/(1 + 2P) = (2 + 2P)/(1 + 2P)$, so the output power is $201/202 = 0.995$. Also $a^{\mathsf H}R^{-1}b = a^{\mathsf H}b/(1 + 2P)$, which gives the gain $1/(2(1 + P)^2) = 4.9 \times 10^{-5}$. Delay-and-sum has the gain $0.5$ and the output power $(2 + 2P)/4 = 50.5$.

23. The phase differences are $0.5$, $1.0$ and $1.5$, with mean gradient $1.0$. The corrected differences $-0.5$, $0$, $0.5$ integrate to $(0, -0.5, -0.5, 0)$. Its best line is the constant $-0.25$, so the estimate is $(0.25, -0.25, -0.25, 0.25)$. The best line of $\varphi$ is $-0.25 + k$, and $\varphi$ minus that line is the same vector. One iteration is exact here because there is one scatterer and no clutter; the linear part is lost, as it always is.

24. The singular values are $14.16$ and $0.706$. The residual is $\sigma_2 u_2 v_2^{\mathsf T}$, with power $0.00125$ in the tissue pixel and $0.4975$ in the blood pixel, against $1$ before. The blood signal $(0, 1)$ is not orthogonal to the tissue signal $(1, 1)$, and the filter removes nearly all of its component along $(1, 1)/\sqrt2$, which holds half of its power.

25. On the detector, $p = (r - ct)/(2r)$ for $|r - ct| < a$. At the centre, the time is $t = r/c = 16.67$ µs, where $p = 0$ and $\partial p/\partial t = -c/(2r)$. So $b = 0 - 2(r/c)(-c/(2r)) = 1 = p_0$ for every detector, and the solid angle weights add to 1.
