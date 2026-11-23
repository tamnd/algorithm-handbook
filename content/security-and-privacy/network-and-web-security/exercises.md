The models in these exercises are those of the entries. A [SYN cookie](/syn-cookies/) is CHECK-COOKIE with a 64-second counter, 5 bits of time, 3 bits of MSS and a 24-bit hash. [Packet marking](/probabilistic-packet-marking/) receives the edge at distance $j$ with probability $q_j = p(1-p)^{j-1}$, and the mean number of packets until all $d$ edges have arrived is $\sum_{\emptyset \ne S} (-1)^{|S|+1} / \sum_{j \in S} q_j$. The DNS race uses $P_s = DRW/(NPI)$ of RFC 5452. The [Markov](/markov-password-model/) and [PCFG](/pcfg-password-model/) password models are trained on the made-up lists of their entries.

1. ◦ Compare each URL with `http://intranet.example.org:8080/app/`: (a) `http://INTRANET.example.org:8080/other?x=1`, (b) `http://intranet.example.org/app/`, (c) `https://intranet.example.org:8080/app/`, (d) `http://intranet.example.org:8080/app/#top`, (e) `http://www.example.org:8080/app/`. Which are the same origin, and why not the others? A page of this origin embeds `https://cdn.example.net/lib.js`. With which origin does the script run?

2. ◦ A server keeps $B = 1024$ half-open connections and drops each after $T = 75$ s. What rate of forged SYNs keeps the table full? An attacker sends 20 SYNs per second into an empty table. When is the table full for the first time?

3. ◦ A resolver uses a fixed source port and may ask $N = 2$ authoritative servers; $D = 1$ and $I = 65536$. The attacker sends $R = 5000$ forged replies per second into windows of $W = 0.05$ s. Compute $P_s$ and the number of windows for a 50 percent chance of success. Repeat with random ports from a range of 16,384, and convert the windows to years for a TTL of one hour.

4. ◦ An attack path has $d = 3$ routers and each marks with $p = 1/2$. Give the probability that a packet arrives with the edge at distance 1, 2 and 3, and the probability that a mark written by the attacker survives to the victim. Compute the exact mean number of packets until all three edges have arrived, and compare it with the bound $H_d / (p(1-p)^{d-1})$.

5. ◦ A CAPTCHA shows 4 characters from an alphabet of 32. A program reads each character right with probability 0.5, a person with probability 0.95, independently. Give the chance that each passes one challenge, the mean number of challenges the program needs to pass once, and the chance of a blind guess.

6. ◦ A site stores $k$ sweetwords per user with a perfectly flat generator. An attacker who has cracked the file logs in once to each of two accounts, each time with one sweetword. Give the chance of an alarm on one login, and the smallest $k$ for which the chance of passing both logins is below $1/1000$.

7. ◦ Use the four VRPs of the example of [route origin validation](/route-origin-validation/). Give the state of each route: (a) 198.51.100.0/26 with origin 64497; (b) 198.51.100.0/23 with origin 64497; (c) 2001:db8:1fff::/48 with origin 64498; (d) 2001:db8:2000::/48 with origin 64498; (e) 192.0.2.0/24 with AS_PATH 64500 64496 64511. Then the VRP (192.0.2.0/24, 24, 64511) is added. Which states change?

8. ◦ A social graph has $n = 10^6$ honest nodes and $g = 50$ attack edges, and [SybilGuard](/sybilguard/) uses routes of length $w = 2000$. Bound the number of Sybil identities that one honest verifier accepts, and evaluate the bound $gw/n$ of Yu et al. on the chance that a random walk from a random honest node crosses an attack edge. What happens to both numbers with $g = 500$?

9. • The site `https://app.example.com` marks its session cookie `SameSite=Lax`, puts a token in its forms and rejects a POST whose `Origin` is not its own. For each request, say whether the browser sends the cookie and which checks reject it: (a) a form on `https://www.example.org` posts to `/transfer`; (b) a link on `https://www.example.org` opens `https://app.example.com/delete?id=7`, and the server deletes on GET; (c) a form on `https://forum.example.com`, a host of the same site run by other people, posts to `/transfer` with no token. (d) In case (c), the server checks only `Sec-Fetch-Site` and rejects the value `cross-site`. What happens?

10. • Run AUTO-ESCAPE on the template `<a href="` PRINT(u) `?q=` PRINT(v) `">` PRINT(t) `</a><script>var s = '` PRINT(w) `';</script>`, starting in HTML text. Give the context and the escaper of each hole, and the output for $u =$ `javascript:alert(1)`, $v =$ `a b&c`, $t =$ `<b>` and $w =$ `';alert(1)//`. Then a template has IF($b$, TEXT(`<a href="`), TEXT(`<i>`)) followed by PRINT(x). What does the algorithm do, and why?

11. • Use the template of the example of [parse-tree validation](/parse-tree-query-validation/), `SELECT a FROM t WHERE name = '` $x_1$ `' AND id = ` $x_2$. Which of these inputs are accepted, and for each rejected one, at which line? (a) $x_1 =$ `''`; (b) $x_1 =$ `it''s ''ok''`; (c) $x_1 =$ `x' OR name = 'y`; (d) $x_1 =$ `'''`; (e) $x_2 =$ `'7'`; (f) $x_2 =$ `7 OR id = 8`. Use the other input of the example where one is needed.

