## History

The phase problem was first met in X-ray crystallography. Patterson (1934) showed that the measured
intensities give the autocorrelation of the electron density, a map of interatomic vectors, and Harker
(1936) used the symmetry of the crystal to read it. Karle and Hauptman
(1950) derived inequalities among the structure factors from the nonnegativity of the density, Sayre (1952)
gave his equation for a density of equal, separated atoms, and Cochran (1955) the probability law for the
triplet phases. Karle and Hauptman shared the 1985 Nobel
Prize in Chemistry for these direct methods. Oszlányi and Sütő (2004) added charge flipping,
which uses no phase probabilities.

In optics the phase was first recorded. Gabor (1948) proposed in-line holography and
met the twin image at once; Leith and Upatnieks (1962) separated the twin with an off-axis reference,
Takeda, Ina and Kobayashi (1982) gave the Fourier method of selecting one sideband, and Schnars and Jüptner
(1994) reconstructed a hologram recorded on a CCD numerically. Teague (1983) derived the transport of
intensity equation, which finds the phase from a focal series without a reference, and Paganin and Nugent
(1998) gave the noninterferometric form used with X-rays.

Iterative phase retrieval began with Gerchberg and Saxton (1972), who used the image and diffraction
plane intensities of an electron microscope. Fienup (1978) replaced the image intensity by an object
constraint, and his 1982 comparison of algorithms proved that the error of error reduction does not
increase and introduced hybrid input-output, which works much better and has no convergence proof. The
question of when a solution is unique was settled in the same years: Hayes, Lim and Oppenheim (1980)
described the many solutions in one dimension, and Bruck and Sodin (1979), Hayes (1982) and Bates (1982)
showed that in two or more dimensions almost every image is fixed up to the trivial ambiguities. Miao, Sayre and
Chapman (1998) turned a remark of Sayre (1952) on finer sampling into the oversampling rule.

Miao, Charalambous, Kirz and Sayre (1999) recorded an oversampled X-ray pattern of a non-periodic object
and recovered its image, which started coherent diffraction imaging. Bauschke, Combettes and Luke (2002)
read the algorithms as projection methods and identified HIO with $\beta = 1$ as Douglas-Rachford; Elser
(2003) gave the difference map, Marchesini and coworkers (2003) the shrinkwrap support update, and Luke
(2005) RAAR. Ptychography goes back to Hoppe (1969); Rodenburg and Faulkner (2004) gave the iterative PIE,
Thibault and coworkers (2008) refined object and probe together, Maiden and Rodenburg (2009) gave ePIE, and
Zheng, Horstmeyer and Yang (2013) moved the idea to Fourier space.

A theory with guarantees came from frame theory and compressed sensing. Balan, Casazza and Edidin (2006)
asked which measurement vectors determine a signal from magnitudes and found the $2n - 1$ count for real
signals; Conca, Edidin, Hering and Vinzant (2015) proved $4n - 4$ generic vectors suffice in the complex
case. Candès, Strohmer and Voroninski (2013) gave PhaseLift, and Candès and Li (2014) brought its count to
the order of $n$. Candès, Li and Soltanolkotabi (2015) proved that Wirtinger flow
from a spectral start converges for Gaussian measurements. These results are for random measurement models, not for the Fourier data of an experiment.

## Further reading

- Yoav Shechtman, Yonina C. Eldar, Oren Cohen, Henry N. Chapman, Jianwei Miao and Mordechai Segev, "Phase
  retrieval with application to optical imaging: a contemporary overview", *IEEE Signal Processing
  Magazine* 32(3), 2015. A survey of uniqueness, the classical algorithms and the
  convex methods, with optical and X-ray applications.
- James R. Fienup, "Phase retrieval algorithms: a comparison", *Applied Optics* 21(15), 1982. Defines the
  input-output algorithms and compares them with error reduction.
- Heinz H. Bauschke, Patrick L. Combettes and D. Russell Luke, "Phase retrieval, error reduction algorithm,
  and Fienup variants: a view from convex optimization", *Journal of the Optical Society of America A*
  19(7), 2002. The reading of the iterative methods as projection algorithms.
- Joseph W. Goodman, *Introduction to Fourier Optics*, 3rd ed. (Roberts, 2005). Propagation, the angular
  spectrum and holography.
- Carmelo Giacovazzo, *Direct Phasing in Crystallography: Fundamentals and Applications* (Oxford University
  Press, 1998). The crystallographic phase problem and the direct methods in depth.
