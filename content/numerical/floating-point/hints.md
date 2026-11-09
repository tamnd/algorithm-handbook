1. $-6.5 = -1.101_2 \times 2^2$. The sign bit is 1, the biased exponent is $2 + 127 = 129 = 10000001_2$, and the fraction is $101$ followed by twenty zeros. The word is `0xC0D00000`.

3. Binary32 holds every integer up to $2^{24}$, so the answer is $2^{24} + 1 = 16777217$, and it rounds to $2^{24}$. For binary64 it is $2^{53} + 1 = 9007199254740993$, which rounds to $2^{53}$. Both are ties, and ties to even pick the power of 2.

5. They give $0, 2, 2, 4$. Halfway cases go up as often as they go down, so their errors cancel on average.

7. The answers are $1/2$, $1001$ and $700$. The square root is well conditioned everywhere, the subtraction is ill conditioned near $x = 1$, and $e^x$ magnifies relative errors by $|x|$.

9. The sum $x + 1$ rounds to $x$, so the computed difference is $0$; the true value is about $5.0 \times 10^{-9}$. Multiply and divide by $\sqrt{x + 1} + \sqrt{x}$.

10. $\cos(10^{-8}) = 1 - 5 \times 10^{-17}$ to first order, which is within half an ulp of 1 below 1. Use $1 - \cos x = 2\sin^2(x/2)$.

12. Expand $(1 + 2^{-30})^2$. The last term is below half an ulp of 1. You should find $p = 1 + 2^{-29}$ and $e = 2^{-60}$.

14. The values are $5$, $4$ and $36$.

15. The bit patterns of positive floats are ordered like the floats. Every pattern from 1 up to the pattern of $1.0$ minus one is a float in $(0, 1)$. The answer is $1023 \cdot 2^{52} - 1$.

16. The answer is $n = 49$, and the product is $1 - 2^{-53}$, the float just below 1.

19. Every addition $s + u$ with $s = 1$ is a tie between $1$ and $1 + 2^{-52}$, and ties to even keeps $1$. The computed sum stays $1$, the exact sum is $1 + 1000u$, and the relative error is $1000u/(1 + 1000u) \approx 1.11 \times 10^{-13}$.

20. If the signs agree, then $|a| \le |s| \le 2|a|$. If they differ and $|b| \le |a|/2$, then $|a|/2 \le |s| \le |a|$. In both cases the lemma applies to $s$ and $a$. If they differ and $|b| > |a|/2$, the lemma applies to $a$ and $-b$, so $s = a + b$ exactly and $z = b$.

21. $x + 0.5 = 1 - 2^{-54}$ lies halfway between $1 - 2^{-53}$ and $1$. Near $2^{52}$ the spacing is $1$, so $2^{52} + 1.5$ is a tie between two integers. The result is $2^{52} + 2$.

22. $q = 6004799503160661 \times 2^{-54}$, so $3q = (2^{54} - 1) \times 2^{-54} = 1 - 2^{-54}$. That value lies halfway between $1 - 2^{-53}$ and $1$, and ties to even rounds it up.
