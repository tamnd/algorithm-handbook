## History

Equalization grew up with data transmission over telephone lines. Lucky built the first automatic equalizers for
telephone-line modems at Bell Labs; his 1965 paper defined the peak distortion and showed that the
zero-forcing equalizer minimizes it when the eye is open. Gersho (1969) used the mean squared error
instead, the criterion of the MMSE designs and of the LMS equalizer. Austin described the decision feedback equalizer in a 1967 report, and Salz (1973) derived the
error of the infinite-length MMSE-DFE. Tomlinson (1971) and Harashima and Miyakawa (1972) moved the feedback
to the transmitter with modulo arithmetic. Gitlin and Weinstein (1981) analyzed the fractionally spaced
equalizer, which Ungerboeck had studied in 1976, and Qureshi's 1985 survey collected the adaptive theory.

Sequence detection began with Forney (1972), who showed that the matched filter outputs are sufficient
statistics, whitened their noise with the minimum-phase spectral factor and ran the Viterbi algorithm on the
result. Ungerboeck (1974) showed that the Viterbi algorithm can use the matched filter outputs directly.
Falconer and Magee (1973) shortened the channel in front of the detector. Eyuboglu and Qureshi (1988)
reduced the trellis with set partitions and per-survivor decision feedback, and Duel-Hallen and Heegard
(1989) published delayed decision-feedback sequence estimation. Raheli, Polydoros and Tzou (1995) stated
per-survivor processing as a general principle for detection with unknown parameters.

Blind equalization started with Sato (1975) for multilevel amplitude modulation. Godard (1980) and,
independently, Treichler and Agee (1983) introduced the constant modulus cost. Ding, Kennedy, Anderson and
Johnson (1991) showed that finite-length Godard equalizers can converge to wrong minima. A different route
used second-order statistics of an oversampled signal: Tong, Xu and Kailath (1991, journal version 1994)
showed that they identify the channel when the subchannels share no zero, and Moulines, Duhamel, Cardoso
and Mayrargue (1995) gave the subspace method.

The 1990s tied equalization to coding and to block transmission. Cioffi, Dudevoir, Eyuboglu and Forney
(1995) proved that the unbiased MMSE-DFE is canonical. Douillard and coauthors (1995) proposed turbo
equalization, and Tüchler, Koetter and Singer (2002) made it cheap with the MMSE equalizer with priors. Sari,
Karam and Jeanclaude (1995) proposed single-carrier transmission with frequency-domain equalization, which
Falconer and coauthors (2002) advocated for broadband wireless. Melsa, Younce and Rohrs (1996) and
Al-Dhahir and Cioffi (1996) designed channel-shortening equalizers for DSL. On the estimation side, Cavers
(1991) analyzed pilot-symbol-assisted modulation on Rayleigh fading channels, and the Kalman filter and
sparse recovery later gave the trackers and the sparse estimators of the chapter.

## Further reading

- John G. Proakis and Masoud Salehi, *Digital Communications*, fifth edition, McGraw-Hill, 2008. The
  standard reference for the equalizers, MLSE and adaptive algorithms, with the channels A, B and C used
  throughout the chapter.
- John R. Barry, Edward A. Lee and David G. Messerschmitt, *Digital Communication*, third edition, Kluwer
  Academic Publishers, 2004. A careful treatment of the linear and decision feedback equalizers, the
  whitened matched filter and precoding, with the infinite-length formulas.
- Shahid U. H. Qureshi, "Adaptive equalization", *Proceedings of the IEEE* 73(9), 1985. The classic survey
  of adaptive and fractionally spaced equalizers and their convergence.
- C. Richard Johnson, Jr., Philip Schniter, Thomas J. Endres, James D. Behm, Donald R. Brown and Raul A.
  Casas, "Blind equalization using the constant modulus criterion: a review", *Proceedings of the IEEE*
  86(10), 1998. What is known and not known about CMA, including its minima.
- Ralf Koetter, Andrew C. Singer and Michael Tüchler, "Turbo equalization", *IEEE Signal Processing
  Magazine* 21(1), 2004. A tutorial on the iterative receivers of the last group.
