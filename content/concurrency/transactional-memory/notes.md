## History

Maurice Herlihy and Eliot Moss proposed transactional memory at ISCA in 1993, as a small set of new instructions and a transactional cache that would make lock-free data structures easy to write. Nir Shavit and Dan Touitou answered at PODC in 1995 with a software version built from load-linked and store-conditional; it was lock-free but handled only static transactions, whose data set is known in advance. The journal version appeared in *Distributed Computing* in 1997.

Dynamic transactions came in 2003. Herlihy, Luchangco, Moir and Scherer gave DSTM, an obstruction-free STM in which a transaction opens objects as it goes, and Harris and Fraser gave language support for lightweight transactions in the same year. DSTM moved progress into a separate contention manager, and Scherer and Scott compared Polite, Karma, Polka and many others in 2004 and 2005. Guerraoui, Herlihy and Pochon gave Greedy at PODC 2005, the first manager with a proved bound. In the same year Harris, Marlow, Peyton Jones and Herlihy added retry and orElse to the STM of the Glasgow Haskell Compiler.

The designs used today dropped non-blocking progress for speed. Dice, Shalev and Shavit gave TL2 at DISC 2006, with a global version clock and locks taken at commit; Riegel, Felber and Fetzer gave the lazy snapshot algorithm at the same conference, and it became the core of TinySTM in 2008. SwissTM followed at PLDI 2009, and Dalessandro, Spear and Scott removed per-word metadata altogether with NOrec at PPoPP 2010. The theory caught up at the same time: Guerraoui and Kapałka defined opacity at PPoPP 2008, Spear and colleagues named the privatization problems in 2007, and Attiya, Hillel and Milani proved the disjoint-access-parallel lower bound at SPAA 2009. The STAMP suite of Cao Minh and colleagues, from 2008, gave the field a common benchmark.

Hardware took longer. Research designs such as TCC (2004) and LogTM (2006) explored unbounded transactions, and Sun's Rock processor, which had them, never shipped. The first commercial HTMs were best effort: IBM Blue Gene/Q and zEC12 in 2012, Intel TSX in the Haswell processors of 2013, and IBM POWER8 in 2014. Its HLE interface brought the speculative lock elision of Rajwar and Goodman (2001) to a commercial processor. Errata, and in 2019 the TSX Asynchronous Abort attack, led Intel to remove HLE and to turn RTM off by microcode on many processors.

## Further reading

- Tim Harris, James Larus and Ravi Rajwar, *Transactional Memory*, second edition, Morgan and Claypool, 2010. The standard survey of software and hardware designs, with the semantics questions in one place.
- Rachid Guerraoui and Michał Kapałka, *Principles of Transactional Memory*, Synthesis Lectures on Distributed Computing Theory, 2010. Opacity, progress and the lower bounds, stated and proved with care.
- Maurice Herlihy and J. Eliot B. Moss, *Transactional Memory: Architectural Support for Lock-Free Data Structures*, ISCA 1993. The paper that started the field, still clear on what the cache must do.
- Dave Dice, Ori Shalev and Nir Shavit, *Transactional Locking II*, DISC 2006. A short paper whose clock-and-lock design most later STMs copy.
- Luke Dalessandro, Michael F. Spear and Michael L. Scott, *NOrec: Streamlining STM by Abolishing Ownership Records*, PPoPP 2010. Shows how far a single sequence lock and value-based validation go.
- Tim Harris, Simon Marlow, Simon Peyton Jones and Maurice Herlihy, *Composable Memory Transactions*, PPoPP 2005. Retry and orElse, and the case that transactions compose where locks do not.
