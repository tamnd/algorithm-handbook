A design says what a part is. A process plan says how to make it: which processes and machines, which
operations in which order, how the part is held, and at what speeds. This chapter is about the computations
that build such plans for machined parts, for sheet metal, and for cast and molded parts.

Take a small steel bracket. If it is milled from a block, the planner groups its holes and pockets into a few
setups, one for each way the block is clamped, orders the cuts in each setup to save tool changes, and picks
six locators and a clamp that hold the block in a known place. It then chooses a cutting speed from a tool
life law. If the same bracket is bent from sheet, the planner instead computes the flat blank with the bend
allowance of each bend, orders the cuts of the blank on the laser, and orders the bends so that no flange hits
the press brake. If it is cast, the planner checks that the part can leave its mold, and sizes risers that
freeze after the sections they feed.

The toolpaths that do the cutting, and the slicing and supports of 3D printing, are in the previous chapter on
CAM and additive manufacturing. Feature recognition, which finds the holes and pockets that a plan starts
from, is in the chapter on solid modeling. This chapter starts where those features are known.

Keep three kinds of result apart. Some are exact for their model: the rank test of a locator layout, the
form closure test of four planar contacts, the listing of all modular fixtures of one class, and the trace of a
parting line. Some are searches with a stated cost: A* over sets of done bends gives a cheapest plan for its
costs, while operation and cutting sequences are NP-hard orders, solved exactly by dynamic programming or branch and cut only when they are small. And some are
empirical laws with fitted constants: the K-factor, Taylor's tool life equation $V T^n = C$ and Chvorinov's
rule $t = B (V/A)^n$ come from tests, not theorems, and a plan built on them is as good as the constants.

## What the chapter covers

1. **Process plans.** [Computer-aided process planning](/computer-aided-process-planning/) in its variant
   and generative forms, and [manufacturability analysis](/manufacturability-analysis/).
2. **Setups and operation order.** [Setup planning](/setup-planning/) as a set cover over tool directions,
   and [operation sequencing](/operation-sequencing/) as a traveling salesman problem with precedence.
3. **Holding the part.** The [3-2-1 locating principle](/three-two-one-locating-principle/),
   [kinematic fixture analysis](/kinematic-fixture-analysis/), [fixture planning](/fixture-planning/) and the
   [Brost-Goldberg modular fixture algorithm](/modular-fixture-design/).
4. **Cutting conditions.** The [Taylor tool life equation](/taylor-tool-life-equation/) and
   [cutting parameter optimization](/cutting-parameter-optimization/).
5. **Bends and blanks.** The [K-factor](/k-factor/), the [bend allowance](/bend-allowance/),
   [flat pattern development](/flat-pattern-development/) and
   [springback compensation](/springback-compensation/).
6. **Cutting and bending order.** [Cutting sequence planning](/cutting-sequence-planning/),
   [bend sequence planning](/bend-sequence-planning/) and [A* bend sequencing](/a-star-bend-sequencing/).
7. **Molds.** [Draft angle analysis](/draft-angle-analysis/), [undercut detection](/undercut-detection/),
   [parting line generation](/parting-line-generation/),
   [gate location optimization](/gate-location-optimization/) and
   [conformal cooling design](/conformal-cooling-design/).
8. **Casting.** [Chvorinov's rule](/chvorinov-rule/), the
   [modulus method for risers](/riser-design-modulus-method/) and
   [casting hot spot detection](/casting-hot-spot-detection/).

## A first reading

For a first pass, read these entries in order:

1. [computer-aided process planning](/computer-aided-process-planning/)
2. [setup planning](/setup-planning/)
3. [operation sequencing](/operation-sequencing/)
4. [3-2-1 locating principle](/three-two-one-locating-principle/)
5. [kinematic fixture analysis](/kinematic-fixture-analysis/)
6. [Taylor tool life equation](/taylor-tool-life-equation/)
7. [K-factor](/k-factor/)
8. [bend allowance](/bend-allowance/)
9. [flat pattern development](/flat-pattern-development/)
10. [bend sequence planning](/bend-sequence-planning/)
11. [draft angle analysis](/draft-angle-analysis/)
12. [undercut detection](/undercut-detection/)
13. [Chvorinov's rule](/chvorinov-rule/)
14. [modulus method for riser design](/riser-design-modulus-method/)

They give one problem or law from each group. On a first pass you can skip the Brost-Goldberg algorithm,
springback compensation, the A* planner, parting lines, gates, cooling channels and hot spots. Each refines a
step from the list. The groups on sheet metal, molds and casting can be read in any order.

## Before you start

In this volume you need the [accessibility cone](/accessibility-cone/) and
[mold parting directions](/mold-parting-direction/) from CAM and additive manufacturing, and
[feature recognition](/feature-recognition/) and [offset surfaces](/offset-surface/) from solid modeling.

The orders and covers come from other volumes. Read [set cover](/set-cover/) in Volume 18, the
[traveling salesman problem](/traveling-salesman-problem/), [geometric programming](/geometric-programming/)
and [black-box optimization](/black-box-optimization/) in Volume 15, [topological sort](/topological-sort/)
and [spanning trees](/spanning-tree/) in Volume 7, and [state-space search](/state-space-search/) and
[A* search](/a-star-search/) in Volume 29.

The fixture pages use the [rank](/rank/) of a matrix from Volume 11 and [Farkas' lemma](/farkas-lemma/) from
Volume 15. The casting and bending pages use the [heat equation](/heat-equation/) and
[fixed-point iteration](/fixed-point-iteration/) from Volume 12, and the
[distance transform](/distance-transform/) and [silhouette edges](/silhouette-edge/) from Volume 28.
