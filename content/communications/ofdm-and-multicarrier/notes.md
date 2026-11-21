## History

Multicarrier transmission with overlapping orthogonal subchannels goes back to Robert Chang, who in 1966 gave
the conditions under which band-limited signals on many carriers can be sent without interference between
the carriers or between symbols. Burton Saltzberg analysed the same scheme in 1967 and showed that staggering
the in-phase and quadrature parts by half a symbol, the offset QAM later used in filter bank multicarrier,
keeps the subchannels apart with shaped pulses. Weinstein and Ebert proposed in 1971 to build the modulator
and demodulator with the discrete Fourier transform, with a guard interval between blocks. Peled and Ruiz
filled the guard with a cyclic extension in 1980, which is the cyclic prefix of every OFDM system since.
Cimini's 1985 study of OFDM on mobile radio channels and Bingham's 1990 survey, "Multicarrier modulation for
data transmission: an idea whose time has come", carried the idea from theory toward products.

Wireline systems came first. Chow, Tu and Cioffi proposed discrete multitone with bit loading for high-rate
digital subscriber lines in 1991, and DMT became the modulation of ADSL. Wireless systems followed with
digital audio and video broadcasting, the 802.11a wireless LAN and, later, LTE and 5G NR, where SC-FDMA, a
DFT-spread OFDM studied by Myung, Lim and Goodman in 2006, serves the uplink.

Synchronization was the first receiver problem. Moose gave the maximum likelihood frequency offset estimate
from two repeated symbols in 1994, and Pollet, Van Bladel and Moeneclaey computed the degradation that an
offset and phase noise cause in 1995. Schmidl and Cox published their timing and frequency method in 1997,
and van de Beek, Sandell and Börjesson the blind estimator based on the cyclic prefix in the same year.
Channel estimation grew at the same time: van de Beek and coauthors studied estimation through the DFT in
1995, Hoeher, Kaiser and Robertson the two-dimensional Wiener interpolation of pilots in 1997, Edfors and
coauthors the low-rank estimator in 1998, and Coleri, Ergen, Puri and Bahai compared pilot arrangements in
2002.

The peak power problem gathered its own literature. Bäuml, Fischer and Huber introduced selected mapping in
1996 and Müller and Huber partial transmit sequences in 1997. Tellado's work on tone reservation, collected
in his 2000 book, and Krongold and Jones's active constellation extension of 2003 added methods that send no
side information. Armstrong studied repeated clipping and filtering in 2002, and Han and Lee surveyed the
field in 2005.

The search for waveforms beyond OFDM started from its spectrum. Farhang-Boroujeny's 2011 article "OFDM versus
filter bank multicarrier" set out the case for filter banks. Fettweis, Krondorf and Bittner proposed GFDM in
2009, Vakilian and coauthors UFMC in 2013, Hadani and coauthors OTFS in 2017, and Bemani, Ksairi and
Kountouris AFDM in 2023, the last two for channels with large Doppler spread.

## Further reading

- Andrea Goldsmith, *Wireless Communications* (Cambridge University Press, 2005). Chapter 12 covers
  multicarrier modulation and OFDM, with the prefix, the FFT implementation and the main impairments.
- David Tse and Pramod Viswanath, *Fundamentals of Wireless Communication* (Cambridge University Press,
  2005). Shows OFDM as the diagonalization of a circulant channel and places it among the other answers to
  frequency selectivity.
- John A. C. Bingham, "Multicarrier modulation for data transmission: an idea whose time has come", IEEE
  Communications Magazine 28(5), 1990. A short and clear account of the ideas, still a good first read.
- Jose Tellado, *Multicarrier Modulation with Low PAR: Applications to DSL and Wireless* (Kluwer, 2000). The
  source for tone reservation and tone injection, with the statistics of the peak.
- Seung Hee Han and Jae Hong Lee, "An overview of peak-to-average power ratio reduction techniques for
  multicarrier transmission", IEEE Wireless Communications 12(2), 2005. Compares the reduction methods of
  the chapter side by side.
- Behrouz Farhang-Boroujeny, "OFDM versus filter bank multicarrier", IEEE Signal Processing Magazine 28(3),
  2011. A tutorial on filter banks and on what they gain and lose against OFDM.
