In these exercises $A$ is an $m \times n$ matrix with columns $a_1, \ldots, a_n$, a vector is $s$-sparse if it has at most $s$ nonzero entries, $\delta_s$ is the restricted isometry constant of order $s$, and $\mu$ is the [mutual coherence](/mutual-coherence/), the largest $|\langle a_i, a_j\rangle|$ over distinct unit-norm columns. Basis pursuit is $\min\|x\|_1$ subject to $Ax = y$. Soft thresholding is $\mathrm{shrink}(v, t) = \mathrm{sign}(v)\max(|v| - t, 0)$.

1. ◦ Three measurements of one constant $x$ give $y = (1, 2, 10)$, so $A = (1, 1, 1)^{\mathsf T}$. Find the minimizer of the least squares, the Kullback-Leibler and the $\ell_1$ [data fidelity term](/data-fidelity-term/), with no regularizer. Which one ignores the value 10, and for which noise law is it the right choice?

2. ◦ Compute the coherence of the three columns $(1, 0)$, $(0, 1)$ and $(1, 1)/\sqrt2$, and compare it with the Welch bound $\sqrt{(n - m)/(m(n - 1))}$ for $m = 2$, $n = 3$. Give three unit vectors in the plane that meet the bound.

3. ◦ Let $A = [I_4, H_4/2]$, where $H_4$ is the $4 \times 4$ Hadamard matrix with entries $\pm1$. Compute $\mu$ and the Welch bound for $m = 4$, $n = 8$. Up to which $s$ does the coherence condition $s < \tfrac12(1 + 1/\mu)$ guarantee recovery by basis pursuit?

4. ◦ Let $A = (1\ 1\ 1)$, a single row. Show that the [null space property](/null-space-property/) of order 1 fails, and find all solutions of basis pursuit for $y = 1$, the data of $x = (1, 0, 0)$.

5. ◦ [Iterative hard thresholding](/iterative-hard-thresholding/) contracts the error by the factor $2\delta_{3s}$ per step when $\delta_{3s} < 1/2$. With noise-free data and $\delta_{3s} = 0.2$, how many steps reduce the error by a factor of $10^6$? For [CoSaMP](/cosamp/), evaluate the factor $\rho = 4\delta\sqrt{1 + c^2}/(1 - \delta)$ with $c = \delta/(1 - \delta)$ at $\delta = 0.05$.

6. ◦ For total variation in two dimensions with forward differences, $\|K\|^2 \le 8$. Which of the step pairs $(\tau, \sigma) = (0.35, 0.35)$, $(1/\sqrt8, 1/\sqrt8)$, $(0.5, 0.25)$ and $(1, 0.1)$ satisfy the condition $\tau\sigma\|K\|^2 < 1$ of the [Chambolle-Pock algorithm](/chambolle-pock-algorithm/)?

7. ◦ A dictionary of $K$ atoms for signals of length $n$ is to be learned with $s$ nonzero coefficients per signal. (a) How many dictionaries give the same fit by the signed permutation ambiguity of [dictionary learning](/dictionary-learning/), for $K = 4$? Give $\log_{10}$ of the count for $K = 256$. (b) For $8 \times 8$ patches, $K = 256$ and $s = 4$, how many training signals does the count $N \ge nK/(n - s)$ ask for?

8. ◦ Let $\Omega$ be the $3 \times 3$ matrix with rows $(1, 0, 0)$, $(-1, 1, 0)$ and $(0, -1, 1)$. Find the synthesis dictionary $D$ for which the analysis model $\|\Omega x\|_1$ and the synthesis model $x = Dz$ with $\|z\|_1$ are the same, as in [analysis and synthesis sparsity](/analysis-and-synthesis-sparsity/). Check it on $x = (2, 2, 5)$.

9. • Run [Bregman iteration](/bregman-iteration/) on the scalar problem $A = \sigma = 0.1$ with $R(x) = \tfrac12x^2$ and $\lambda = 0.01$. Show that the residual is multiplied by $\lambda/(\sigma^2 + \lambda)$ at each step, so that after $k$ steps the filter factor is $1 - (\lambda/(\sigma^2 + \lambda))^k$. How many steps give a filter factor of at least 0.9?

10. • Let $R(x) = \|x\|_1$ on $\mathbb{R}^3$, $x^\dagger = (1, 0, -2)$ and $p = (1, 0.5, -1)$. Check that $p \in \partial R(x^\dagger)$ and compute the Bregman distance $D^p(x, x^\dagger) = R(x) - R(x^\dagger) - \langle p, x - x^\dagger\rangle$ for $x = (0.5, 1, -1)$, $(2, 0, -4)$, $(1, 0.4, -2)$ and $0$. What do the zero values say about [convergence rates in the Bregman distance](/bregman-distance-convergence-rates/)?

11. • The rate bound $D^{\mathrm{sym}} \le (\delta + \lambda\|w\|)^2/(4\lambda)$ holds under the source condition $A^*w \in \partial R(x^\dagger)$. Show that $\lambda = \delta/\|w\|$ minimizes it, with the value $\|w\|\delta$. Evaluate the bound for $\|w\| = 2$, $\delta = 0.01$ at $\lambda = \delta$ and at the optimal $\lambda$.

