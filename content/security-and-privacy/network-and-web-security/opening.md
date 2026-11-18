The protocols of the Internet were designed for cooperating hosts, and the web for documents, not for programs from strangers. Both now carry banking and medicine, and both are attacked at every layer. A spoofed flood of TCP connection requests can exhaust a server's memory; a forged reply can poison a DNS cache and send a whole network to the wrong address; a false route announcement can pull another network's traffic through an attacker. On the web, a script injected into a page runs with the rights of the site, and a string pasted into a query can rewrite it.

Many of the defenses are small algorithms with exact properties. SYN cookies let a server keep no state for a half-open connection by encoding it in the sequence number. Parse-tree validation stops SQL injection by checking that user input did not change the structure of a query. Others are statistical, such as models that estimate how likely a password is, or graph methods that tell honest accounts from fake ones.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Web attacks and defenses.** The same-origin policy, cross-site scripting, cross-site request forgery and SQL injection, with content security policy, context-sensitive auto-escaping and parse-tree validation of queries.
2. **Network attacks.** SYN flooding and SYN cookies, DNS cache poisoning, BGP prefix hijacking with route origin validation, ingress filtering and firewall policy anomaly detection.
3. **Tracing attacks to their source.** The IP traceback problem, probabilistic packet marking and hash-based IP traceback.
4. **Passwords and humans.** Markov and probabilistic context-free grammar models of passwords, honeywords and the CAPTCHA.
5. **Sybil attacks.** The Sybil attack, Douceur's theorem that a system without a trusted authority cannot prevent it, SybilGuard and SybilRank.

## What to read meanwhile

The protocols under attack are in Volume 26: the [Border Gateway Protocol](/bgp/), [path-vector routing](/path-vector-routing/) and [packet classification](/packet-classification/), the algorithm a firewall runs on every packet. Hash-based traceback stores packet digests in a [Bloom filter](/bloom-filter/) of Volume 3. SYN cookies and honeywords rest on the [HMAC](/hmac/) and [password hashing](/password-hashing/) of Volume 23, and the [padding oracle attack](/padding-oracle-attack/) there shows how an error message becomes a decryption oracle.

The [probabilistic context-free grammar](/probabilistic-context-free-grammar/) of Volume 9 and the [Markov chain](/markov-chain/) of Volume 17 are the models behind password guessing. Parse-tree validation compares [abstract syntax trees](/abstract-syntax-tree/), also in Volume 9, and [taint analysis](/taint-analysis/) in Volume 34 finds the paths from user input to a query. SybilRank ranks accounts by short random walks, like [personalized PageRank](/personalized-pagerank/) in Volume 7, and its guarantee depends on the [mixing time](/mixing-time/) of Volume 17.