12. • In the worked table of [ingress filtering](/ingress-filtering/), a packet with source 192.0.2.1, an address with no specific route, arrives on the upstream link $i_0$. Give the decisions of strict mode and of loose mode as lines L4 and L6 are written. What does the result say about the order of the checks, and what change to line L4 restores it?

13. • A page is served with the policy of SERVE in [content security policy](/content-security-policy/) and the nonce $n$. Trace SCRIPT-ALLOWED for each script: (a) `<script nonce="n" src="https://cdn.example.net/app.js">`, written by the server; (b) a script element that `app.js` creates and appends; (c) `<script src="https://cdn.example.net/jsonp?callback=alert">`, injected through a comment field; (d) an injected inline `<script>alert(1)</script>`. (e) Which of them run if the header is `Content-Security-Policy-Report-Only`? (f) `app.js` builds the URL of the script in (b) from `location.hash`. Which assumption of the entry fails?

14. • For a path of $d = 10$ routers, compare $p = 1/10$ with $p = 1/25$: the value of $p(1-p)^{d-1}$, the bound $H_d / (p(1-p)^{d-1})$, the exact mean number of packets, and the chance $(1-p)^d$ that a mark of the attacker survives. What does the second probability cost the victim?

15. • In [hash-based IP traceback](/hash-based-ip-traceback/), every router has at most $d = 6$ neighbors and the path has $n = 20$ routers. Choose $p$ so that the theorem of Snoeren et al. bounds the expected number of extra routers by 1, and give the false-positive rate that each digest table may have. With the estimate $(1 - e^{-k/b})^k$ for $b$ bits per stored packet and $k$ hash functions, what is the smallest whole $b$ that meets it?

16. • A firewall has one field, the destination port, and default action allow: $R_1$ allows ports 0 to 499, $R_2$ allows ports 500 to 1023, $R_3$ denies ports 100 to 600. List what ANOMALIES reports for each pair. Is $R_3$ ever used? Run IS-DEAD on $R_3$ and give the pieces left after each subtraction.

17. • In the example of the Markov password model ($k = 1$, $\delta = 1$, $\sigma = 4$), compute $P(\texttt{b1})$ and $P(\texttt{a})$, their strengths in bits, and their guess numbers. Explain why the one-letter password $\texttt{a}$ is less probable than $\texttt{ab1}$, and what $\delta = 0$ gives for it.

18. • In the example of the PCFG password model, compute $P$, the strength and the guess number of $\texttt{star12}$, $\texttt{love99}$ and $\texttt{moon!}$. Which string has the same probability as $\texttt{moon!}$, and why does that make its guess number 12 and not 13?

19. • In Douceur's model, a system has $|C| = 1000$ correct entities and accepts an identity vouched for by $q = 7$ accepted identities, with no coordination of the intervals. How many identities can one minimally capable faulty entity present by Lemma 4? Now take $q = 5$ and three faulty entities with $2.5\,r_M$ resources each. Check the two conditions of Lemma 3, and show that the conclusion holds anyway.

20. • Run [SybilRank](/sybilrank/) on the graph of its example with the single seed $E$, the honest node of the attack edge, $T_G = 648$ and $w = 3$. Give the trust after each iteration, the trust per degree and the ranking. Which nodes are ranked wrongly, and which remark of the entry does this illustrate?

21. ★ A SYN cookie is made at counter $t_0 = 1000$ and checked with $A = 2$ at $now = 1032$, $1033$ and $1034$. What does line L5 give, and does line L6 reject? Which line rejects the cookie, and with what probability does it fail to, if $F_K$ is a random function? Correct the sentence "line L6 rejects every cookie older than 32 steps".

22. ★ For $d = 2$, write the exact mean number of packets $E(p)$ of packet marking as a function of $p$. Compute $E(1/2)$ and $E(5/9)$. Is $p = 1/d$ the best marking probability? What does $p = 1/d$ minimize instead?

23. ★ The prefix 198.51.100.0/24 belongs to AS 64496, which announces only the /24. An attacker announces 198.51.100.0/25 with the AS_PATH "attacker 64496", a forged origin. Give the state of the route under ROV with a ROA of maxLength 24 and with a ROA of maxLength 25, and say which traffic the attacker gets in each case. What does this say about the advice of RFC 9319 to use minimal ROAs?

24. ★ In the SybilRank example with seeds $C$ and $D$, compute the total trust in the Sybil region after each of the 4 iterations and the escape bound of the entry for $w = 4$. Why is the bound larger than the true value? Account for the difference exactly.

25. ★ The 85 years in the example of [DNS cache poisoning](/dns-cache-poisoning/) assume that a failed window costs one TTL. Suppose the attacker can start a new window every second, by making the resolver ask for a new name each time, and that a win on any of those names poisons the target. How long does a 50 percent chance take with a fixed port and with random ports from 16,384? Which defenses of the entry's table still count?
