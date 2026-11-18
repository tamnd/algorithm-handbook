1. ◦ A sample has four species with counts $(6, 3, 2, 1)$. Compute the [Shannon index](/shannon-diversity-index/) $H$ in nats, the effective number $e^H$ and Pielou's evenness $H/\ln 4$. Then compute the [Simpson index](/simpson-diversity-index/) $\lambda = \sum p_i^2$, its inverse $1/\lambda$, and the unbiased form $\sum n_i(n_i - 1)/(n(n - 1))$.

2. ◦ A biologist marks and releases $M = 50$ fish. A second catch of $C = 40$ fish holds $R = 8$ marked ones. Give the [Lincoln-Petersen](/lincoln-petersen-estimator/) estimate of the population and Chapman's form $(M + 1)(C + 1)/(R + 1) - 1$.

3. ◦ A sample shows 12 species, of which 4 were seen once and 2 were seen twice. Give the classic [Chao1](/chao1-estimator/) estimate $S_{obs} + f_1^2/(2 f_2)$ and the bias-corrected form $S_{obs} + f_1(f_1 - 1)/(2(f_2 + 1))$.

4. ◦ An infection has $R_0 = 5$. Give the [herd immunity threshold](/herd-immunity-threshold/) and the vaccine coverage needed with a vaccine that protects 90% of those who receive it. Repeat for $R_0 = 12$ and say what the result means.

5. ◦ In the [Levins model](/levins-metapopulation-model/) $\dot p = c p (1 - p) - e p$ with $c = 0.4$ and $e = 0.1$, find the equilibrium fraction of occupied patches. If 30% of the patches are destroyed, the model becomes $\dot p = c p (1 - D - p) - e p$ with $D = 0.3$. Find the new equilibrium and the value of $D$ at which the species is lost.

6. ◦ An [SEIR model](/seir-epidemic-model/) has $\beta = 0.5$, $\sigma = 0.2$, $\gamma = 0.25$ and births and deaths at rate $\mu = 0.05$, all per day. Compute $R_0 = \beta\sigma/((\sigma + \mu)(\gamma + \mu))$, and compare it with the value for $\mu = 0$.

7. ◦ For the [logistic map](/logistic-map/) $x_{t+1} = r x_t (1 - x_t)$, find the positive fixed point and the slope of the map there for $r = 2.5$ and for $r = 3.2$. Which fixed point is stable?

8. ◦ The [Ricker model](/ricker-model/) $u_{t+1} = u_t e^{r(1 - u_t)}$ has the fixed point $u = 1$. Show that the slope there is $1 - r$. Is the fixed point stable for $r = 1.5$? For $r = 2.5$? For which $r$ does the population approach it without overshooting?

9. ◦ A predator has a [Holling type II](/holling-functional-response/) response $f(N) = aN/(1 + ahN)$ with attack rate $a = 0.5$ and handling time $h = 0.2$. Give the largest possible rate of predation, the prey density at which the rate is half of it, and $f(40)$.

10. • A [Galton-Watson process](/galton-watson-process/) has offspring probabilities $p_0 = 1/6$, $p_1 = 1/3$ and $p_2 = 1/2$. Find the mean, the extinction probability for one ancestor, and the extinction probability for two ancestors.

11. • Solve the [final size relation](/final-size-relation/) $1 - z = e^{-R_0 z}$ by [fixed-point iteration](/fixed-point-iteration/) for $R_0 = 2$ and $R_0 = 3$. Then suppose that 25% of the population is immune before an epidemic with $R_0 = 2$ arrives. What share of the whole population is infected?

12. • A [Leslie matrix](/leslie-matrix/) has fecundities $(0, 1, 2)$ and survival probabilities $P_1 = P_2 = 1/2$. Write its characteristic equation, show that $\lambda = 1$ is the dominant eigenvalue, give the stable age distribution, and give the modulus of the other two eigenvalues.

13. • In the [Lotka-Volterra competition model](/lotka-volterra-competition/) take $K_1 = 100$, $K_2 = 80$, $\alpha_{12} = 0.5$ and $\alpha_{21} = 0.6$. Find the coexistence equilibrium and say whether it is stable. What happens if $\alpha_{21}$ is raised to 1.5?

