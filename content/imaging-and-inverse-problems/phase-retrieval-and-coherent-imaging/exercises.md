In these exercises a signal $x = [x[0], \ldots, x[n-1]]$ has $x[0] \ne 0$ and $x[n-1] \ne 0$, its transform is $X(e^{i\omega}) = \sum_t x[t] e^{-i\omega t}$, and its autocorrelation is $r[k] = \sum_t x[t+k]\, \overline{x[t]}$, as in the [phase retrieval](/phase-retrieval/) entry. Two signals are trivially equivalent if one is obtained from the other by a shift, a conjugate reversal or multiplication by a constant of modulus 1.

1. ◦ Compute the autocorrelation $r[k]$, $k = -2, \ldots, 2$, of $x = [2, 1, 3]$, and from it $|X(e^{i\omega})|$ at $\omega = 0$ and at $\omega = \pi$. Check both values directly from $X$.

2. ◦ A real signal of length 64 is to be recovered from samples of its Fourier magnitude at $M$ equally spaced frequencies. (a) What is the smallest $M$ for which the samples determine the autocorrelation? (b) Keep the signal in positions $0, \ldots, 63$. How many real signals do the trivial ambiguities give, counting $x$ itself, and when are there fewer? (c) Up to how many classes of solutions can there be in all?

3. ◦ The entry flips the zero $-2$ of $X(z) = 1 + 5z^{-1} + 6z^{-2} = (1 + 2z^{-1})(1 + 3z^{-1})$ and gets $[2, 7, 3]$. Flip the zero $-3$ instead, and then flip both zeros. Which of the two signals you get is trivially equivalent to $x$, and which to $[2, 7, 3]$?

4. ◦ Let $x = [1, 2i]$. Show that $|X(e^{i\omega})|^2 = 5 + 4 \sin\omega$. Compute the same for the plain reversal $[2i, 1]$ and the conjugate reversal $[-2i, 1]$, and say which of them is a trivial ambiguity.

5. • The signal $x = [1, 6, 11, 6]$ has $X(z) = (1 + z^{-1})(1 + 2z^{-1})(1 + 3z^{-1})$. List all real signals of length 4 with the same Fourier magnitude, and group them into classes of trivially equivalent signals. Why are there fewer than $2^{n-2} = 4$ classes?

6. • A real signal of length 2 has autocorrelation $r[0] = 5$, $r[1] = r[-1] = 2$. Find every such signal by spectral factorization: write the polynomial $z \sum_k r[k] z^{-k}$, factor it, and choose one root of each pair $\{a, 1/a\}$.

7. • Take $n = 3$ and only $M = 3$ magnitude samples, at $\omega = 0, 2\pi/3, 4\pi/3$. Show that $[1, 5, 6]$ and $[1, 6, 5]$ give the same three samples, and that they are not trivially equivalent. Then show that $M = 5$ samples tell them apart. Explain the result with the aliasing of $r$.

8. • A filter designer wants the minimum-phase signal, with all zeros inside the unit circle, whose Fourier magnitude equals that of $[1, 5, 6]$. Find it, and check its autocorrelation against the one in the entry.

9. • In generalized phase retrieval the data are $b_i = |\langle a_i, x\rangle|^2$ with $\langle a, x\rangle = a^* x$. (a) Show that $b_i = a_i^* X a_i = \operatorname{tr}(a_i a_i^* X)$ with $X = x x^*$, so each measurement is linear in $X$. (b) Check this for $a = (1, 1)$ and $x = (1, 2i)$ by computing $X$. (c) What constraint on $X$ must be dropped to get the semidefinite relaxation of PhaseLift?

10. ★ Fienup's error reduction starts from a signal $g_k$ that satisfies the object constraint (for example a known support), computes $G_k = \mathcal{F} g_k$ with the unitary DFT $\mathcal{F}$, replaces its magnitude by the measured one to get $G'_k$, sets $g'_k = \mathcal{F}^{-1} G'_k$, and lets $g_{k+1}$ be the point nearest to $g'_k$ that satisfies the object constraint. Let $E_k = \lVert G_k - G'_k \rVert$. Prove that $E_{k+1} \le E_k$. Does your proof show that the iteration converges to a solution?

11. ★ Let $x$ be a real signal of length $n$ whose $n - 1$ zeros are real, distinct, off the unit circle, and such that no zero is the reciprocal of another. Prove that exactly $2^n$ real signals of length $n$ have the Fourier magnitude of $x$. Check the count for $[1, 5, 6]$ and for $[1, 10, 31, 30]$, whose zeros are $-2$, $-3$ and $-5$.
