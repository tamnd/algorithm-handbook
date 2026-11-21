3. The integral of $x$ from 0 to $b$ is $0$, $(b - 2)/2$ or $3/2 + (b - 5)$ on the three pieces. The payments are 0, $3 \cdot \frac12 - \frac12 = 1$ and $6 - \frac52 = \frac72$. In step form, $\frac72 = 2 \cdot \frac12 + 5 \cdot \frac12$: each jump of $x$ is paid at the bid where it happens.

7. Send "convict" always when guilty and with probability $q$ when innocent, and make the judge exactly indifferent: $\frac{2/5}{2/5 + (3/5) q} = \frac23$ gives $q = \frac13$. The conviction rate is $\frac25 + \frac35 \cdot \frac13 = \frac35$, the prior divided by the threshold.

8. Every job goes to machine 1, and each payment is the second smallest time, 2, so machine 1 is paid 6, works 3 and has utility 3. The makespan is 3. Two jobs on machine 1 and one on machine 2 give makespan 2, which is optimal, so the ratio here is $3/2$.

9. Trade happens with probability $\frac14$, and given trade $\mathbb{E}[v] = \frac34$ and $\mathbb{E}[c] = \frac14$, so the gains are $\frac14 \cdot \frac12 = \frac18$. This is $\frac34$ of the first-best $\frac16$, while $\frac{9}{64}$ is $\frac{27}{32}$ of it.

11. $h(s)$ is the other agent's expected value from the project when you report $s$. The project is built only at $(1, 1)$, so $h(1) = \frac12$ and $h(-3) = 0$. With $p_i = h(b_j) - h(b_i)$, type 1 expects $\frac34$ from the truth and $-\frac14$ from lying; type $-3$ expects $-\frac14$ from the truth and $-\frac54$ from lying. Only type $-3$ fails interim IR.

13. The lengths are $c(t^1, t^2) = 2$, $c(t^1, t^3) = 4$, $c(t^2, t^1) = 4$, $c(t^2, t^3) = 1$, $c(t^3, t^1) = 6$ and $c(t^3, t^2) = 4$. The 2-cycles have lengths 6, 10 and 5 and the 3-cycles 9 and 12, all nonnegative. The distances from $t^1$ are 0, 2 and 3, and the truthful utilities are 6, 3 and 1.

14. For $S = \{H\}$ the condition reads $3 \cdot \frac12 q(H) \le 1 - \frac18$, so $q(H) \le \frac{7}{12}$. For $S = \{H, L\}$ it reads $\frac32 (q(H) + q(L)) \le 1$, so $q(L) \le \frac{1}{12}$. Give the item to a uniformly random H bidder if there is one, and else to a uniformly random bidder.

15. Each type's conditional belief puts $\frac45$ on the other bidder having the same type. The Vickrey rents are 0 for value 1 and $\frac15$ for value 2. Solving $\frac45 z(1) + \frac15 z(2) = 0$ and $\frac15 z(1) + \frac45 z(2) = \frac15$ gives $z(1) = -\frac{1}{15}$ and $z(2) = \frac{4}{15}$. The Vickrey revenue is $\frac75$, the bets bring $\frac15$, and the total $\frac85$ is the expected highest value. Each lie gives $-\frac{1}{10}$.

21. Here $L = 0$ and $H = 1$, so the bound is $-\int_0^1 t (1 - t/2)\, dt = -\frac13$. The VCG deficit is $\mathbb{E}[(v - c)^+] = \int_0^1 \frac{(2 - c)^2}{4}\, dc = \frac{7}{12}$. The lowest buyer type gets nothing, so $K_b = 0$; the highest seller type gets $\mathbb{E}[(v - 1)^+] = \frac14$, so $K_s = \frac14$. The remaining deficit is $\frac{7}{12} - \frac14 = \frac13$, which meets the bound.

22. $h_b(v) = \mathbb{E}_c[-c \cdot 1\{c \le v\}] = -v^2/2$ and $h_s(c) = \mathbb{E}_v[v \cdot 1\{v \ge c\}] = (1 - c^2)/2$, with means $-\frac16$ and $\frac13$. Then $U_b(v) = v^2 - v^2/2 - \frac13 = v^2/2 - \frac13$ and $U_s(c) = (1 - c)^2/2 + \frac16$. The worst types are $v = 0$ with $-\frac13$ and $c = 1$ with $\frac16$. Any constant shift between the agents keeps BIC and balance but leaves the sum $-\frac16$, so both cannot be made IR, as the theorem says.

23. The receiver takes action 0 below belief $\frac13$, action 1 on $[\frac13, \frac23)$ and action 2 from $\frac23$ on. The upper hull of the points $(0, 0)$, $(\frac13, 1)$, $(\frac23, 3)$, $(1, 3)$ runs from $(0, 0)$ to $(\frac23, 3)$, so the value at $\frac14$ is $\frac98$. Recommend action 2 always in the good state and with probability $\frac16$ in the bad state.

24. Fix $b_{-i}$ and let $m = \max_{j \ne i} b_j$. Bidder $i$'s allocation is a step from 0 to 1 at $m$, so the lemma gives $p_i = h_i'(b_{-i}) + m$ when $i$ wins and $h_i'(b_{-i})$ when it loses. Set $h_i = h_i' + m$ and compare with $h_i(b_{-i}) - \sum_{j \ne i} b_j(x)$.

25. Type 1 gains nothing by lying for any $p$. Type $-3$ pays the same expected charge $\mathbb{E}[h(t_j)]$ either way. Reporting 1 adds $-3p$ in value and $h(1) = \frac12$ in transfer, so the gain from lying is $\frac12 - 3p$, and truth telling is an equilibrium if and only if $p \ge \frac16$. The payments were tuned to one prior, and BIC can fail for another.
