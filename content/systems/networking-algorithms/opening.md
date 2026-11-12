A network moves packets between computers that share links, buffers and radio channels, with no central control and failures at any time. At every hop something must decide which path a packet takes, which queued packet goes next, how fast a sender may send, and what to do when a packet is lost. These rules run in every router and host, and their mistakes show: from 1986 the Internet went through a series of congestion collapses, in which links stayed busy but almost no data got through, until Van Jacobson added slow start and congestion avoidance to TCP.

Many of the algorithms are distributed forms of classic ones. Distance-vector routing is the Bellman-Ford algorithm run by every router on its neighbours' estimates, and link-state routing floods the topology so that each router can run Dijkstra's algorithm. A crossbar switch must find a matching between its inputs and outputs in every time slot. Fair queueing approximates an ideal fluid model in which flows share a link in proportion to their weights.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Reliable transfer.** Stop-and-wait, sliding windows with go-back-n and selective repeat, flow control, and Jacobson's and Karn's timeout rules.
2. **Congestion control.** AIMD, slow start, TCP Tahoe, Reno, Vegas and CUBIC, BBR, active queue management by RED, CoDel and PIE, ECN, and the fairness criteria behind them: max-min and proportional fairness, and network utility maximization.
3. **Routing.** Distance-vector routing and count-to-infinity, link-state and path-vector routing, BGP, the spanning tree protocol, multicast, ad hoc and geographic routing, compact routing, and lookup in Chord and Kademlia.
4. **Forwarding and switching.** Longest prefix match, packet classification, and switch scheduling by parallel iterative matching, iSLIP and the Birkhoff-von Neumann decomposition.
5. **Sharing a link.** Generalized processor sharing, weighted fair queueing and deficit round robin, and medium access by slotted ALOHA, CSMA/CD and CSMA/CA with exponential backoff.
6. **Interconnection networks.** Store-and-forward, wormhole and virtual cut-through switching, dimension-order, Valiant and Beneš routing, and network coding.

## What to read meanwhile

The routing algorithms are in Volumes 7 and 21: [Bellman-Ford](/bellman-ford/), [Dijkstra's algorithm](/dijkstra/), [distributed Bellman-Ford](/distributed-bellman-ford/), [flooding](/flooding/) and the [distributed spanning tree](/distributed-spanning-tree/). Switch scheduling is [bipartite matching](/bipartite-matching/) repeated every slot; see also [maximal matching](/maximal-matching/) and [edge coloring](/edge-coloring/). Routing many flows at once is the [multicommodity flow problem](/multi-commodity-flow-problem/). Longest prefix match is a search in a [trie](/trie/) or [radix tree](/radix-tree/).

Retransmission timers smooth round-trip times with an [exponential moving average](/exponential-moving-average/), and the [TCP acknowledgment problem](/tcp-acknowledgment-problem/) of Volume 19 asks when to delay acknowledgments. Volume 24 has the error detection in every packet, with the [cyclic redundancy check](/cyclic-redundancy-check/) and the [Internet checksum](/internet-checksum/), and the [fountain codes](/fountain-codes/) used to send data without retransmission.
