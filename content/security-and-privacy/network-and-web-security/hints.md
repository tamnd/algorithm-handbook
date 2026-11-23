1. (a) and (d) are the same origin: the host is compared in lower case, and the path, the query and the fragment play no part. (b) has port 80, (c) has another scheme and (e) another host. The script runs with the origin (`http`, `intranet.example.org`, 8080) of the page that embeds it.

3. Fixed port: $P_s = 250/131072 \approx 0.00191$, and $\ln 2 / (-\ln(1 - P_s)) \approx 363$ windows. Random ports: $P_s \approx 1.16 \times 10^{-7}$, about 5.95 million windows, which at one hour each is about 680 years.

4. The edges arrive with probability $1/2$, $1/4$ and $1/8$, and a mark of the attacker survives with probability $(1/2)^3 = 1/8$. The sum has 7 terms: $14 - 28/5 + 8/7 = 334/35 \approx 9.54$ packets. The bound is $(11/6)/(1/8) = 44/3 \approx 14.67$.

7. (a) Invalid, since 26 > 25. (b) NotFound: a /23 is shorter than the /24 of the VRP, so it is not covered. (c) Valid: 1fff starts with the nibble 1, so the /36 covers it, and 48 ≤ 48. (d) NotFound, since 2000 starts with 2. (e) Invalid: the origin is the rightmost AS, 64511. With the new VRP only (e) changes, to Valid.

9. (a) No cookie, and both the `Origin` check and the token reject it. (b) The cookie goes with a top-level GET, no check runs, and the record is deleted: the defenses assume that GET changes no state. (c) The cookie goes, since the request is same-site, but the `Origin` is `https://forum.example.com` and there is no token, so it is rejected. (d) `Sec-Fetch-Site` is `same-site`, so the transfer goes through; a server that wants to stop it must accept only `same-origin`.

10. $u$ is at the start of a URL: url-filter gives `about:invalid`. Line L7 moves to the rest of the URL, so $v$ gets url-encode: `a%20b%26c`. $t$ is in HTML text: `&lt;b&gt;`. $w$ is in a script string, and js-string gives `\u0027\u003balert\u00281\u0029\u002f\u002f`. In the IF, one branch ends at the start of a URL and the other in HTML text, so line L10 fails and the template is rejected: no one escaper fits the hole after it.

12. Strict mode passes the packet, because the longest match for 192.0.2.1 is the default route, which leaves on $i_0$. Loose mode drops it, because default routes do not count there. So a packet can pass strict and fail loose, against the order of the checks the entry states. Ignoring default routes in lines L4 and L5 too restores the order.

15. $np/(1-p) \le 1$ gives $p \le 1/21$, so each table may have a false-positive rate of at most $1/126 \approx 0.0079$. With $b = 10$ the best $k$ is 7, which gives 0.0082, just too much; $b = 11$ with $k = 8$ gives 0.0051.

17. $P(\texttt{b1}) = \frac{4}{12} \cdot \frac{5}{13} \cdot \frac{7}{11} = 35/429$, 3.62 bits, guess number 3: only `a1` and the empty string, which the model also scores, are more probable. $P(\texttt{a}) = \frac{6}{12} \cdot \frac{1}{11} = 1/22$, 4.46 bits, guess number 8. No password of the list ends after an `a`, so only the smoothing gives the end step a count; with $\delta = 0$ the probability is 0.

19. Lemma 4 gives $\lfloor 1000/7 \rfloor = 142$. For Lemma 3, $|F| = 3 < 5$ and $7.5\,r_M < (q + |F|)\,r_M = 8\,r_M$, so neither condition holds. The proof needs only $\sum_k \lfloor r_k / r_M \rfloor \ge q$, and here the sum is $2 + 2 + 2 = 6$.

20. After iteration 1, $B$, $D$ and $F$ hold 216 each. After iteration 2, $A$ 72, $C$ 180, $E$ 252, $G$ 72, $H$ 72. After iteration 3, $A$ 60, $B$ 180, $C$ 36, $D$ 144, $E$ 0, $F$ 132, $G$ 24, $H$ 24, $I$ 48. The ranking is $E, G, H, C, I, A, F, B, D$: the seed itself comes first, and the Sybil $F$ ranks above the honest $C$ and $A$. The guarantee of the entry excludes attack edges near the seeds.

21. $t_5 = 8$. Line L5 gives $t = 1032$ at all three times, with ages 0, 1 and 2, so line L6 passes. Line L7 compares $F_K(c, 1032)$ with the hash made for $t_0 = 1000$; for a random function these are independent, so the cookie is accepted with probability $2^{-24}$. Line L6 bounds the age of the rebuilt counter, not of the cookie; the hash check rejects a cookie that is 32 or more steps old, except with probability $2^{-24}$.

22. $E(p) = \frac{1}{p} + \frac{1}{p(1-p)} - \frac{1}{p(2-p)}$. $E(1/2) = 14/3 \approx 4.667$ and $E(5/9) = 1197/260 \approx 4.604$, so $1/2$ is not the best; the minimum is near $p = 0.557$. The value $p = 1/d$ maximizes the chance $p(1-p)^{d-1}$ of the rarest edge, so it minimizes the bound, not the mean.

23. With maxLength 24 the /25 is covered but too long: Invalid. Validating routers drop it, and the rest prefer it by longest prefix. With maxLength 25 it is Valid and more specific than the real /24, so every router that hears it sends the traffic for the /25 to the attacker. With a minimal ROA, the attacker who forges the origin must announce the /24 itself and compete on path length.

24. The Sybil totals are 0, 0, 54, 66 and 98. The bound is $0 + 54 + 30 + 42 = 126$. It counts only trust that enters over the attack edge; $F$ also sends trust back to $E$: 18 in iteration 3 and 10 in iteration 4, and $126 - 18 - 10 = 98$.

25. Fixed port: about 45 windows, so 45 seconds. Random ports: about 744,000 windows, about 8.6 days. Removing the TTL wait turns years into days. The random ID, the random port and 0x20 still multiply the work, ingress filtering still removes the forged sources, and DNSSEC still removes the race.
