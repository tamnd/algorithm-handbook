Between a finished design and a finished part lies the process plan: which processes, machines and tools, which operations in which order, how the part is held, and at what speeds. For a machined part the plan groups features into setups and orders the cuts. For a sheet metal part it finds the flat blank and the order of the bends. For a cast or molded part it chooses the parting line, checks draft and undercuts, and places risers, gates and cooling channels. Experienced planners long did this by hand; computer-aided process planning either adapts the plan of a similar part or derives a new one from the geometry.

The methods are of three kinds, and the entries will keep them apart. Some are geometric tests: draft angle analysis, undercut detection, and the rank test of kinematic fixture analysis; the Brost-Goldberg algorithm is complete, listing every fixture of its class. Some are searches over orders: A* search over bend sequences, and cutting sequences posed as a generalized traveling salesman problem, which is NP-hard, so large instances are solved by heuristics. And some are empirical laws with fitted constants: Taylor's tool life equation, Chvorinov's rule, the modulus method for risers and typical K-factor values are rules from experiment, not theorems.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Process plans.** Computer-aided process planning, manufacturability analysis, setup planning and operation sequencing.
2. **Holding the part.** The 3-2-1 locating principle, fixture planning, kinematic fixture analysis and the Brost-Goldberg modular fixture algorithm.
3. **Machining parameters.** The Taylor tool life equation and cutting parameter optimization.
4. **Sheet metal.** The K-factor, bend allowance, flat pattern development, bend sequence planning and its A* search, springback compensation and cutting sequence planning.
5. **Molding and casting.** Draft angle analysis, undercut detection, parting line generation, gate location optimization, conformal cooling channels, casting hot spot detection, Chvorinov's rule and the modulus method for riser design.

## What to read meanwhile

The chapter on CAM and additive manufacturing holds the nearest written entries: [mold parting direction](/mold-parting-direction/), which decides whether a polyhedral part can be made in a two-piece mold, the [accessibility cone](/accessibility-cone/) used for setups, [toolpath planning](/toolpath-planning/), [pocket machining](/pocket-machining/), the [irregular nesting problem](/nesting-problem/) for sheets and [tolerance stack-up analysis](/tolerance-stack-up/). Process planning starts from features, so read [feature-based modeling](/feature-based-modeling/), [feature recognition](/feature-recognition/) and [attributed adjacency graph recognition](/attributed-adjacency-graph/) in the chapter on solid modeling.

The search and optimization tools are elsewhere: [A* search](/a-star-search/) (Volume 29), the [traveling salesman problem](/traveling-salesman-problem/) and the [linear programming problem](/linear-programming-problem/) (Volume 15), and [topological sort](/topological-sort/) (Volume 7) for orders under precedence. The [distance transform](/distance-transform/) (Volume 28) is one way to find the hot spots of a casting.
