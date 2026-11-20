## History

Numerical weather prediction needed an initial state on a grid, and the first answer was statistical.
Gandin's *Objective Analysis of Meteorological Fields* (1963) set out optimal interpolation, the best linear
estimate from nearby observations with modelled error covariances, and Lorenc's global multivariate
scheme of 1981 became the operational analysis at ECMWF. Sasaki had proposed in the late 1950s to find the
analysis by minimizing a cost under dynamical constraints, and gave a general variational formalism in 1970. Hoke and Anthes (1976)
used nudging, a relaxation of the model towards the observed fields, to initialize forecasts.

The variational line grew through the 1980s. Lewis and Derber (1985), Le Dimet and Talagrand (1986) and
Talagrand and Courtier (1987) used the adjoint model to compute the gradient of a cost over a time window,
which is 4D-Var. Lorenc (1986) showed that the optimal interpolation analysis minimizes a cost derived from Bayes'
theorem, and the spectral statistical interpolation of Parrish and Derber (1992), a 3D-Var, replaced optimal
interpolation at the US National Meteorological Center, with the background covariance estimated from forecast differences. Courtier,
Thépaut and Hollingsworth (1994) proposed the incremental form, and ECMWF made 4D-Var operational on 25
November 1997 (Rabier and coworkers, 2000). In oceanography, Bennett and McIntosh (1982) solved a tidal
inverse problem with representers, and Bennett's books of 1992 and 2002 made weak constraints and the
representer method standard tools there.

Evensen (1994) proposed the ensemble Kalman filter for a nonlinear ocean model. Burgers, van Leeuwen and
Evensen (1998) and Houtekamer and Mitchell (1998) showed that the observations must be perturbed, and
Houtekamer and Mitchell (2001) added localization with the compactly supported correlation function of
Gaspari and Cohn (1999). Deterministic square root forms followed: the EAKF of Anderson (2001), the ETKF of
Bishop, Etherton and Majumdar (2001) and the serial filter of Whitaker and Hamill (2002), unified by Tippett
and coworkers (2003). Ott and coworkers (2004) gave a local ensemble Kalman filter, and Hunt, Kostelich
and Szunyogh (2007) its transform form, the LETKF. Lorenz (1996) and Lorenz and Emanuel (1998) supplied the small chaotic
model on which most of these filters were tested.

Hamill and Snyder (2000) proposed mixing the ensemble covariance into 3D-Var, Lorenc (2003) gave the alpha
control variable, and Wang, Snyder and Hamill (2007) proved the two forms equivalent; Liu, Xiao and Wang
(2008) and Buehner and coworkers (2010) carried the idea over a time window. Desroziers, Berre, Chapnik and
Poli (2005) gave the diagnostics of error statistics from innovations and residuals. Snyder, Bengtsson,
Bickel and Anderson (2008) showed why global particle filters fail in weather models, which led to the
local particle filters of Penny and Miyoshi (2016) and Poterjoy (2016). Iglesias, Law and Stuart (2013)
turned the ensemble update into a general method for inverse problems.

## Further reading

- Eugenia Kalnay, *Atmospheric Modeling, Data Assimilation and Predictability* (Cambridge University Press,
  2003). The standard introduction from the side of weather prediction: models, optimal interpolation,
  3D-Var and 4D-Var, and the start of ensemble methods.
- Geir Evensen, *Data Assimilation: The Ensemble Kalman Filter* (second edition, Springer, 2009). The
  ensemble Kalman filter and smoother, with their square root forms and many worked examples.
- Mark Asch, Marc Bocquet and Maëlle Nodet, *Data Assimilation: Methods, Algorithms, and Applications*
  (SIAM, 2016). A modern account of variational and ensemble methods side by side, with attention to
  algorithms.
- Kody Law, Andrew Stuart and Konstantinos Zygalakis, *Data Assimilation: A Mathematical Introduction*
  (Springer, 2015). The mathematical view: filtering and smoothing as Bayesian problems, with proofs.
- Andrew F. Bennett, *Inverse Modeling of the Ocean and Atmosphere* (Cambridge University Press, 2002).
  Weak constraints, representers and their iterative solution.
- R. N. Bannister, "A review of operational methods of variational and ensemble-variational data
  assimilation", *Quarterly Journal of the Royal Meteorological Society* 143 (2017). How the methods of this
  chapter are combined in the systems of weather centres.
