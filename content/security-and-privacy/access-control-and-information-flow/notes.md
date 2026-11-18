## History

The question of what a program may do with the data it reads was put by Butler Lampson in 1973, in *A note on the confinement problem*: how to make sure that a borrowed program cannot pass its caller's data to its owner, through files it writes or through its effect on resources that others share. Access control alone cannot answer it, because the program is allowed to read the data.

Dorothy Denning gave the first general model in 1976, in *A lattice model of secure information flow*. Security classes form a lattice, information may flow only upward in it, and a program has two kinds of flow: explicit flows through assignments and implicit flows through the control flow. With Peter Denning she then showed in 1977 how a compiler can certify a program against such a policy. Joseph Goguen and José Meseguer stated noninterference in 1982, in *Security policies and security models*, as a property of a system shared by groups of users: the actions of one group must have no effect on what another group can see.

Dennis Volpano, Cynthia Irvine and Geoffrey Smith joined the two lines in 1996. Their paper *A sound type system for secure flow analysis* writes Denning's certification as a type system for a small while language and proves that every typable program is noninterfering. Andrei Sabelfeld and Andrew Myers surveyed the field in 2003 in *Language-based information-flow security*, which set out the semantic definition, the termination and timing channels, and the problem of declassification.

The view of noninterference as a property of pairs of runs came later. Gilles Barthe, Pedro D'Argenio and Tamara Rezk reduced it to the verification of one program by self-composition in 2004. Tachio Terauchi and Alex Aiken named 2-safety in 2005 and showed that noninterference is a 2-safety property but not a safety property. Michael Clarkson and Fred Schneider generalized this in *Hyperproperties* (2010), where security policies are sets of sets of traces.

## Further reading

- Andrei Sabelfeld and Andrew C. Myers, *Language-based information-flow security*, IEEE Journal on Selected Areas in Communications, 2003. The survey to read first: definitions, type systems, channels and open problems as they stood.
- Dennis Volpano, Cynthia Irvine and Geoffrey Smith, *A sound type system for secure flow analysis*, Journal of Computer Security, 1996. A short paper with the type rules and the soundness proof.
- Dorothy E. Denning, *A lattice model of secure information flow*, Communications of the ACM, 1976. The lattice of levels and the two kinds of flow.
- Michael R. Clarkson and Fred B. Schneider, *Hyperproperties*, Journal of Computer Security, 2010. Why noninterference is not a trace property, and the theory of properties of sets of traces.
- Joseph A. Goguen and José Meseguer, *Security policies and security models*, IEEE Symposium on Security and Privacy, 1982. The original definition of noninterference for systems.
