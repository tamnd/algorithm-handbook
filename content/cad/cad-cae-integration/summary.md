## What to remember

- [Isogeometric analysis](/isogeometric-analysis/) uses the B-spline or NURBS basis of the CAD model for the geometry and the field. The elements are the nonempty knot spans, refinement keeps the geometry exact, and $n$ elements of degree $p$ with maximal smoothness carry $n + p$ functions per direction, against $pn + 1$ for $C^0$ elements.
- [Bézier extraction](/bezier-extraction/) writes the B-splines on an element as $N^e = C^e B$, where $B$ holds the Bernstein polynomials. Each $C^e$ is nonnegative and invertible, and its columns sum to 1. [k-refinement](/k-refinement/) raises the degree before inserting knots, so each new knot keeps $C^{p-1}$ smoothness.
- The [error bound for NURBS spaces](/nurbs-approximation-estimates/) is $h_K^{l-k}$ times a Sobolev norm of order $l$, for $0 \le k \le l \le p + 1$, with a constant that depends on the geometry. It is proved for h-refinement with the weights and the geometry fixed on the coarse mesh.
- [Quadrature](/isogeometric-quadrature/) with $p + 1$ Gauss points per direction is exact only for B-splines on an affine map with constant coefficients. A curved map of degree $p$ needs $\lceil 3p/2 \rceil$ points for the 1D mass matrix, and the stiffness integrand is rational.
- General [T-splines](/t-spline/) can have linearly dependent blending functions. [Analysis-suitable T-splines](/analysis-suitable-t-spline/), whose T-junction extensions do not cross, are [linearly independent](/t-spline-linear-independence/) for any knot values. The condition is sufficient, not necessary.
- [Hierarchical B-splines](/hierarchical-b-spline/) are linearly independent but are not a partition of unity. [Truncation](/truncated-hierarchical-b-spline/) restores the partition of unity and spans the same space. [LR B-splines](/lr-b-spline/) can be linearly dependent, and [PHT-splines](/pht-spline/) have dimension $4(V_b + V_+)$.
- A cut element whose active part is a fraction $\epsilon$ of its width has a mass diagonal of order $\epsilon^{2p+1}$ in [trimmed analysis](/trimmed-isogeometric-analysis/), so trimmed and immersed methods need a stabilization. The [finite cell method](/finite-cell-method/) puts a stiffness $\alpha$ in the void, and its error stalls at a level set by $\alpha$. The [cut finite element method](/cut-finite-element-method/) adds a ghost penalty and keeps the condition number $O(h^{-2})$ whatever the cut.
- [Volumetric spline parameterization](/volumetric-spline-parameterization/) has no general solution. Positive Bernstein coefficients of $\det J$ prove that a map is valid, and the test is sufficient, not necessary.
- [Defeaturing](/defeaturing/) changes the compliance by an integral over the removed feature only, but a small hole can still triple the local stress. [Mid-surface extraction](/midsurface-extraction/) is exact only for special shapes. Both are judged case by case.

| Method | Builds | Cost | Guarantee |
|---|---|---|---|
| T-spline | blending functions of $a$ anchors | $O(a(m + n))$ | local refinement; can be dependent |
| Analysis-suitable T-spline refinement | refined T-mesh | $O(kc(mn(m + n) + x^2) + a^2)$ | stays analysis-suitable, nested spaces |
| Hierarchical B-spline | selected functions of all levels | $O(Np^2)$ | independent; not a partition of unity |
| Truncated hierarchical B-spline | truncated functions | $O(Np^2 + kLmp^2)$ | independent, partition of unity, strongly stable |
| LR B-spline | one mesh line inserted | $O((b + s)mp)$ | partition of unity with weights; can be dependent |
| PHT-spline | one refinement step | $O(VL + nr)$ | $C^1$ bicubic, dimension $4(V_b + V_+)$ |
| Finite cell method | system on $m$ cut cells | $O(m(d + 1)gp^2 + (mp)^3)$ | error stalls for $\alpha > 0$; rates measured |
| Isogeometric collocation | system on $n$ functions | $O(np^2)$ | orders $p$ or $p - 1$, from numerical tests |
| Isogeometric BEM | dense boundary system | $O(n^2 g + n^3)$ | boundary only; observed orders |
| Mid-surface by shrinking balls | midline points | $O(n^2 k + m^2)$ | exact on a strip and an annular sector |

: Costs as the entries state them. $a$ anchors, $m \times n$ index lines, $k$ insertion edges, $c$ candidates per round, $x$ extensions; $N$ tensor B-splines of all levels, $L$ levels; $b$ functions and $s$ splits; $V$ vertices, $r$ split cells; $d$ bisection depth, $g$ Gauss points.

## Choosing a method

Start with tensor product NURBS and k-refinement for one patch or a few conforming patches, with Bézier extraction in an existing finite element code. For adaptive refinement, use truncated hierarchical B-splines when a partition of unity and simple data structures matter, and analysis-suitable T-splines when the model is already a T-spline. Check linear independence before using LR B-splines.

For a trimmed CAD solid, analyze the trimmed patches with a stabilization and weak boundary conditions, or immerse the part with the finite cell method or CutFEM. Defeature by the effect on the quantity you need, not by size, and keep every feature where a local stress is wanted. Extend mid-surfaces to the free edges. For new holes, use [topology optimization](/topology-optimization/) before shape optimization.
