A game or a flight simulator must draw a full frame in about 16 milliseconds, at sixty frames a second, with millions of pixels, thousands of lights and shadows, and surfaces that look like metal, cloth or skin. Real-time rendering is the set of methods that make this possible on a graphics processor. Most of them are approximations chosen for speed: a light integral replaced by a lookup table, a shadow by a depth map, a distant mountain by a coarser mesh. The craft lies in knowing what each shortcut costs in error and where the error shows.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Shading models.** Blinn-Phong and Oren-Nayar shading, the GGX distribution with the Smith masking term and Schlick's approximation, the Disney BRDF, and physically based shading with the split sum and linearly transformed cosines for area lights.
2. **Surface detail and textures.** Bump, normal, parallax, parallax occlusion and displacement mapping, texture compression such as S3TC and ASTC, virtual texturing, and procedural noise by Perlin, simplex and Worley.
3. **Lighting from the environment.** Cube maps and environment mapping, image-based lighting, irradiance maps with spherical harmonics, light maps, irradiance volumes and precomputed radiance transfer, with sky and atmosphere models.
4. **Shadows and screen-space effects.** Cascaded, variance and moment shadow maps, percentage-closer filtering and soft shadows, screen-space ambient occlusion in its SSAO, HBAO and GTAO forms, and screen-space reflections.
5. **Organizing the frame.** Deferred, tiled and clustered shading with the G-buffer and the visibility buffer, order-independent transparency, tone mapping, and stylized Gooch and toon shading.
6. **Level of detail.** Billboards and impostors, geomorphing, ROAM, geometry clipmaps and view-dependent refinement of terrain and meshes.

## What to read meanwhile

The [graphics pipeline](/graphics-pipeline/) is the frame in which every method of the chapter runs. [Texture mapping](/texture-mapping/), the [mipmap](/mipmap/) and [anisotropic filtering](/anisotropic-filtering/) cover the sampling that detail maps rely on, and [Phong shading](/phong-shading/) is the classic model that physically based shading replaces. For the physics of light, read the [rendering equation](/rendering-equation/), the [BRDF](/brdf/), [Lambertian reflectance](/lambertian-reflectance/), the [microfacet BRDF](/microfacet-brdf/) and the [Fresnel equations](/fresnel-equations/). [Shadow mapping](/shadow-mapping/), [ambient occlusion](/ambient-occlusion/) and [temporal antialiasing](/temporal-antialiasing/) are the base of the screen-space methods. For transparency, read [alpha blending](/alpha-blending/), [depth peeling](/depth-peeling/) and the [A-buffer](/a-buffer/). For level of detail, read [mesh simplification](/mesh-simplification/) and the [progressive mesh](/progressive-mesh/) of Volume 31, with [frustum culling](/frustum-culling/) and [occlusion culling](/occlusion-culling/) for what is not drawn at all.
