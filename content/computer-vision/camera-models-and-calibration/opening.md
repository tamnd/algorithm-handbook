A camera on a robot has a focal length of 600 pixels and its principal point at pixel $(320, 240)$. A point 2 metres in front of the lens and 0.5 metres to the right lands at $u = 320 + 600 \cdot 0.5/2 = 470$. That one line holds the whole pinhole model: divide by the depth, scale by the focal length, shift by the principal point. Real lenses bend the rays, so the line needs a distortion term, and a wide lens breaks it altogether. With a focal length of 300 pixels, a ray at $60°$ from the axis lands $300 \tan 60° = 519.6$ pixels from the centre under the pinhole model, and a ray at $90°$ lands nowhere. A fisheye lens records that ray anyway, and the equidistant model puts it at $300 \cdot \pi/2 = 471.2$ pixels.

Calibration finds the numbers of the model from images. If the positions of some scene points are known, as on a printed checkerboard, the problem is a fit: linear algebra gives a first guess and a nonlinear least squares fit of the reprojection error refines it. If nothing in the scene is known, the images still constrain the camera, through the vanishing points of parallel lines or through the way points move from one view to the next, but some motions leave the answer ambiguous. The linear steps are exact for noise-free data and minimize an algebraic error; only the final fit minimizes the error in pixels, and it finds a local minimum.

## What the chapter covers

1. **The pinhole camera in homogeneous coordinates.** [Homogeneous coordinates](/homogeneous-coordinates/), the [extrinsic parameters](/camera-extrinsic-parameters/) $R$ and $t$ with the centre $C = -R^{\mathsf T} t$, the [intrinsic matrix](/camera-intrinsic-matrix/) $K$, the [projection matrix](/camera-projection-matrix/) $P = K[R \mid t]$, its [decomposition](/camera-matrix-decomposition/) by an RQ factorization, and the [affine camera](/affine-camera-model/).
2. **Calibration with a known target.** The [calibration problem](/camera-calibration/), [DLT resectioning](/dlt-camera-resectioning/) from at least six points, [Tsai's method](/tsai-calibration-method/), [Zhang's method](/zhang-calibration-method/) with a flat pattern, and [stereo calibration](/stereo-camera-calibration/) of a rig.
3. **Lens distortion and wide-angle cameras.** The [Brown-Conrady model](/brown-conrady-distortion-model/), the [division model](/division-distortion-model/), the [Kannala-Brandt fisheye model](/kannala-brandt-fisheye-model/) and the [unified omnidirectional model](/unified-omnidirectional-camera-model/).
4. **Vanishing points and the absolute conic.** The [image of the absolute conic](/image-of-the-absolute-conic/), [vanishing point detection](/vanishing-point-detection/) and [calibration from vanishing points](/vanishing-point-calibration/).
5. **Self-calibration.** The [Kruppa equations](/kruppa-equations/) and [self-calibration](/self-calibration/) from an unknown rigid scene.
6. **Cameras that are not a single pinhole.** The [rolling shutter model](/rolling-shutter-camera-model/) and the [generalized camera model](/generalized-camera-model/).

## A first reading

Read these 9 entries in order:

1. homogeneous coordinates;
2. camera extrinsic parameters;
3. camera intrinsic matrix;
4. camera projection matrix;
5. camera calibration;
6. DLT resectioning;
7. camera matrix decomposition;
8. Zhang's method;
9. Brown-Conrady distortion model.

Skip at first the absolute conic, the Kruppa equations, self-calibration, the omnidirectional and generalized models and Tsai's method. Come back to the fisheye models when you use a wide lens, and to the absolute conic after the fundamental matrix of Chapter 38.3, which the Kruppa equations and self-calibration need.

## Before you start

You need the [pinhole camera model](/pinhole-camera-model/) and the [pixel](/pixel/) from Volume 28, and [rigid body transformations](/rigid-body-transformation/) with the [special orthogonal group](/special-orthogonal-group/) from Volume 37. The linear algebra is the [QR decomposition](/qr-decomposition/), the [singular value decomposition](/singular-value-decomposition/) and the [least squares problem](/least-squares-problem/) of Volume 12, and the [cross product](/cross-product/) of Volume 13. Vanishing points start from [line detection](/line-detection/) (Volume 28). Several later entries lean on Chapter 38.3: the [projective plane](/projective-plane/), the [fundamental matrix](/fundamental-matrix/), the [essential matrix](/essential-matrix/) and the [projective reconstruction theorem](/projective-reconstruction-theorem/).

The roadmap below lists every entry of the chapter with its kind and level, and the figure after it shows which entries lean on which.
