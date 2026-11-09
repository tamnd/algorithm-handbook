## History

Euler's paper on the seven bridges of Königsberg, presented to the Saint Petersburg Academy in 1736 and printed in 1741, is usually taken as the start of graph theory. Euler showed that a route crossing every bridge once needs at most two land areas with an odd number of bridges, and stated without proof that the condition is also sufficient. Carl Hierholzer supplied the proof by splicing closed tours; he died in 1871, and the paper was published in 1873. Fleury's bridge-avoiding rule followed in 1883 and became the textbook method, while algorithm books later preferred Hierholzer's linear one.

Cycles through every vertex are named after William Rowan Hamilton, who in the 1850s sold a puzzle asking for such a cycle on the dodecahedron; Thomas Kirkman had studied the question for polyhedra a little earlier. No simple criterion was found, and Karp's 1972 list of NP-complete problems explained why. Sufficient conditions came instead: Gabriel Dirac's minimum-degree theorem in 1952, Øystein Ore's degree-sum version in 1960, and Bondy and Chvátal's closure in 1976, which unified them. Held and Karp gave the subset dynamic program in 1962, and it is still the best general worst-case bound for the travelling salesman problem.

The postman problem came from China. Kwan Mei-Ko posed it in 1962 with an optimality condition but no efficient method, and Alan Goldman gave it its English name. Edmonds and Johnson solved it in 1973 with Edmonds' weighted matching algorithm, and showed in the same paper that the directed version is a flow problem. On the scheduling side, the critical path method of Kelley and Walker in 1959 and the Navy's PERT computed longest paths in acyclic networks of activities.

Depth-first search, in Tarjan's 1972 paper, made cycle detection and many related tests linear. Itai and Rodeh found shortest cycles by breadth-first search in 1978, and Karp characterized the minimum cycle mean in a three-page note the same year. For listing, Tiernan in 1970 and Weinblatt in 1972 gave searches that could stall between outputs; Tarjan in 1973, Read and Tarjan in 1975 and Donald B. Johnson in 1975 gave methods with polynomial time per path or cycle. Fulkerson's 1956 proof of Dilworth's theorem through a split bipartite graph is the source of the path cover reduction.

## Further reading

- J. A. Bondy and U. S. R. Murty, *Graph Theory* (2008). Eulerian and Hamiltonian graphs, closures and the cycle space, with exercises.
- Herbert Fleischner, *Eulerian Graphs and Related Topics* (1990 and 1991). Two volumes on Euler tours, postman problems and their many variants.
- Ravindra K. Ahuja, Thomas L. Magnanti and James B. Orlin, *Network Flows* (1993). Karp's minimum mean cycle algorithm and its use in minimum-cost flow.
- Jeff Erickson, *Algorithms* (2019), Chapter 6. Depth-first search, cycle detection and longest paths in DAGs, explained with care.
- Alon Itai and Michael Rodeh, "Finding a minimum circuit in a graph", *SIAM Journal on Computing* (1978). Short, and still the base of shortest-cycle algorithms.
