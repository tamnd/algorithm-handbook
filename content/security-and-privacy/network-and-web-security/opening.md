A user is logged in to a bank at `https://bank.example`. In another tab she opens a page of `https://www.example.org`, which holds a hidden form that posts a transfer to the bank. The bank set its session cookie with `SameSite=None`, so the browser sends it with the post, as it sends such a cookie with every request to its site, whoever starts the request. The bank sees a valid session and moves the money. Nothing was broken: the browser, the cookie and the bank all did what the protocols say. The attack works because one fact, "this request carries my cookie", was taken as proof of a second fact, "the user asked for this".

The network has the same weakness at every layer. A TCP server keeps state for each SYN it receives, and the source address of a SYN is whatever the sender wrote. A router believes the origin AS of a route announcement. A DNS resolver accepts the first reply whose question, query ID, addresses and ports match. An open peer-to-peer system counts identities, and an identity costs almost nothing. In each case the attacker supplies a value that the receiver trusts and does not check.

The defenses of the chapter add the missing check, and they come in three kinds. Some add a secret that an attacker off the path cannot see: a CSRF token, a script nonce, the hash in a SYN cookie, the random ID and port of a DNS query. These stop an attacker who cannot read the traffic, and nothing more. Some add a signature: route origin authorizations for BGP and DNSSEC for names. Some add structure that the attacker cannot fake: the parse tree of a query, the context of a template hole, the few edges between fake accounts and real ones in a social graph. Each entry states its adversary, and a defense is only as good as the match between that adversary and the real one.

## What the chapter covers

1. **The browser's boundary.** The [same-origin policy](/same-origin-policy/) limits reads to the scheme, host and port of the page but lets any page send requests. [Cross-site request forgery](/cross-site-request-forgery/) and [cross-site scripting](/cross-site-scripting/) are the two attacks that follow, and a [content security policy](/content-security-policy/) and [context-sensitive auto-escaping](/context-sensitive-auto-escaping/) are defenses against the second.
2. **Injection into queries.** [SQL injection](/sql-injection/) changes the structure of a query; [parse-tree validation](/parse-tree-query-validation/) compares the tree with the inputs against the tree the programmer meant.
3. **Floods and forged sources.** [SYN flooding](/syn-flooding/) fills the table of half-open connections when $rT \ge B$; [SYN cookies](/syn-cookies/) store nothing until the client answers, and [ingress filtering](/ingress-filtering/) drops forged sources at their edge.
4. **Tracing packets back.** The [IP traceback problem](/ip-traceback-problem/) asks for the attack path; [probabilistic packet marking](/probabilistic-packet-marking/) rebuilds it from many packets and [hash-based IP traceback](/hash-based-ip-traceback/) from one.
5. **Routing, naming and filtering rules.** [BGP prefix hijacking](/bgp-prefix-hijacking/) and its partial defense [route origin validation](/route-origin-validation/), [DNS cache poisoning](/dns-cache-poisoning/) with the RFC 5452 model of the race, and [firewall policy anomaly detection](/firewall-policy-anomaly-detection/) for rule lists that contradict themselves.
6. **Passwords and humans.** The [CAPTCHA](/captcha/), two models of password guessing, the [Markov password model](/markov-password-model/) and the [PCFG password model](/pcfg-password-model/), and [honeywords](/honeywords/), which detect the use of a stolen password file.
7. **Many identities.** The [Sybil attack](/sybil-attack/), [Douceur's theorem](/sybil-impossibility-theorem/) on why it cannot be stopped without an authority or strong assumptions, and two defenses on social graphs, [SybilGuard](/sybilguard/) and [SybilRank](/sybilrank/).

## A first reading

Read these in order:

1. [Same-origin policy](/same-origin-policy/)
2. [Cross-site request forgery](/cross-site-request-forgery/)
3. [Cross-site scripting](/cross-site-scripting/)
4. [SQL injection](/sql-injection/)
5. [SYN flooding](/syn-flooding/)
6. [SYN cookies](/syn-cookies/)
7. [Ingress filtering](/ingress-filtering/)
8. [IP traceback problem](/ip-traceback-problem/)
9. [Probabilistic packet marking](/probabilistic-packet-marking/)
10. [BGP prefix hijacking](/bgp-prefix-hijacking/)
11. [DNS cache poisoning](/dns-cache-poisoning/)
12. [Sybil attack](/sybil-attack/)

The content security policy and route origin validation are the next two to read, since they are what sites and networks deploy. Auto-escaping, parse-tree validation, firewall anomalies, the password models, honeywords and the Sybil defenses can wait; each builds on one entry of the first reading and on nothing else in the chapter.

## Before you start

The network entries assume the basics of TCP and IP: the three-way handshake, source and destination addresses, and forwarding by [longest prefix match](/longest-prefix-match/). Routing uses [BGP](/bgp/) and firewalls use [packet classification](/packet-classification/) and the [access control list](/access-control-list/) of Chapter 45.1. SYN cookies need an [HMAC](/hmac/) or another [pseudorandom function](/pseudorandom-function/), and honeywords sit on top of [password hashing](/password-hashing/). The web entries assume HTML, URLs and cookies, and the query entries a [context-free grammar](/context-free-grammar/) and its [parse tree](/parse-tree/). For the analyses: the [geometric distribution](/geometric-distribution/) and the [coupon collector problem](/coupon-collector-problem/) for packet marking, the [Bloom filter](/bloom-filter/) for hash-based traceback, the [n-gram language model](/n-gram-language-model/) with [Laplace smoothing](/laplace-smoothing/) and the [probabilistic context-free grammar](/probabilistic-context-free-grammar/) for passwords, and the [Markov chain](/markov-chain/), its [mixing time](/mixing-time/) and [power iteration](/power-iteration/) for the Sybil defenses.
