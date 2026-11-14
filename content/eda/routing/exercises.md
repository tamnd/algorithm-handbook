1. ◦ A channel has ten columns, with top pins $2, 1, 0, 3, 1, 4, 0, 4, 5, 0$ and bottom pins $0, 2, 2, 0, 3, 0, 5, 3, 0, 4$ (0 is no pin). Give the interval of each net, the local density of every column and the [density](/channel-density/) $d$. List the edges of the [vertical constraint graph](/vertical-constraint-graph/), run the [left-edge algorithm](/left-edge-algorithm/) and say which nets share a track. Is the result optimal?

2. ◦ A routing grid has six rows, numbered 0 to 5 from the top, and six columns, numbered 0 to 5 from the left. Row by row, with `#` for a blocked cell, the rows are `......`, `.####.`, `....#.`, `###.#.`, `s...#t` and `....#.`, so $s$ is the cell in row 4, column 0 and $t$ the cell in row 4, column 5. Run [Lee's algorithm](/lee-maze-routing/) and give the length of a shortest path, the number of shortest paths, and the detour number of a shortest path as defined by [Hadlock's algorithm](/hadlock-algorithm/). Separately, on another grid, Hadlock's algorithm reaches $t = (7, 5)$ from $s = (1, 2)$ with detour number 3. How long is the path it returns?

