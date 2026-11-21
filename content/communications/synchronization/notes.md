## History

The phase-locked loop is older than digital communication. Henri de Bellescize described synchronous
reception with a locally locked oscillator in 1932. Eugene Jaffe and Richard Rechtin gave the optimum loop
filters for tracking a signal in noise in 1955, and John Costas, at General Electric, proposed the loop for
suppressed-carrier signals that carries his name in 1956. Andrew Viterbi solved the nonlinear first-order
loop with Fokker-Planck methods in 1963, which gave the distribution of the phase error and the mean time
between cycle slips. Floyd Gardner's *Phaselock Techniques* (1966) and the book of William Lindsey and Marvin
Simon (1973) made the loop a standard design.

Symbol timing and frames followed. Ronald Barker published his short sequences with low sidelobes in 1953, and
James Massey derived the optimum frame synchronizer for a sync word surrounded by random data in 1972. Kurt
Mueller and Markus Müller gave a timing detector that needs one sample per symbol in 1976, and Gardner gave
his two-sample detector for BPSK and QPSK in 1986. Martin Oerder and Heinrich Meyr estimated the timing in
feedforward form from the squared signal in 1988. In the same year C. W. Farrow proposed the filter structure
for a variable fractional delay, and in 1993 Gardner, with Lars Erup and Robert Harris, set out the theory of
interpolation in digital modems.

Frequency estimation came from spectral analysis. David Rife and Robert Boorstyn showed in 1974 that the
maximum-likelihood estimate of a tone's frequency is the peak of the periodogram, and gave its Cramér-Rao
bound. Steven Tretter proposed estimating the frequency from the unwrapped phase in 1985, and Steven Kay in
1989 replaced it with a weighted sum of phase differences that reaches the bound at high SNR. Andrew and
Audrey Viterbi gave the $M$th-power feedforward phase estimator for $M$-PSK in 1983.

The bounds and the burst estimators came together in the 1990s. Aldo D'Andrea, Umberto Mengali and Ruggero
Reggiannini introduced the modified Cramér-Rao bound in 1994, which handles the unknown data simply. Marco
Luise and Reggiannini gave their autocorrelation frequency estimator for bursts in 1995, and Paul Moose (1994)
and Timothy Schmidl and Donald Cox (1997) gave estimators for OFDM built on repeated training. Fulvio Gini,
Reggiannini and Mengali extended the modified bound to several parameters in 1998, and Marc Moeneclaey
compared it with the true bound in the same year.

## Further reading

- Umberto Mengali and Aldo N. D'Andrea, *Synchronization Techniques for Digital Receivers* (Plenum Press,
  1997). The reference for carrier, frequency and timing estimators and their bounds.
- Heinrich Meyr, Marc Moeneclaey and Stefan A. Fechtel, *Digital Communication Receivers* (Wiley, 1998).
  Synchronization and channel estimation derived from maximum likelihood, with full analyses of the loops.
- Floyd M. Gardner, *Phaselock Techniques* (third edition, Wiley, 2005). The practical account of
  phase-locked loops: design, acquisition, noise and cycle slips.
- Steven M. Kay, *Fundamentals of Statistical Signal Processing, Volume I: Estimation Theory* (Prentice Hall,
  1993). The Cramér-Rao bound and the estimators of frequency and phase as worked problems.
- Floyd M. Gardner, "Interpolation in digital modems, Part I: Fundamentals", *IEEE Transactions on
  Communications* 41(3) (1993). Why and how a receiver with a free-running clock interpolates to the symbol
  instants.
