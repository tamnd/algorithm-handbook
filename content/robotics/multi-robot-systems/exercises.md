1. ◦ Four agents run the [Laplacian consensus protocol](/laplacian-consensus-protocol/) with unit weights, once on the path $1 - 2 - 3 - 4$ and once on the star with center 1. Find the eigenvalues of both Laplacians. Which graph agrees faster in continuous time? For the sampled protocol with $\varepsilon = 1/4$, find the factor $\max(\lvert 1 - \varepsilon\lambda_2\rvert, \lvert 1 - \varepsilon\lambda_r\rvert)$ by which the error shrinks per round on each graph.

2. ◦ Four agents on the cycle $1 - 2 - 3 - 4 - 1$ start at $x(0) = (4, 0, 0, 0)$ and run the sampled protocol $x(k+1) = x(k) - \varepsilon L x(k)$ with $\varepsilon = 1/4$. Compute three rounds. What is the limit, and which quantity stays the same in every round?

3. ◦ Three robots on the segment $[0, 1]$ with uniform density stand at $0.2$, $0.4$ and $0.5$. Do one step of the [distributed Lloyd coverage algorithm](/cortes-coverage-algorithm/) with gain $k = 1$: give the cells, the centroids and the cost $H$ before and after. What is the cost at the limit $1/6$, $1/2$, $5/6$?

4. ◦ Nine robots cover the unit square with uniform density. Evaluate the lower bound $H \ge A^2/(2\pi r)$ of [coverage control](/coverage-control/), and the cost of the grid with one robot at the center of each square of side $1/3$. By what factor is the grid above the bound?

5. ◦ Three robots and three tasks have these costs in seconds:

| | task 0 | task 1 | task 2 |
|---|---|---|---|
| robot 0 | 4 | 9 | 7 |
| robot 1 | 3 | 1 | 2 |
| robot 2 | 6 | 5 | 8 |

Find the result of the [contract net protocol](/contract-net-protocol/) with the full window, the result with one task per round in the order 0, 1, 2, and the minimum cost assignment.

6. ◦ Place each of these in the taxonomy of [multi-robot task allocation](/multi-robot-task-allocation/): (a) warehouse robots that each carry one shelf, assigned as orders arrive; (b) a table that needs two robots to lift; (c) delivery robots that plan the order of their next ten deliveries; (d) a drone that films a site and relays radio at the same time. Which of them is the assignment problem?

7. ◦ Six robots in the plane must hold a shape. How many sensing edges does a displacement-based formation need at least, and how many does a distance-based one need? How many in space? Three arms hold one object with rigid grasps, and in a second setup four point fingers with friction hold it. Find the dimension of the internal forces in each case, as in [cooperative manipulation](/cooperative-manipulation/).

8. ◦ Robots $A$ and $B$ of combined radius 1 m are 5 m apart on the $x$ axis, with $v_A = (1, 0)$ and $v_B = (-1, 0)$ m/s. Find the half-angle of the cone of [reciprocal velocity obstacles](/reciprocal-velocity-obstacles/) and its apex. Which of the new velocities $v'_A = (1, 0.15)$ and $(1, 0.25)$ m/s lie in $RVO_{A|B}$?

9. • Five robots stand at $0$, $0.8$, $1.6$, $2.4$ and $3.2$ on a line, with sensing range $V = 1$. Run [Ando's circumcenter algorithm](/ando-circumcenter-algorithm/) synchronously until they meet, with the safe disks. Give the positions and the diameter after each round, and check that no link is lost.

10. • Three robots at $(0, 0)$, $(2, 0)$ and $(0, 1)$ run [distance-based formation control](/distance-based-formation-control/) on the triangle graph with all target distances 1. Compute the squared errors, $V$ and the three inputs $u_i = -\sum_j e_{ij}(p_i - p_j)$. Check that the centroid does not move, and explain why each robot can compute its input in its own frame.

11. • In [leader-follower formation control](/leader-follower-formation-control/) with the follower at its target separation and bearing, the heading error obeys $\dot e = -(v_L/d)\sin e$. With $v_L = 0.5$ m/s, $d = 0.2$ m and $e(0) = 2$ rad, find the time until $\lvert e\rvert < 0.01$. What happens when the leader drives backward?

12. • Three robots on a path have edge weights $w_1$ and $w_2$. Show that $\lambda_2 = w_1 + w_2 - \sqrt{w_1^2 - w_1 w_2 + w_2^2}$. With $w_1 + w_2 = 2$, compare $(1, 1)$, $(1.25, 0.75)$ and $(1.5, 0.5)$, and check the concavity of $\lambda_2$ that [connectivity maintenance](/connectivity-maintenance/) uses.

13. • In [pebble motion](/pebble-motion-on-graphs/) on the cycle of 5 vertices, three labeled pebbles stand on three of the vertices. How many placements are there in all, and how many can be reached from a given one? Explain the count.

14. • Give a $2 \times 2$ utility matrix for which greedy assignment, largest utility first, gets only just over half of the optimum. Why does this show that the bound of the [consensus-based bundle algorithm](/consensus-based-bundle-algorithm/) cannot be improved for its rule?

15. • Robots $A$ and $B$ of combined radius $R = 1$ m are 6 m apart on the $x$ axis, with $v_A = (1, 0)$ and $v_B = (-1, 0)$ m/s. For [ORCA](/optimal-reciprocal-collision-avoidance/) with $\tau = 2$ s and $\tau = 4$ s, decide whether the relative velocity is in $VO^\tau_{A|B}$. In the case where it is, find $u$ and the new velocity of $A$ if $v_A$ is also its preferred velocity.

16. • Two robots hold a horizontal bar of 10 kg at the points $x = -0.5$ and $x = 0.5$ m, with planar point forces $(f_x, f_y)$. The center of mass is at $x = 0.2$ m. Find the vertical forces that hold the bar still, and the internal forces that leave the bar at rest.

17. • Two robots cover $[0, 1]$ with the density $\phi(q) = 2q$. Find the centroidal Voronoi configuration, and show that the border between the cells is $(\sqrt 5 - 1)/2$. Compare its cost with that of the uniform optimum $1/4$, $3/4$ under the same density.

18. ★ Show that the sampled consensus protocol on a connected bipartite $\Delta$-regular graph with $\varepsilon = 1/\Delta$ does not converge from every start. Start with two agents and one edge, and then show that $\lambda_r = 2\Delta$ for such a graph.

19. ★ Three labeled pebbles move on the 4-cycle, and then on the graph made by adding one chord to the 4-cycle. Count the placements that can be reached from a given one in each case, and explain the difference with the parity argument of the pebble motion entry.

20. ★ Prove the main step of ORCA: if $v'_A$ lies in $ORCA_{A|B}$ and $v'_B$ in $ORCA_{B|A}$, then $v'_A - v'_B$ is not in $VO^\tau_{A|B}$. Use that $VO^\tau_{A|B}$ is convex, and show this first.

21. ★ Prove that greedy assignment, largest utility first, gets at least half of the best total utility in the ST-SR-IA class. Then explain why greedy on costs, smallest cost first, has no constant bound.
