## History

The limits came first. In 1928 Harry Nyquist showed that a band of $W$ hertz carries at most $2W$ independent
pulses per second and gave the condition on the channel shaping under which the pulses do not interfere at
the sampling instants. Ralph Hartley, in the same year, measured information by the logarithm of the number of
distinguishable messages. Claude Shannon added noise as a random process: in 1948 he gave the capacity of the
band-limited Gaussian channel, and in 1949 the geometric proof, in which signals are points in a space of
$2TW$ dimensions and the noise turns each into a small sphere. Vladimir Kotelnikov's theory of optimum noise
immunity, translated into English in 1959, and the textbook of John Wozencraft and Irwin Jacobs (1965) made
that signal space the standard frame for detection.

The detectors and error rates of the basic constellations were worked out in the 1950s and 1960s, as data
moved onto telephone lines and radio links. Frank Gray's patent on pulse code communication, filed in 1947 and
issued in 1953, gave the reflected binary code that now labels most constellations. Adam Lender introduced
duobinary signaling in 1963, and Peter Kabal and Subbarayan Pasupathy classified partial-response systems in
1975. James Mazo showed in 1975 that binary sinc pulses can be sent faster than the Nyquist rate without
losing minimum distance, down to a spacing of about $0.802T$. John Craig's 1991 form of the Q-function made
exact error rates of two-dimensional constellations finite integrals.

Constant-envelope schemes followed the needs of satellite and mobile radio. Kazuaki Murota and Kenkichi Hirade
proposed GMSK for digital mobile telephony in 1981, and it became the modulation of GSM. Pierre Laurent
showed in 1986 that binary continuous-phase signals are sums of amplitude-modulated pulses, which let
receivers for CPM use linear methods. The book of John Anderson, Tor Aulin and Carl-Erik Sundberg (1986)
collected the theory of continuous-phase modulation.

Coded modulation joined codes and constellations. Hideki Imai and Shuji Hirakawa proposed multilevel coding in
1977, and Gottfried Ungerboeck published trellis-coded modulation with set partitioning in 1982; Lee-Fang
Wei's 8-state code with a 32-point cross constellation went into the V.32 modem. Ephraim Zehavi introduced bit
interleaving for coded 8-PSK in 1992, and Giuseppe Caire, Giorgio Taricco and Ezio Biglieri gave the theory of
bit-interleaved coded modulation in 1998, the year before Udo Wachsmann, Robert Fischer and Johannes Huber
published design rules for multilevel codes. Frank Kschischang and Pasupathy studied optimal nonuniform
signaling in 1993, and Georg Böcherer, Fabian Steiner and Patrick Schulte made probabilistic shaping practical
with a binary code in 2015; Schulte and Böcherer gave constant composition distribution matching in 2016.

## Further reading

- John G. Proakis and Masoud Salehi, *Digital Communications* (fifth edition, McGraw-Hill, 2008). The
  standard reference for constellations, error rates, pulses and coded modulation.
- Robert G. Gallager, *Principles of Digital Communication* (Cambridge University Press, 2008). A careful
  treatment of signal space, Nyquist pulses and detection, with proofs.
- John M. Wozencraft and Irwin M. Jacobs, *Principles of Communication Engineering* (Wiley, 1965). The book
  that set out detection in signal space, still clear on the geometry.
- John B. Anderson, Tor Aulin and Carl-Erik Sundberg, *Digital Phase Modulation* (Plenum Press, 1986).
  Continuous-phase modulation, its distances and its receivers.
- Giuseppe Caire, Giorgio Taricco and Ezio Biglieri, "Bit-interleaved coded modulation", *IEEE Transactions
  on Information Theory* 44(3) (1998). The capacity and the design rules of BICM with Gray labels.
