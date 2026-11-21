## History

The mean power came first. Friis published his transmission formula for free space in 1946, and the
inverse-square law with an aperture term is still the start of every link budget. Mobile radio at VHF and
UHF showed that the real loss grows much faster with distance and varies from street to street. Okumura
and his colleagues measured field strength in and around Tokyo and published curves in 1968, and Hata
fitted formulas to those curves in 1980. Gudmundson's 1991 model of the correlation of shadow fading along
a route completed the picture of slow variations around the mean.

The statistics of fast fading go back to Rice's papers on the mathematical analysis of random noise in
1944 and 1945, which give the distribution of a sine wave plus Gaussian noise and the expected rate at
which a random process crosses a level. Nakagami proposed his m-distribution in 1960 as a fit to measured
fading of radio signals. Clarke's 1968 paper on a statistical theory of mobile-radio reception put
scatterers all around a moving vehicle and derived the Bessel correlation and the U-shaped Doppler
spectrum. The Bell Laboratories book *Microwave Mobile Communications*, edited by Jakes in 1974, collected
this theory, the fade statistics and Jakes' sum-of-sinusoids simulator. In 1975 Smith described a simulator
that shapes Gaussian noise in the frequency domain. The flaws of Jakes' simulator were
studied later: Dent, Bottomley and Croft changed it in 1993, Pop and Beaulieu showed in 2001 that it is not
wide-sense stationary, and Zheng and Xiao gave a randomized sum of sinusoids with proved statistics in 2003.

Diversity is as old as fading radio links. Kahn described a ratio-squared combiner in 1954, and Brennan's
1959 survey of linear diversity combining named maximal ratio combining and compared it with equal gain
and selection combining. For wideband channels Bello's 1963 paper on randomly time-variant linear channels
introduced the WSSUS assumptions and the system functions still used. Saleh and Valenzuela fitted their
cluster model to indoor measurements in an office building in 1987. Fleury proved in 1996 the uncertainty
relation that turns the rules of thumb between delay spread and coherence bandwidth into a bound.

The information theory of fading came with digital cellular systems. Ozarow, Shamai and Wyner's 1994 paper
on information-theoretic considerations for cellular mobile radio set the outage view for slowly fading
channels beside the ergodic one, and Goldsmith and Varaiya's 1997 paper on the capacity of fading
channels with channel side information treated water-filling in time with transmitter knowledge. On the
side of codes, Gilbert's 1960 two-state model of a burst-noise channel and Elliott's 1963 estimates of error
rates on it gave the Gilbert-Elliott channel, and Mushkin and Bar-David found its capacity in 1989.

## Further reading

- Theodore S. Rappaport, *Wireless Communications: Principles and Practice*, 2nd edition (2002). Path loss,
  shadowing, the empirical models and the measured delay and Doppler parameters, with many worked numbers.
- Andrea Goldsmith, *Wireless Communications* (2005). Fading distributions, capacity with and without
  transmitter knowledge, and diversity combining, at the level of this chapter.
- David Tse and Pramod Viswanath, *Fundamentals of Wireless Communication* (2005). The clearest account of
  ergodic and outage capacity and of diversity as a slope.
- Marvin K. Simon and Mohamed-Slim Alouini, *Digital Communication over Fading Channels*, 2nd edition
  (2005). Closed forms for error and outage probabilities of every combiner under many fading models.
- William C. Jakes (editor), *Microwave Mobile Communications* (1974). The classical source for the Clarke
  model, fade statistics and the sum-of-sinusoids simulator.
