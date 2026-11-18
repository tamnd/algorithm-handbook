A warehouse runs two hundred robots that carry shelves to packing stations. No robot sees the whole floor. Each knows its own position, hears the robots within radio range, and senses the ones a few meters away. Orders arrive every second, and someone has to decide which robot fetches which shelf. Two robots that meet in an aisle must not collide, and they must not stop in a deadlock either. If the central computer fails, the robots should still finish the work in hand.

The chapter is about such teams. The new difficulty is not in one robot. It is in the information each robot has and in the graph of who senses or talks to whom, which changes as the robots move. Many of the results here are statements about that graph. Consensus converges when the graph is connected, or connected often enough over time. Formations hold when the graph makes the target shape rigid. Most of the distributed laws are gradient or averaging laws, and they reach a critical point or a local minimum, not the best configuration. The entries say which, and they separate theorems from measurements in simulation.

## What the chapter covers

1. **Teams and swarms.** A [multi-robot system](/multi-robot-system/) is a team with centralized, decentralized or distributed decisions. [Swarm robotics](/swarm-robotics/) studies many simple robots with local rules, and [boids](/boids/) are the classic flocking rules of separation, alignment and cohesion.
2. **Agreement and rendezvous.** The [Laplacian consensus protocol](/laplacian-consensus-protocol/) $\dot x = -Lx$ reaches the average on a connected undirected graph. [Multi-robot rendezvous](/multi-robot-rendezvous/) asks the robots to meet at a point, [Ando's circumcenter algorithm](/ando-circumcenter-algorithm/) solves it with a limited sensing range, and [connectivity maintenance](/connectivity-maintenance/) keeps the graph connected while the team moves.
3. **Formations.** [Formation control](/formation-control/) sorts the problem by what the robots sense. [Leader-follower formation control](/leader-follower-formation-control/) chains pairs of unicycles, and [distance-based formation control](/distance-based-formation-control/) follows the gradient of the distance errors.
4. **Coverage and search.** [Coverage control](/coverage-control/) places sensors to minimize the expected squared distance to an event, the [distributed Lloyd coverage algorithm](/cortes-coverage-algorithm/) moves each robot to the centroid of its Voronoi cell, and [visibility-based pursuit-evasion](/polygon-pursuit-evasion/) sweeps a polygon so that no evader can stay hidden.
5. **Task allocation.** [Multi-robot task allocation](/multi-robot-task-allocation/) gives the taxonomy of Gerkey and Matarić. [Market-based task allocation](/market-based-task-allocation/), the [contract net protocol](/contract-net-protocol/) and the [consensus-based bundle algorithm](/consensus-based-bundle-algorithm/) solve it with bids.
6. **Paths for many robots.** [Coupled and decoupled planning](/coupled-and-decoupled-planning/) sets completeness against speed, [prioritized planning](/prioritized-multi-robot-planning/) plans the robots one at a time in space-time, and [pebble motion on graphs](/pebble-motion-on-graphs/) is the discrete version.
7. **Avoiding each other on the fly.** [Reciprocal velocity obstacles](/reciprocal-velocity-obstacles/) share the avoidance between two robots, and [ORCA](/optimal-reciprocal-collision-avoidance/) turns each neighbor into a half-plane of safe velocities.
8. **One object, one map.** [Cooperative manipulation](/cooperative-manipulation/) shares a load among several arms, and [multi-robot SLAM](/multi-robot-slam/) merges the data of several robots into one map.

## A first reading

For a first pass, read these in order:

1. [Multi-robot system](/multi-robot-system/)
2. [Laplacian consensus protocol](/laplacian-consensus-protocol/)
3. [Multi-robot rendezvous](/multi-robot-rendezvous/)
4. [Formation control](/formation-control/)
5. [Coverage control](/coverage-control/)
6. [Distributed Lloyd coverage algorithm](/cortes-coverage-algorithm/)
7. [Multi-robot task allocation](/multi-robot-task-allocation/)
8. [Contract net protocol](/contract-net-protocol/)
9. [Coupled and decoupled planning](/coupled-and-decoupled-planning/)
10. [Prioritized planning](/prioritized-multi-robot-planning/)
11. [ORCA](/optimal-reciprocal-collision-avoidance/)

Distance-based formations, the bundle algorithm, pursuit-evasion and connectivity maintenance are closer to research and can wait for a second pass.

## Before you start

The chapter uses the [graph](/graph/) and its [Laplacian matrix](/laplacian-matrix/) from Volume 7, with the [assignment problem](/assignment-problem/), the [Hungarian algorithm](/hungarian-algorithm/) and the [auction algorithm](/auction-algorithm/). The convergence rates need the [eigenvalues](/eigenvalue/) of Volume 12. The [Voronoi cell](/voronoi-cell/), [Lloyd's algorithm](/lloyds-algorithm/) and the [minimum enclosing circle](/minimum-enclosing-circle/) are in Volume 13. [Seidel's linear programming](/seidel-linear-programming/) algorithm and the [submodular function](/submodular-function/) are in Volume 15. The planners use the [configuration space](/configuration-space/), [A* search](/a-star-search/) and [multi-agent pathfinding](/multi-agent-pathfinding/) from Volume 29, and distance-based formations use the [rigidity matrix](/rigidity-matrix/) and [infinitesimal rigidity](/infinitesimal-rigidity/) from Volume 31. [Feedback linearization](/feedback-linearization/) and the [LaSalle invariance principle](/lasalle-invariance-principle/) are in Volume 36. From this volume, read the [unicycle model](/unicycle-model/) and the [velocity obstacle](/velocity-obstacle/) in the chapter on mobile robots, the [grasp matrix](/grasp-matrix/) in the chapter on grasping, and [pose graph optimization](/pose-graph-optimization/) in the chapter on SLAM.