3. ◦ For each of Lee's algorithm, Hadlock's algorithm, [Soukup's algorithm](/soukup-algorithm/), the line-probe router of Mikami and Tabuchi and the line-probe router of Hightower ([line-probe routing](/line-probe-routing/)), say whether it always finds a path when one exists, and whether the path it finds is always a shortest one.

4. ◦ Take the pins $(0,0)$, $(0,5)$, $(2,3)$, $(6,3)$ and $(6,0)$. How many points has the Hanan grid, and how many of them are candidate Steiner points that are not pins? Compute the length of the [rectilinear minimum spanning tree](/rectilinear-minimum-spanning-tree/). Give two lower bounds on the rectilinear Steiner minimal tree, one from [Hwang's theorem](/hwang-rectilinear-steiner-ratio/) and one from the half-perimeter of the bounding box. The true optimum is 14; how far is each bound from it?

5. ◦ In [river routing](/river-routing/), the top terminals are at columns $a = (4, 5, 6, 7, 8)$ and the bottom terminals at $b = (1, 2, 3, 9, 10)$, wire $i$ joining $a_i$ to $b_i$. Use the cut condition to find the least number of tracks $h$, and name the pair of wires that rules out each smaller $h$.

6. ◦ A $4 \times 4$ grid of gcells $(x, y)$, $0 \le x, y \le 3$, has capacity 1 on every edge. The two-pin nets are A from $(0,0)$ to $(3,0)$, B from $(1,1)$ to $(2,1)$, C from $(0,2)$ to $(3,3)$, D from $(1,3)$ to $(2,0)$, E from $(0,1)$ to $(2,2)$ and F from $(1,0)$ to $(3,2)$. Give the half-perimeter lower bound on the wirelength of a [global routing](/global-routing/). Use the cut between the columns $x \le 1$ and $x \ge 2$ to bound the total overflow, the integral congestion and the fractional congestion $\lambda^*$ from below.

7. ◦ Run the update rules of [negotiated congestion routing](/negotiated-congestion-routing/) with the defaults $\mathrm{pres\_first} = 0$, $\mathrm{pres\_init} = 1/2$, $\mathrm{pres\_mult} = 3/2$ and $\mathrm{hist\_fac} = 1$, base cost 1. Give pres_fac in iterations 1 to 4. An edge of capacity 2 carries 3, 2 and 4 nets at the end of iterations 1, 2 and 3. What is its history cost in iteration 4, and what does it cost a net in iteration 4 when 2 other nets use it? When 1 other net uses it?

8. ◦ A chip has four routing layers, 1 and 3 horizontal, 2 and 4 vertical, and all pins are on layer 1. A net is the L-shaped route from the pin $(0,0)$ along a horizontal segment to $(3,0)$ and then along a vertical segment to the pin $(3,2)$. A via between layers $\ell$ and $\ell + 1$ counts once, and a stack from $\ell$ to $\ell'$ counts $|\ell' - \ell|$. Give the number of vias for the [layer assignments](/layer-assignment/) (1, 2), (3, 2) and (3, 4), where the pair gives the layers of the horizontal and the vertical segment.

9. ◦ State the complexity of each problem, as given by the entries: the minimum number of tracks for a channel without doglegs; the same with doglegs; the same when the vertical constraint graph has no edges; deciding whether a channel can be routed at all without doglegs; the least width of a river routing; deciding whether a [switchbox](/switchbox-routing/) can be routed.

10. ◦ A run of the [multicommodity flow](/multicommodity-flow-global-routing/) router has $k = 200$ nets on a grid of $100 \times 100$ gcells whose smallest edge capacity is 4, so $\rho = k / \min c = 50$. Take $\varepsilon = 1/10$ and suppose $\lambda^* = 1$. How many rounds $T$ does the condition $T \ge 2\rho \ln|E| / (\varepsilon^2 \lambda^*)$ ask for, and what bound on $\lambda_{\mathrm{frac}}$ does it give?

11. ◦ The chain of the source $(0,0)$ and the points $(1,3)$, $(2,6)$, $(3,9)$, $(6,9)$, $(9,9)$, $(9,6)$, $(9,3)$, $(9,0)$ has a minimum spanning tree of cost 27, and the farthest point is at distance $R = 18$ from the source. Give the radius and cost bounds of the [bounded-radius bounded-cost tree](/bounded-radius-bounded-cost-tree/) for $\varepsilon = 1/2$ and the radius bound of the [Prim-Dijkstra tree](/prim-dijkstra-tradeoff/) for $c = 1/2$. The entries report cost 63 and radius 18 for the first, cost 33 and radius 18 for the second. Which bounds are far from these values?

12. • A channel has top pins $1, 1, 2, 3$ and bottom pins $2, 3, 4, 4$. Find the density, the vertical constraint graph and the number of nets on its longest path. Show that every routing without doglegs needs 4 tracks, so the larger of the two lower bounds is not reached. Does [dogleg routing](/dogleg-channel-routing/) at pin columns help here?

13. • For $N \ge 2$, build a channel of $N$ two-pin nets with density 2 whose optimal routing without doglegs needs $N$ tracks. Write it out for $N = 4$ and say why doglegs at pin columns do not help.

14. • In river routing, the top row $a = (1, 3, 5, 6)$ may be shifted by an integer $s$, giving $a + s$, while the bottom row stays at $b = (2, 3, 7, 9)$. For $h = 1, 2, 3$ tracks, find all shifts $s$ for which the cut condition holds.

15. • Prove that the cut condition of river routing is sufficient for $h = 1$: if $a_{i+1} - b_i \ge 1$ and $b_{i+1} - a_i \ge 1$ for all $i$, the wires can be routed in one track.

16. • Run [iterated 1-Steiner](/iterated-one-steiner/) on the pins $(0,2)$, $(2,0)$, $(5,3)$ and $(3,5)$. Give the minimum spanning tree, each Steiner point added with its gain, and the final length. Prove that the result is optimal, and give the ratio of the spanning tree to the optimum.

17. • The source is $s = (0,0)$ and the sinks are $p_1 = (0,2)$, $p_2 = (4,5)$, $p_3 = (8,2)$ and $p_4 = (1,5)$. Build the Prim-Dijkstra tree for $c = 0$ and for $c = 1/2$. Give the cost and the radius of each, and compare the radius for $c = 1/2$ with the bound $R/c$.

18. • In the $2 \times 2$ grid of gcells with capacity 1 on its four edges, net A joins $(0,0)$ and $(1,1)$, and net B joins $(1,0)$ and $(0,1)$. Compute the cut bound $k_S - c(S)$ on the total overflow for every set $S$ of gcells, and compare the best of them with the least overflow of a routing. What does this say about the cut bound?

19. • On a grid with no obstacles, $s$ and $t$ are at Manhattan distance $L$, far from the border. Count the cells within distance $r$ of $s$. How many cells does Lee's algorithm label before it labels $t$, at least? About how many does a search label that grows waves from $s$ and from $t$ at the same time and stops when they meet?

20. • The multicommodity flow entry bounds the average congestion by $\lambda_{\mathrm{frac}} \le (1+\varepsilon)\lambda^* + \rho \ln|E| / (T \ln(1+\varepsilon))$. Derive from it that $T \ge 2\rho\ln|E|/(\varepsilon^2\lambda^*)$ rounds give $\lambda_{\mathrm{frac}} \le (1+2\varepsilon)\lambda^*$ for $0 < \varepsilon \le 1$. Then, for the numbers of Exercise 10, find the smaller number of rounds that gives the same bound when $\ln(1+\varepsilon)$ is used as it is.

21. • In river routing, let $a_i = i$ and $b_i = i + s$ for $i = 1, \ldots, n$, with an integer $s \ge 1$. Show with the cut condition that the least width is $n$, whatever $s$ is, and explain the answer by the shape of the wires.

22. • The density entry notes that when both layers may carry trunks, the lower bound becomes $\lceil d/2 \rceil$. Give a channel with two nets and $d = 2$ that can be routed in one track in that model, and say on which layer each trunk and each branch runs.

23. • Two nets share an edge $e_1$ of capacity 1; every other edge has capacity 1 and is used by one net only. Net A has two routes, $\{e_1, e_2\}$ and $\{e_3, e_4, e_5\}$; net B has $\{e_1, e_6\}$ and $\{e_7, e_8, e_9, e_{10}\}$. Run negotiated congestion with the defaults of Exercise 7, base cost 1, rerouting A before B in each iteration and taking the cheaper route. Give the costs each net sees, its choice in each iteration, and the iteration that ends without overflow. Which net gives up its short route, and why that one?

24. ★ On the $3 \times 3$ grid of gcells $(x, y)$ with capacity 1 on all 12 edges, the nets join $(0,0)$ to $(2,2)$, $(2,0)$ to $(0,2)$ and $(1,0)$ to $(1,2)$. The multicommodity flow entry finds $\lambda^* = 1$ and, by exhaustive search, an integral optimum of 2. Prove by hand that every integral routing has congestion at least 2.

25. ★ In the global form of layer assignment, a net is a tree of horizontal and vertical segments, each segment may take any of a given set of layers of its direction, and at each node of the tree the vias form a stack from the lowest to the highest layer present there, with layer 1 present at a pin. Give a dynamic program that minimizes the vias of one net exactly, and bound its running time in terms of the number of segments and the number of layers $L$.

26. ★ Prove that the cut condition of river routing is sufficient for every $h$. Describe the route of wire $i$ by the columns where it moves from track to track, and show that the needed inequalities between these columns can be met exactly when the cut condition holds.

27. ★ Prove that the rectilinear Steiner minimal tree of the four corners of an $a \times b$ rectangle has length $a + b + \min(a, b)$.

28. ★ Lee's backtrace can work with a label $f(k)$ that depends only on the distance $k$ and takes values in $\{0, 1\}$. Show that a sequence $f$ works for every grid exactly when $f(k-1) \ne f(k+1)$ for all $k \ge 1$, find all such sequences, and explain why 0, 1, 0, 1, … fails. How many bits does a cell need in all?
