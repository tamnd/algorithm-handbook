A service that runs on many servers needs a rule that sends each request, connection or key to one of them. The rule should spread the load evenly and adapt when servers are added, removed or fail. Often it must also send each key to the same server every time, where its cache or its shard of data lives. A web front end, a distributed cache, a sharded database and the equal-cost paths of a data-centre network all need such a rule.

Two results shape the field. If $n$ requests go to $n$ servers chosen uniformly at random, the busiest server receives $\Theta(\log n / \log\log n)$ of them with high probability. If each request instead looks at two random servers and joins the less loaded one, the maximum falls to $\ln\ln n / \ln 2 + O(1)$. The second concerns change. A key placed by $h(k) \bmod n$ almost always moves when $n$ changes; consistent hashing, from Karger and colleagues in 1997, maps keys and servers onto a ring so that adding a server moves only about a $1/n$ share of the keys.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **The problem.** Load balancers, load skew, sharding by hash and by range, remapping keys when servers change, and the properties a good mapping should have: balance, monotonicity, spread and load.
2. **Balancing policies.** Round robin and random choice with their weighted forms, least connections, least response time, peak EWMA, source address hashing, and the power of two choices with its maximum-load theorems.
3. **Consistent hashing.** The hash ring, virtual nodes, the maximum-load bound and bounded loads, multi-probe consistent hashing, rendezvous hashing and CARP, jump consistent hash, and Maglev hashing.
4. **Balancers in practice.** Layer 4 and layer 7 balancing, DNS balancing, ECMP, direct server return, sticky sessions, health checks, service discovery, failover, connection draining and load shedding.

## What to read meanwhile

Read the [hash table](/hash-table/), [hash function](/hash-function/), [universal hashing](/universal-hashing/) and [tabulation hashing](/tabulation-hashing/) entries of Volume 3. [Balls into bins](/balls-into-bins/) in Volume 1 derives the maximum load of random placement and states the effect of two choices.

[Dynamo-style replication](/dynamo-style-replication/) in Chapter 21.4 shows a hash ring with virtual nodes inside a real storage system. Health checks are failure detectors; read the [phi accrual failure detector](/phi-accrual-failure-detector/) and the [gossip protocol](/gossip-protocol/) in Chapter 21.7.

Balancing jobs rather than keys is a scheduling problem. [Online makespan minimization](/online-makespan-minimization/) in Volume 19 analyses the rule "send each job to the least loaded machine", and [online restricted assignment](/online-restricted-assignment-load-balancing/) adds machines that can serve only some jobs. In parallel programs, idle processors take work by [work stealing](/work-stealing/) (Volume 20).
