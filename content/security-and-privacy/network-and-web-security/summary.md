## What to remember

- An origin is the triple (scheme, host, port). A script may read only what has its own origin, but any page may send requests anywhere, and cookies are scoped by domain and path, not by origin. Request forgery uses those requests.
- Injection is input that changes the syntactic structure of the output instead of staying inside one value. Prepared statements stop it in SQL, escaping by context in HTML. A content security policy with a fresh nonce and `strict-dynamic` limits which scripts run.
- A SYN flood keeps a table of $B$ half-open entries full when $rT \ge B$: 8.53 SYNs per second for $B = 256$ and $T = 30$ s. A SYN cookie holds 5 bits of time, 3 of MSS and 24 of a pseudorandom function; $q$ forged ACKs from off the path succeed with probability at most $q \cdot 2^{-24}$ plus the PRF advantage.
- Ingress filtering stops forged sources only in traffic from networks that deploy it. Strict reverse path checks drop real traffic on multihomed links.
- Packet marking receives the edge at distance $j$ with probability $p(1-p)^{j-1}$, and the mean number of packets is at most $H_d / (p(1-p)^{d-1})$: for $d = 10$, $p = 1/25$, the exact mean is 89.57 and the bound 105.73. Hash-based traceback never misses a router that forwarded a stored packet.
- Route origin validation stops wrong origins and too specific prefixes, not a forged origin at the end of a real-looking path. In the RFC 5452 model, $P_s = DRW/(NPI)$; only DNSSEC stops an attacker on the path.
- Password strength from a Markov or PCFG model is an estimate relative to its training list. Honeywords catch a login with a decoy with probability $1 - 1/k$ only for a flat generator.
- One entity with $\rho$ times the minimal resources presents $\lfloor \rho \rfloor$ identities, and without simultaneous tests any number (Douceur). SybilGuard accepts at most $gw$ Sybil identities per verifier; SybilRank's $O(g \log n)$ bound assumes fast mixing and attack edges at random honest nodes.

## The methods side by side

| Method | Against | Cost in the entry | What it does not stop |
|---|---|---|---|
| [Content security policy](/content-security-policy/) | injected scripts | one check per script | injected markup that is not a script, a leaked nonce |
| [Context-sensitive auto-escaping](/context-sensitive-auto-escaping/) | values that leave their context | $\Theta(n)$ per template | nothing in contexts it rejects, such as event handlers |
| [Parse-tree validation](/parse-tree-query-validation/) | inputs that change the query tree | $\Theta(n)$ per query | a wrong but well-formed value |
| [SYN cookies](/syn-cookies/) | backlog exhaustion | $O(1)$, no state per SYN | floods of completed connections |
| [Ingress filtering](/ingress-filtering/) | forged sources leaving a network | one prefix lookup per packet | forgery inside the prefix |
| [Probabilistic packet marking](/probabilistic-packet-marking/) | unknown attack paths | $O(1)$ per packet | tracing a single packet |
| [Hash-based IP traceback](/hash-based-ip-traceback/) | one forged packet | $O(k(V+E))$ per trace | packets older than the stored window |
| [Route origin validation](/route-origin-validation/) | wrong origin, too specific prefix | $O(L + c)$ per route | forged origins |
| [Firewall anomaly detection](/firewall-policy-anomaly-detection/) | conflicting rule pairs | $\Theta(m^2 d)$ | a rule hidden by a union of rules |
| [SybilGuard](/sybilguard/) | Sybil identities, no operator | $O(w^2 m)$ setup | many attack edges |
| [SybilRank](/sybilrank/) | fake accounts, one operator | $O((n + m) \log n)$ | attack edges near the seeds |

: Each method with the adversary and the cost of its entry. The limits are the ones the entries state; none of the methods replaces another.

## Choosing a method

For a web application, use prepared statements and a template engine that escapes by context. Add a nonce policy with `strict-dynamic`, first as report-only, and protect state-changing requests with a token or an `Origin` check, not with `SameSite` alone. Parse-tree validation is for code that must build queries from strings.

For a server, RFC 4987 lets a SYN cache be on by default and says SYN cookies should not be, because they lose TCP options. For a network, filter customer links, run route origin validation with minimal ROAs, and validate DNSSEC where zones are signed. Choose packet marking for floods of many packets through routers that keep no state, and hash-based traceback when one packet must be traced.

For passwords, hash them slowly, rate them with a smoothed Markov model or a PCFG trained on a list like the users' passwords, and test a honeyword generator for flatness. Against Sybil identities, an operator with the whole graph and seeds in each community uses SybilRank; an open system uses SybilGuard or SybilLimit. Both need a fast-mixing honest region with few attack edges.