12. • In one dimension, with forward differences $Du$ and $Dw$, the second order [total generalized variation](/total-generalized-variation/) is $\min_w \alpha_1\|Du - w\|_1 + \alpha_0\|Dw\|_1$. Compute it for the hat $u = (0, 1, 2, 1, 0)$, and compare with $\alpha_1\mathrm{TV}(u)$. Evaluate for $(\alpha_1, \alpha_0) = (1, 1)$, $(1, 3)$ and $(1, 0.25)$.

13. • Let $N = 16$ and let $x$ have the value 1 at $t = 0, 4, 8, 12$ and 0 elsewhere. Compute its DFT, and find a set $\Omega$ of 12 frequencies on which $x$ and the zero signal agree. Why does this not contradict Theorem 1.1 of the [Candès-Romberg-Tao theorem](/candes-romberg-tao-theorem/) entry?

14. • Let $A$ be a $1 \times 3$ matrix with i.i.d. standard Gaussian entries, and let $x = c\,e_1$ with $c \ne 0$. Show that basis pursuit recovers $x$ exactly when $|a_1| > \max(|a_2|, |a_3|)$, and find the probability. Compare with the small cases of the [Donoho-Tanner phase transition](/donoho-tanner-phase-transition/).

15. • The [split Bregman method](/split-bregman-method/) for $\min_x \tfrac12(x - f)^2 + \lambda|x|$ with the split $d = x$ iterates $x \leftarrow (f + \mu(d - b))/(1 + \mu)$, $d \leftarrow \mathrm{shrink}(x + b, \lambda/\mu)$, $b \leftarrow b + x - d$. Run it from $d = b = 0$ with $f = 3$, $\lambda = 1$ and $\mu = 1$ for four steps, and show that the error of $x$ halves at each step from the second on. What is the limit?

16. • In [K-SVD](/k-svd/), the residual of the signals that use atom $k$, without the contribution of that atom, is $E = \begin{pmatrix} 3 & 1 \\ 1 & 3\end{pmatrix}$, one column per signal. Compute the new atom and its coefficients from the best rank one approximation of $E$, and the squared error before and after the update.

17. • In Fourier-domain [convolutional sparse coding](/convolutional-sparse-coding/) each frequency needs the solution of $(\rho I + aa^{\mathsf H})x = r$. Derive the Sherman-Morrison solution $x = \rho^{-1}(r - a\,a^{\mathsf H}r/(\rho + a^{\mathsf H}a))$ and evaluate it for $a = (1, 2, 2)$, $\rho = 1$ and $r = (1, 0, 0)$.

18. • The bound $\delta_s \le (s - 1)\mu$ turns coherence into a restricted isometry constant. For $\mu = 1/16$, bound $\delta_5$. For which $s$ does it certify the condition $\delta_{3s} < 1/2$ of iterative hard thresholding, and for which the condition $\delta_{4s} \le 0.1$ of CoSaMP?

19. • Draw five $64 \times 256$ matrices with i.i.d. Gaussian entries, normalize the columns, and compute $\mu$ for each. Use `random.Random(1)`. Compare with the Welch bound and with $\sqrt{\log n/m}$, and say up to which $s$ the coherence condition guarantees recovery.

20. ★ Let $A$ have unit-norm columns and coherence $\mu$. Show that every $v$ in the null space of $A$ satisfies $(1 + \mu)|v_i| \le \mu\|v\|_1$ for each $i$, and deduce that the null space property of order $s$ holds when $s < \tfrac12(1 + 1/\mu)$.

21. ★ Let $N = 5$ and $\Omega = \{0, 1\}$. Construct two different signals, with at most 2 nonzero entries each, whose DFTs agree on $\Omega$. Use a polynomial with roots at $e^{-2\pi ik/5}$ for $k \in \Omega$. Check that the difference meets Tao's bound $|\mathrm{supp}\,h| + |\mathrm{supp}\,\hat h| \ge N + 1$ with equality.

22. ★ In [diffusion posterior sampling](/diffusion-posterior-sampling/) take the prior $N(0, 1)$, $A = 1$, noise variance $\sigma^2 = 0.25$, and a state $x_t = \sqrt{\bar\alpha}\,x_0 + \sqrt{1 - \bar\alpha}\,\varepsilon$ with $\bar\alpha = 0.5$. Compute the exact likelihood $p(y \mid x_t)$ and the one that DPS uses with the exact Tweedie estimate. Find the ratio of their gradients in $x_t$, and evaluate both gradients at $x_t = 1$, $y = 1$.

23. ★ Prove that the matrix $M = \begin{pmatrix} I/\tau & -K^{\mathsf T} \\ -K & I/\sigma\end{pmatrix}$ is positive definite exactly when $\tau\sigma\|K\|^2 < 1$. This is the step condition of the Chambolle-Pock algorithm read as a [proximal point method](/proximal-point-method/) in the metric $M$.

24. ★ Let $\Omega$ have the rows $(1, 0)$, $(0, 1)$ and $(1, 1)$, and let $D = \Omega^+$ be its pseudoinverse. Solve the analysis problem $\min_x \tfrac12\|x - y\|^2 + \lambda\|\Omega x\|_1$ and the synthesis problem $\min_z \tfrac12\|Dz - y\|^2 + \lambda\|z\|_1$ for $y = (1, 1)$ and $\lambda = 0.2$, and show that the two reconstructions differ.
