## History

Antenna arrays at the receiver are old; Winters's optimum combining of 1984, which maximizes the SINR of an
array in the presence of interference, is the MMSE filter of one stream. The step to many antennas at both
ends came from Bell Labs in the mid-1990s. Telatar derived the capacity of the Gaussian MIMO channel, fixed
and with Rayleigh fading, in a technical memorandum of 1995, published in the European Transactions on
Telecommunications in 1999. Foschini described the layered space-time architecture in 1996, and Foschini
and Gans gave the outage view of quasi-static channels in 1998. The same year Raleigh and Cioffi used the
SVD of the channel to send parallel streams, and Wolniansky, Foschini, Golden and Valenzuela built V-BLAST,
whose receiver nulls with the rows of the pseudoinverse and cancels one stream at a time.

Space-time coding grew in parallel. Guey, Fitz, Bell and Kuo gave the rank condition for transmit diversity
in 1996. Tarokh, Seshadri and Calderbank stated the rank and determinant criteria in 1998 and built the
first space-time trellis codes with them. Alamouti published his two-antenna code the same year, and Tarokh,
Jafarkhani and Calderbank placed it in the theory of orthogonal designs in 1999. Liang and Xia proved in 2003
that rate one is impossible for more than two antennas. Zheng and Tse defined the diversity-multiplexing
tradeoff in 2003, which changed the goal of code design, and Belfiore, Rekaya and Viterbo found the golden
code with its nonvanishing determinant in 2005.

Detection research looked for near-ML performance at a bounded cost. Tan and Rasmussen applied semidefinite
relaxation in 2001; Wong, Tsui, Cheng and Mow proposed the K-best search in 2002; Yao and Wornell introduced
lattice reduction aided detection the same year; and Hochwald and ten Brink gave the list sphere decoder for
coded systems in 2003. Jaldén and Ottersten proved in 2005 that the expected cost of sphere decoding is
exponential at every fixed SNR. For large systems, Céspedes, Olmos, Sánchez-Fernández and Pérez-Cruz
proposed expectation propagation in 2014 and Jeon, Ghods, Maleki and Studer an AMP detector in 2015.

On the transmit side, Costa's "Writing on dirty paper" of 1983 waited twenty years for its main use.
Caire and Shamai studied the multiantenna broadcast channel in 2003, the duality between broadcast and
multiple access gave its sum capacity the same year, and Weingarten, Steinberg and Shamai proved in 2006 that
dirty paper coding reaches the whole capacity region. Linear and lattice precoders came alongside: Lo's
maximum ratio transmission in 1999, block diagonalization by Spencer, Swindlehurst and Haardt with Choi
and Murch in 2004, regularized zero forcing and vector perturbation by Peel, Hochwald and Swindlehurst in
2005, and the weighted MMSE algorithm of Shi, Razaviyayn, Luo and He in 2011. Marzetta's 2010 paper on
base stations with unlimited numbers of antennas started massive MIMO and identified pilot contamination;
cell-free massive MIMO (Ngo and coauthors, 2017), hybrid beamforming for millimeter wave (El Ayach and
coauthors, 2014) and intelligent reflecting surfaces (Wu and Zhang, 2019) followed.

## Further reading

- David Tse and Pramod Viswanath, *Fundamentals of Wireless Communication* (Cambridge University Press,
  2005). Chapters 7 to 10 cover MIMO capacity, the receivers, the diversity-multiplexing tradeoff and
  multiuser MIMO with one consistent set of models.
- Arogyaswami Paulraj, Rohit Nabar and Dhananjay Gore, *Introduction to Space-Time Wireless Communications*
  (Cambridge University Press, 2003). A first text on channel models, space-time codes and receivers.
- Hamid Jafarkhani, *Space-Time Coding: Theory and Practice* (Cambridge University Press, 2005). Orthogonal
  and quasi-orthogonal designs, trellis codes and the design criteria in depth.
- Robert W. Heath Jr. and Angel Lozano, *Foundations of MIMO Communication* (Cambridge University Press,
  2018). A recent and complete treatment, including precoding with feedback and hybrid arrays.
- Thomas L. Marzetta, Erik G. Larsson, Hong Yang and Hien Quoc Ngo, *Fundamentals of Massive MIMO*
  (Cambridge University Press, 2016). Channel hardening, favorable propagation, pilots and the capacity
  bounds of large arrays.
- Abbas El Gamal and Young-Han Kim, *Network Information Theory* (Cambridge University Press, 2011). The
  broadcast channel and dirty paper coding with full proofs.
