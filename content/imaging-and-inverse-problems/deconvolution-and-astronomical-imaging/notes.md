## History

The limits came first. Abbe (1873) explained microscope images by diffraction orders and found the smallest
resolvable period $\lambda/(2\,\mathrm{NA})$; Rayleigh (1879) gave his criterion for two points in a
spectroscope, and Sparrow (1916) the criterion of the vanishing dip. Van Cittert (1931) corrected spectral
lines for the slit width by adding back the residual again and again, the first deconvolution iteration, and
in 1934 found the correlation of light from an incoherent source, which Zernike (1938) put in its usual
form. Hopkins (1955) and the Fourier optics that followed turned these results into statements about the
optical transfer function.

Radio astronomy made the Van Cittert-Zernike theorem an instrument. Ryle and Hewish (1960) described
aperture synthesis, and Högbom (1974) built CLEAN to remove the sidelobes of the dirty beam. Clark (1980)
split CLEAN into minor and major cycles, Schwab (1984) made the major cycles subtract the model from the
visibilities, and Cornwell (2008) and Cornwell, Golap and Bhatnagar (2008) added multiscale components and
w-projection. A second line used entropy: Frieden (1972) restored images by maximum entropy, Gull and
Daniell (1978) applied it to radio maps with a $\chi^2$ constraint, and Skilling and Bryan (1984) gave the
general algorithm. For photon counts, Richardson (1972) and Lucy (1974) proposed the multiplicative
iteration that Shepp and Vardi (1982) derived as EM for Poisson data in emission tomography.

Optical astronomers attacked turbulence. Labeyrie (1970) showed that the average power spectrum of short
exposures keeps the object to the diffraction limit; Knox and Thompson (1974) recovered the phase from the
cross spectrum, and Weigelt (1977) from triple correlations, whose bispectral theory Lohmann, Weigelt and
Wirnitzer (1983) gave. Fried (1978) computed the chance of a lucky exposure, and Law, Mackay and Baldwin
(2006) made lucky imaging work in the visible. Fried and Hudgin (1977) published least squares wavefront
reconstructors, Southwell (1980) a third geometry, and Gonsalves (1982) phase diversity. Ayers and Dainty
(1988) carried the alternating scheme of phase retrieval over to blind deconvolution, and Miskin and MacKay
(2000), Fergus and coworkers (2006) and Levin and coworkers (2009) developed the variational approach and
explained why joint MAP fails. Irani and Peleg (1991) gave iterative back-projection for multi-frame
super-resolution, and Fruchter and Hook (2002) drizzle, made for the Hubble Deep Field.

Microscopy followed its own path. Agard and Sedat (1983) used nearest neighbour subtraction on focal
series, Gibson and Lanni (1991) modelled the depth-dependent PSF, and Dey and coworkers (2006) added total
variation to Richardson-Lucy. Heintzmann and Cremer (1999) and Gustafsson (2000) introduced structured
illumination. In 2006 Betzig and coworkers, Hess, Girirajan and Mason, and Rust, Bates and Zhuang published
PALM, FPALM and STORM. Thompson, Larson and Webb (2002) gave the precision formula, Ober, Ram and Ward
(2004) the information limit, and Mortensen and coworkers and Smith and coworkers (2010) maximum likelihood
fitting that reaches it. Dertinger and coworkers (2009) introduced SOFI.

The theory of sparse super-resolution is recent. De Castro and Gamboa (2012) recovered nonnegative spikes
by total variation minimization over measures, Candès and Fernandez-Granda (2014) proved exact recovery of
complex spikes separated by $2/f_c$, and Fernandez-Granda (2016) lowered the constant to $1.26$.

## Further reading

- A. Richard Thompson, James M. Moran and George W. Swenson Jr., *Interferometry and Synthesis in Radio
  Astronomy*, 3rd ed. (Springer, 2017). The standard text on visibilities, aperture synthesis and imaging.
- Jean-Luc Starck, Eric Pantin and Fionn Murtagh, "Deconvolution in astronomy: a review", *Publications of
  the Astronomical Society of the Pacific* 114, 2002. A survey of the astronomical deconvolution methods
  and their noise models.
- Mario Bertero, Patrizia Boccacci, Gabriele Desiderà and Giuseppe Vicidomini, "Image deblurring with
  Poisson data: from cells to galaxies", *Inverse Problems* 25, 2009. Richardson-Lucy, its regularized
  forms and stopping rules, with examples from microscopy and astronomy.
- Per Christian Hansen, James G. Nagy and Dianne P. O'Leary, *Deblurring Images: Matrices, Spectra, and
  Filtering* (SIAM, 2006). The linear algebra of deblurring, boundary conditions and spectral filters.
- Joseph W. Goodman, *Introduction to Fourier Optics*, 3rd ed. (Roberts, 2005). Transfer functions,
  coherence and the diffraction limit.
