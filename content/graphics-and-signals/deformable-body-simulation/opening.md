Cloth that drapes and folds, hair that swings, a rubber ball that squashes on impact, muscle and fat that jiggle under a character's skin: these are deformable bodies, and animation simulates them. Unlike a rigid body, a deformable body has a shape that changes, so its state is the position of every vertex or particle, and its forces come from how far each small piece is stretched, sheared or bent. The equations are stiff. A cloth resists stretching far more than bending, and an explicit step must be tiny to stay stable, so most methods for animation step implicitly or recast each step as an optimization. Contact is the other hard part: cloth must never pass through itself, and the collision handling often costs more than the elasticity.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Particles and springs.** Particle systems, mass-spring systems and the fast mass-spring solver, with strain limiting for cloth that must not stretch.
2. **Continuum elasticity.** The deformation gradient and the material models built on it: St. Venant-Kirchhoff, neo-Hookean and its stable variant, corotational and invertible finite elements, modal reduction and brittle fracture.
3. **Cloth, shells and rods.** Implicit cloth after Baraff and Witkin, discrete shells and a quadratic bending model, Cosserat rods and discrete elastic rods for hair.
4. **Constraint and optimization solvers.** Position based dynamics and XPBD, projective dynamics, meshless shape matching, optimization time integration, vertex block descent and the case for many small steps.
5. **Collisions and contact.** Robust cloth collision with impact zones, incremental potential contact and affine body dynamics, which keep a simulation free of intersections.

## What to read meanwhile

The written chapter on [rigid body simulation](/rigid-body-simulation-problem/) covers the contact side: [impulse-based simulation](/impulse-based-simulation/), [projected Gauss-Seidel](/projected-gauss-seidel/), [continuous collision detection](/continuous-collision-detection/) and its [elementary tests](/elementary-ccd-tests/) between moving points, edges and triangles, which cloth collision uses directly. The local and global iteration of [as-rigid-as-possible deformation](/as-rigid-as-possible-deformation/) in Volume 31 is the pattern that projective dynamics extends to elastic energies.

For the numerics, Volume 12 has the [finite element method](/finite-element-method/), the [backward Euler](/backward-euler-method/), [symplectic Euler](/symplectic-euler-method/) and [Verlet](/verlet-integration/) integrators, [Newton's method](/newton-raphson-method/) for the nonlinear system of an implicit step, the [conjugate gradient method](/conjugate-gradient-method/) for its linear solves, and the [singular value decomposition](/singular-value-decomposition/) behind corotational and invertible elements.
