## History

Spread spectrum began as a military technique for resisting jamming and interception, and its
correlation theory grew in the 1950s and 1960s. Price and Green described the Rake system for multipath
HF channels in 1958, and Spilker and Magill gave the delay-lock discriminator for tracking a code delay in
1961. Frank and Zadoff published polyphase codes with good periodic correlation in 1962, and Chu
generalized them in 1972. On the binary side, Gold built his families from pairs of m-sequences in 1967,
and Kasami's 1966 report on the weight distributions of cyclic codes contains the families now named after
him. Welch's bound of 1974 gave the yardstick against which all these families are measured, and Sarwate
and Pursley's survey of 1980 put the families and the bound side by side.

The information theory of shared channels came at the same time. Shannon posed the problem of channels
with several users in 1961. Ahlswede (1971) and Liao (1972) found the capacity region of the multiple
access channel, and Cover introduced superposition coding for the broadcast channel in 1972, with
Bergmans's converse for the Gaussian case in 1974. Successive decoding, which reaches the corner points,
was thus understood long before receivers could do it.

Multiuser detection made the theory into receivers. Verdú gave the optimum detector for asynchronous CDMA
in 1983 and 1986, a Viterbi search whose cost grows as $2^K$, and proved in 1989 that the synchronous
problem is NP-hard. In the same year Lupas and Verdú analysed the decorrelator and defined near-far
resistance. The MMSE detector (Xie, Short and Rushforth, 1990; Madhow and Honig, 1994), multistage
parallel cancellation (Varanasi and Aazhang, 1990) and successive cancellation (Patel and Holtzman, 1994)
followed. Meanwhile, the capacity analysis of Gilhousen and coauthors (1991) made the case for cellular
CDMA, and IS-95 relied on power control and rake receivers rather than joint detection; OVSF codes (Adachi, Sawahashi and Okawa, 1997)
gave WCDMA its variable spreading factors. Van Nee and Coenen's FFT acquisition of 1991 became the standard
in software GPS receivers.

The fourth generation moved to OFDMA, whose adaptive form goes back to Wong and coauthors (1999), and used
Zadoff-Chu sequences for random access preambles. Work on the fifth generation revived non-orthogonal
access: power domain NOMA (Saito and coauthors, 2013) and SCMA (Nikopour and Baligh, 2013). For massive
numbers of devices, contention resolution diversity slotted ALOHA (2007) and Liva's coded slotted ALOHA
(2011) turned collisions into erasure decoding, and Polyanskiy (2017) posed the unsourced random access
problem that now drives work on coded compressed sensing.

## Further reading

- Sergio Verdú, *Multiuser Detection* (Cambridge University Press, 1998). The reference for the
  synchronous and asynchronous models and for every detector in this chapter, with proofs.
- Andrew J. Viterbi, *CDMA: Principles of Spread Spectrum Communication* (Addison-Wesley, 1995). Spread
  spectrum and CDMA from the designer of IS-95, with acquisition, tracking and capacity.
- David Tse and Pramod Viswanath, *Fundamentals of Wireless Communication* (Cambridge University Press,
  2005). The capacity regions, successive cancellation and multiuser diversity, with the systems view.
- Dilip V. Sarwate and Michael B. Pursley, "Crosscorrelation properties of pseudorandom and related
  sequences", *Proceedings of the IEEE* 68 (1980). The survey of m-sequences, Gold and Kasami families
  and their bounds.
- Kai Borre and coauthors, *A Software-Defined GPS and Galileo Receiver* (Birkhäuser, 2007). Code
  generation, FFT acquisition and delay-locked loops in working code.
- Enrico Paolini, Gianluigi Liva and Marco Chiani, "Coded slotted ALOHA: a graph-based method for
  uncoordinated multiple access", *IEEE Transactions on Information Theory* 61 (2015). The density
  evolution analysis of coded random access.
