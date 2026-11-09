1. ◦ Show that the rows $(3, 7)$ and $(2, 5)$ form a [basis](/lattice-basis/) of $\mathbb{Z}^2$, and write $(1, 0)$ as an integer combination of them. Which integer matrix carries the standard basis to this one?

2. ◦ Apply [Gram-Schmidt orthogonalization](/gram-schmidt-orthogonalization/) to $b_1 = (3, 1)$, $b_2 = (2, 4)$. Give $\mu_{21}$ and $b_2^*$, and check that $\|b_1^*\| \, \|b_2^*\|$ equals the [determinant](/lattice-determinant/) of the lattice.

3. ◦ Run [Lagrange-Gauss reduction](/lagrange-gauss-reduction/) on $b_1 = (43, 19)$, $b_2 = (66, 29)$. List the quotient used at each step and the reduced basis. What are $\lambda_1$, $\lambda_2$ and $\det(L)$?

4. ◦ For $b_1 = (5, 0)$, $b_2 = (2, 3)$ and $\delta = 3/4$, check the [Lovász condition](/lovasz-condition/). It fails; swap the vectors, size-reduce, and check the condition again. What [LLL-reduced basis](/lll-reduction/) do you get?

5. ◦ Find a basis of the [dual lattice](/dual-lattice/) of the lattice with basis $(2, 1)$, $(0, 3)$, check the inner products with the original basis, and give the determinant of the dual.