14. • An epidemic grows at $r = 0.1$ per day. Find $R$ from $R = 1/M(-r)$ when the [generation interval](/generation-interval/) is fixed at 5 days, exponential with mean 5 days, and gamma with shape 4 and mean 5 days.

15. • In the discrete [renewal equation](/epidemic-renewal-equation/) $I_t = R \sum_u w_u I_{t-u}$, take $w_1 = w_2 = 1/2$. Find the long-run daily growth factor for $R = 2$. Then find $R$ when the cases grow by a factor 1.2 per day.

16. • A species invades along a line with growth rate $r = 0.5$ per year and diffusion coefficient $D = 0.1$ km² per year. Give the speed of the [Fisher-KPP](/fisher-kpp-equation/) front, and the speed if $D$ is multiplied by 4.

17. • In the [Ross-Macdonald model](/ross-macdonald-model/) take $m = 5$ mosquitoes per human, biting rate $a = 0.25$ per day, $b = 0.4$, $c = 0.6$, human recovery $r = 0.02$ per day, mosquito death rate $g = 0.12$ per day and incubation $n = 12$ days. Compute Macdonald's product $Q = m a^2 b c e^{-gn}/(rg)$ and $R_0 = \sqrt{Q}$, and find the critical density $m_c$. Compare two controls: bed nets that halve $a$, and an insecticide that doubles $g$.

18. • [Cori estimation](/cori-rt-estimation/) uses a gamma prior with shape $a = 1$ and scale $b = 5$. In one window the cases sum to 60 and the total infectiousness $\Lambda$ sums to 40. Give the posterior shape, rate, mean and standard deviation of $R$. How many cases in a window are needed for a coefficient of variation of at most 0.1?

19. • In the [Reed-Frost model](/reed-frost-model/), one case enters a group of three susceptibles, and each contact infects with probability $p = 1/2$. Find the exact law of the final number of new cases and its mean.

20. • A fish stock follows the [logistic model](/logistic-growth-model/) with $r = 0.4$ per year and $K = 1000$. With harvest effort $E$ the catch is $EN$. Find the effort that gives the largest sustained catch, and that catch. With a fixed catch of $H = 30$ per year instead, find the two equilibria and say which is stable.

21. ★ Show that for any abundances $p_1, \ldots, p_S > 0$, the effective numbers satisfy $1/\lambda \le e^H \le S$, and that both are equalities exactly when all $p_i$ are equal. Check the result on exercise 1.

22. ★ In a [branching process](/branching-process-extinction-theorem/) with negative binomial offspring of mean $R_0$ and dispersion $k$, $f(s) = (1 + (R_0/k)(1 - s))^{-k}$. For $R_0 = 2$ and $k = 1/2$, find the extinction probability in closed form, and compare it with the values for $k = 1$ and for Poisson offspring.

23. ★ On a network with degree distribution $P(k) \propto k^{-3}$ for $1 \le k \le K$, the [heterogeneous mean-field](/heterogeneous-mean-field-epidemic/) SIS threshold is $\langle k \rangle / \langle k^2 \rangle$. Show that the threshold is at most $1/\langle k \rangle$, with equality only for a regular network. Compute it for $K = 100$, $1000$ and $10^6$, and show that it tends to 0 like $1/\ln K$.

24. ★ In the SEIR model without births, a case is latent for an exponential time with rate $\sigma$ and then infectious for an exponential time with rate $\gamma$, infecting at rate $\beta$. Show that the generation interval is the sum of two independent exponential times with rates $\sigma$ and $\gamma$, and deduce $R_0 = (1 + r/\sigma)(1 + r/\gamma)$. Check it for $\beta = 0.6$, $\sigma = 0.25$ and $\gamma = 0.2$.

25. ★ A reaction-diffusion system has the Jacobian $J = \begin{pmatrix} 1 & -2 \\ 3 & -4 \end{pmatrix}$ at its equilibrium, with diffusion coefficients $d_u = 1$ and $d_v = d$. Show that the equilibrium is stable without diffusion, and find the smallest $d$ that gives a [Turing instability](/turing-instability/). Give the critical wavenumber squared at that $d$.
