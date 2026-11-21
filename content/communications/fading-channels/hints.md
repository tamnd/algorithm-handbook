1. $20\log_{10} 0.2 + 20\log_{10} 5800 + 32.45 = -13.98 + 75.27 + 32.45 = 93.74$ dB.

2. The mean delay is $0.6 + 0.5 = 1.1$ microseconds and $\sigma_\tau = \sqrt{0.6 \cdot 1.21 + 0.3 \cdot 0.81 + 0.1 \cdot 15.21} = \sqrt{2.49} = 1.578$ microseconds. Fleury gives $B_c(0.5) \ge 1/(6\sigma_\tau) = 105.6$ kHz and the rule gives 126.7 kHz. The exact first crossing of 0.5 is at about 194.7 kHz, so here both are below the true value.

3. $f_D = (33.33 \text{ m/s})(3.5 \cdot 10^9)/(3 \cdot 10^8) = 388.9$ Hz. The correlation falls to 0.5 at $0.2421/f_D = 0.623$ ms; the rule gives $0.423/f_D = 1.09$ ms, which lies past the first zero of $J_0$.

5. $1 - e^{-10^{-1.5}} = 1 - e^{-0.0316} = 0.0311$. The median power is $\Omega\ln 2$, which is 1.59 dB below the mean.

6. $P_{\text{out}} = 1 - e^{-(2^2 - 1)/100} = 0.0296$. At 30 dB, $C_{0.01} = \log_2(1 - 1000\ln 0.99) = \log_2 11.05 = 3.47$ bits per channel use.

7. MRC: $|h_1|^2 + |h_2|^2 = 4 + 2 = 6$. SC: the stronger branch, $4$. EGC: $(|h_1| + |h_2|)^2/(2N_0) = (2 + \sqrt2)^2/2 = 3 + 2\sqrt2 = 5.83$, between the other two.

8. $\pi_B = p/(p + r) = 1/11 = 0.0909$, the mean error rate is $\pi_B e_B = 0.0455$, and the periods are geometric with means $1/r = 5$ bits (bad) and $1/p = 50$ bits (good).

12. The amount of fading is $\mathbb{E}|h|^4 - 1 = 0.5$. Solving $(2K + 1)/(K + 1)^2 = 0.5$ gives $K^2 - 2K - 1 = 0$, so $K = 1 + \sqrt2 = 2.414$, and $m = 1/0.5 = 2$. The tails are $(1 + K)e^{-K} \cdot 0.01 = 3.05 \cdot 10^{-3}$ for Rician and $(m^m/m!)\,x^m = 2 \cdot 10^{-4}$ for Nakagami. Same two moments, but slope 1 against slope 2.

13. The threshold is $x = (2^1 - 1)/10 = 0.1$. SC gives $(1 - e^{-0.1})^L = 0.0952^L$, which is $8.6 \cdot 10^{-4}$ at $L = 3$. MRC gives $4.68 \cdot 10^{-3}$ at $L = 2$ and $1.55 \cdot 10^{-4}$ at $L = 3$. Both need three branches.

15. Propagate the row vector of state probabilities, multiplying by the probability of a correct bit in each state and then by the transition matrix. The result is $0.681$, against $(1 - 0.0455)^{20} = 0.394$ for the binary symmetric channel. Since $e_G = 0$, an error means the bad state, so $\Pr[Z_{t+1} = 1 \mid Z_t = 1] = (1 - r)e_B = 0.4$, almost nine times the mean error rate.

22. For the correlation, the terms with $n \ne m$ vanish because the phases are independent and uniform; each term with $n = m$ gives $\mathbb{E}\,e^{j 2\pi f_D\tau\cos\alpha} = J_0(2\pi f_D\tau)$. For the fourth moment count the index quadruples with $\{n_1, n_2\} = \{n_3, n_4\}$: there are $2N^2 - N$. A unit-power circular Gaussian has $\mathbb{E}|h|^4 = 2$, so a finite sum is never exactly Rayleigh, whatever its correlation.

23. Write the maximum as a sum of spacings of the order statistics: by the memoryless property the gap between the $k$th and $(k+1)$th smallest of $L$ exponentials is exponential with mean $\bar\gamma/(L - k)$. Summing gives $H_L\bar\gamma$. For $L = 4$ the gain is $25/12$, or 3.19 dB.

24. At high SNR the difference tends to $-\mathbb{E}\log_2|h|^2$. For $|h|^2$ exponential with mean 1, $\mathbb{E}\ln|h|^2 = \int_0^\infty \ln x\, e^{-x}\, dx = \Gamma'(1) = -\gamma_E$. The loss is $0.5772 \cdot 1.4427 = 0.833$ bits, which is $10\log_{10} 2^{0.833} = 2.51$ dB of SNR.

25. The power is $(1/\gamma_0 - 1/\gamma)^+$ times the average, so the cutoff solves $\int_{\gamma_0}^\infty (1/\gamma_0 - 1/\gamma)\, e^{-\gamma/\bar\gamma}\, d\gamma/\bar\gamma = 1$, that is $e^{-\gamma_0/\bar\gamma}/\gamma_0 - E_1(\gamma_0/\bar\gamma)/\bar\gamma = 1$. Bisection gives $\gamma_0 = 0.591$ and $C = \log_2(e)\, E_1(\gamma_0/\bar\gamma) = 1.845$ bits, against 1.716 without transmitter knowledge and 2.057 for AWGN.

26. In Clarke's model the envelope $r = |h|$ and its derivative $\dot r$ are independent at the same instant, and $\dot r$ is Gaussian with mean 0 and variance $\pi^2 f_D^2\Omega$, half the power $2\pi^2 f_D^2\Omega$ of $h'$. So $N_R = p(R)\,\mathbb{E}[\dot r^+] = p(R)\,\sigma_{\dot r}/\sqrt{2\pi}$ with $p(R) = (2R/\Omega)e^{-R^2/\Omega}$. Put $\rho = R/\sqrt\Omega$.
