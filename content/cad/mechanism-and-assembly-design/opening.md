A mechanism turns one motion into another: the crank of an engine into the stroke of a piston, the turn of a motor into the sweep of a wiper, the rotation of a camshaft into the timed lift of a valve. Designing linkages, cams and gears is a computational problem: given the motion wanted, find the link lengths, the cam contour or the tooth shape. Assembly raises a second problem: in what order can many parts go together, or come apart, so that each moves without collision.

The results are of several kinds. Some are exact theorems of plane geometry, such as the Grashof condition and the Aronhold-Kennedy theorem. Synthesis leads to polynomial systems: Burmester theory handles up to five positions, and the nine-point path problem was solved numerically, with 1442 solutions up to cognates. Limits on the transmission angle, the pressure angle of a cam and the contact ratio of gears are rules of practice, not theorems. In assembly, partitioning is NP-complete in the plane in the form Kavraki, Latombe and Wilson studied, while the non-directional blocking graph finds a removable subassembly in polynomial time when parts move by translations.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Linkages and their motion.** The four-bar linkage, the slider-crank, Watt and Stephenson six-bars, the Grashof condition, vector loop closure, Freudenstein's equation, instant centers and the Aronhold-Kennedy theorem, the transmission angle and coupler curves.
2. **Kinematic synthesis.** Function, path and motion generation, Chebyshev spacing of precision points, Burmester theory, standard-form dyad synthesis, nine-point path synthesis and optimization-based dimensional synthesis.
3. **What linkages can trace.** The Roberts-Chebyshev cognate theorem, the Peaucellier-Lipkin straight-line linkage and Kempe's universality theorem.
4. **Cams and gears.** Follower motion laws, cam profile synthesis and the pressure angle; the fundamental law of gearing, the involute tooth, generation by enveloping, undercutting, the contact ratio and Willis's formula for planetary trains.
5. **Assembly planning.** Liaison graphs, the De Fazio-Whitney precedence method, AND/OR graphs, assembly and disassembly sequence planning, assembly partitioning, non-directional blocking graphs, the motion space approach and design for assembly.

## What to read meanwhile

A mechanism is a framework that is not rigid, so the chapter on geometric constraint solving is the place to start: the [bar-and-joint framework](/bar-and-joint-framework/), [Maxwell's counting rule](/maxwell-counting-rule/), [degrees of freedom analysis](/degrees-of-freedom-analysis/) and [assembly constraint solving](/assembly-constraint-solving/). Synthesis equations need [polynomial system solving](/polynomial-system-solving/) and the [resultant](/resultant/) (Volume 11), and with [homotopy continuation](/homotopy-continuation/) and [Newton's method for systems](/newton-method-for-systems/) (Volume 12); Chebyshev spacing places precision points at [Chebyshev nodes](/chebyshev-nodes/).

For assembly, read the [configuration space](/configuration-space/), [motion planning](/motion-planning/) and the [piano movers problem](/piano-movers-problem/) in Volume 29, the [Minkowski sum](/minkowski-sum/) in Volume 13 and [topological sort](/topological-sort/) in Volume 7, which orders parts under precedence constraints. [Swept volume computation](/swept-volume/), in the chapter on CAM, checks the clearance of moving parts.