6. ◦ A lattice of rank $4$ has determinant $81$. What upper bound on $\lambda_1$ does [Minkowski's theorem](/minkowski-theorem/) give? What bound follows from the [Hermite constant](/hermite-constant/) $\gamma_4 = \sqrt 2$?

7. ◦ A random lattice of rank $100$ has determinant $1$. What does the [Gaussian heuristic](/gaussian-heuristic/) predict for $\lambda_1$, using $\sqrt{n / (2\pi e)}$? Compare with the bound from Minkowski's theorem.

8. ◦ In rank $n = 300$ with $\det(L) = 1$, estimate $\|b_1\|$ after LLL and after BKZ with block size 20, using the [root Hermite factors](/root-hermite-factor/) $1.0219$ and $1.0128$. Compare with the proved bound $2^{(n-1)/4}$ of the [LLL approximation guarantee](/lll-approximation-guarantee/).

9. • Let $L$ have basis $(2, 0)$, $(1, 3)$. Check that the basis is Lagrange-Gauss reduced and give the [successive minima](/successive-minima/) $\lambda_1, \lambda_2$. Find the [covering radius](/covering-radius/) of $L$ and a deep hole. Check that $\lambda_1 \lambda_2$ lies between $\det(L)$ and $\gamma_2 \det(L)$, as [Minkowski's second theorem](/minkowski-second-theorem/) says.

10. • For the lattice $L$ of Exercise 9, find a basis of the dual lattice $L^\times$ and $\lambda_1(L^\times)$. Then prove that $\lambda_1(L) \, \lambda_1(L^\times) \le \gamma_n$ for every lattice of rank $n$, and compare with the value for $L$.

11. • List all vectors $v \ne 0$ of the lattice of Exercise 9 with $\|v\|^2 \le 10$ by the method of [Fincke and Pohst](/fincke-pohst-enumeration/): first the range of the coefficient of $b_2$, then, for each value, the range of the coefficient of $b_1$. How many vectors are there?

12. • Run the [LLL algorithm](/lll-algorithm/) with $\delta = 3/4$ on the rows $(2, 1, 0)$, $(5, 3, 1)$, $(7, 4, 6)$, size-reducing only when $|\mu_{kj}| > 1/2$. Record each size reduction and each swap. What is the output, and what is $\det(L)$?

13. • The lattice $L$ with basis $(2, 3)$, $(3, -3)$ also has the basis $(2, 3)$, $(11, 9)$. For the target $t = (4.4, 1.3)$, apply [Babai rounding](/babai-rounding/) with each basis. Which answer is the [closest vector](/closest-vector-problem/), and how far from $t$ is each? What does [Babai's nearest plane method](/babai-nearest-plane/) give with the second basis?

14. • Since $11^2 \equiv -1 \pmod{61}$, the vectors $(a, b) \in \mathbb{Z}^2$ with $b \equiv 11 a \pmod{61}$ form a lattice. Give its determinant, use Minkowski's theorem to show that it contains a nonzero vector with $a^2 + b^2 < 122$, and find one by Lagrange-Gauss reduction of $(1, 11)$, $(0, 61)$. Write $61$ as a sum of two squares.

15. • Let $\alpha = \sqrt 3 + \sqrt 5$. Find the [integer relation](/integer-relation-problem/) $m = (m_0, \ldots, m_4)$ with $\sum_i m_i \alpha^i = 0$ that a lattice method would return for $(1, \alpha, \alpha^2, \alpha^3, \alpha^4)$, and check it numerically to six digits.

16. • Find the integer $1 \le q \le 100$ for which $\max(\|q \sqrt 2\|, \|q \sqrt 3\|)$ is smallest, where $\|x\|$ is the distance to the nearest integer. Give the fractions it produces and the error, and compare with the guarantee of [simultaneous Diophantine approximation](/simultaneous-diophantine-approximation/) for $Q = 10$.

17. • Let $A$ be an $m \times n$ matrix over $\mathbb{Z}_q$ with $n = 4$, $q = 17$. For which $m$ does the pigeonhole principle guarantee a nonzero $z \in \{-1, 0, 1\}^m$ with $z A \equiv 0 \pmod q$, whatever $A$ is? Give the bound on $\|z\|$. This is the existence of solutions behind [Ajtai's reduction](/ajtai-worst-case-to-average-case-reduction/).

18. • For the lattice $L$ of Exercise 13 and the target $t = (5, 1)$, form the embedded lattice with rows $(2, 3, 0)$, $(3, -3, 0)$, $(5, 1, 1)$. Find its shortest vectors and its second minimum, and read off the closest vector of $L$ to $t$. Which [unique SVP](/unique-svp/) gap does this instance have?

19. • The lattice $D_4$ is the set of $x \in \mathbb{Z}^4$ with $x_1 + x_2 + x_3 + x_4$ even. Find $\det(D_4)$, $\lambda_1(D_4)$ and the number of shortest vectors, and deduce that $D_4$ reaches the Hermite constant $\gamma_4 = \sqrt 2$.

20. ★ A lattice of rank $n$ has $\lambda_2 > 2^{(n-1)/2} \lambda_1$. Prove that the first vector of any LLL-reduced basis with $\delta = 3/4$ is $\pm s$, where $s$ is a shortest vector. So LLL solves unique SVP with this gap.

21. ★ Show that the output of Exercise 12 is [HKZ-reduced](/hkz-reduction/), and find the three successive minima of that lattice. Check [Minkowski's second theorem](/minkowski-second-theorem/) with $\gamma_3 = 2^{1/3}$.

22. ★ Prove that $\lambda_1(L)^2 \le \frac{2}{\sqrt 3} \det(L)$ for every lattice of rank 2, with equality only when $L$ is a scaled and rotated copy of the hexagonal lattice spanned by $(1, 0)$ and $(\tfrac12, \tfrac{\sqrt 3}{2})$.

23. ★ Let $N = 1000003$ and $f(x) = x^2 + 654321 x + 419719$. The congruence $f(x) \equiv 0 \pmod N$ has a root $x_0$ with $|x_0| < 8$. Following [Coppersmith's method](/coppersmith-method/), reduce the lattice spanned by the coefficient vectors of $N$, $N x X$ and $f(x X)$ for $X = 8$, read off a polynomial $h$ with $h(x_0) = 0$ over the integers, and find $x_0$.

24. ★ The weights $8513, 3290, 9112, 6401, 2577, 7748, 4459, 1823$ have a subset with sum $28485$. Build a lattice in which the subset is a short vector, find it with LLL, and give the subset. What is the density $n / \log_2 \max a_i$ of this instance?
