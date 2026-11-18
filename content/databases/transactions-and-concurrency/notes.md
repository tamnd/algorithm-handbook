## History

The theory of transactions began at IBM during the work on System R. In 1976 Kapali Eswaran, Jim Gray, Raymond Lorie and Irving Traiger published *The Notions of Consistency and Predicate Locks in a Database System*. It defined transactions and serializable schedules, proved that two-phase locking gives serializability, and described the phantom problem with predicate locks as the cure. In the same year Gray, Lorie, Gianfranco Putzolu and Traiger defined degrees of consistency, the ancestors of the SQL isolation levels.

Other schedulers soon followed. Daniel Rosenkrantz, Richard Stearns and Philip Lewis gave wait-die and wound-wait in 1978 for distributed systems. David Reed proposed multiversion timestamps in his 1978 thesis, and Robert Thomas gave his write rule in 1979 in a paper on replicated databases. Christos Papadimitriou set out the theory of serializability in 1979, with the NP-completeness of view serializability. H. T. Kung and John Robinson described optimistic concurrency control in 1981, and Philip Bernstein and Nathan Goodman gave the theory of multiversion concurrency control in 1983. Bernstein, Vassos Hadzilacos and Goodman collected the whole field in their book of 1987.

Weak isolation came back as a research subject in the 1990s. Hal Berenson and his colleagues showed in 1995 that the anomalies of the SQL standard are ambiguous, and defined snapshot isolation, which Oracle and others already used. Atul Adya gave definitions that do not depend on any implementation in his 1999 thesis. Alan Fekete, Elizabeth O'Neil and Patrick O'Neil found in 2004 that even a read-only transaction can see an anomaly under snapshot isolation, and in 2005 Fekete and others proved that every non-serializable snapshot isolation history has two consecutive read-write dependencies between concurrent transactions.

That theorem led to serializable snapshot isolation, by Michael Cahill, Uwe Röhm and Fekete in 2008. PostgreSQL adopted it in version 9.1 in 2011, as Dan Ports and Kevin Grittner described in 2012, so that its serializable level is truly serializable.

## Further reading

- Philip A. Bernstein, Vassos Hadzilacos and Nathan Goodman, *Concurrency Control and Recovery in Database Systems*, Addison-Wesley, 1987. The standard theory, with proofs; free online from the authors.
- Gerhard Weikum and Gottfried Vossen, *Transactional Information Systems: Theory, Algorithms, and the Practice of Concurrency Control and Recovery*, Morgan Kaufmann, 2001. A longer and more recent treatment.
- Jim Gray and Andreas Reuter, *Transaction Processing: Concepts and Techniques*, Morgan Kaufmann, 1993. How real systems implement locks and transactions.
- Hal Berenson, Philip Bernstein, Jim Gray, Jim Melton, Elizabeth O'Neil and Patrick O'Neil, *A Critique of ANSI SQL Isolation Levels*, SIGMOD 1995. The anomalies and snapshot isolation.
- Michael J. Cahill, Uwe Röhm and Alan D. Fekete, *Serializable Isolation for Snapshot Databases*, SIGMOD 2008. The SSI algorithm.
