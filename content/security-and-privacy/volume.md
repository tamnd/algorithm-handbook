A program that checks a password compares the guess with the stored value byte by byte and stops at the first difference. The answer is correct, but the time it takes tells an attacker how many leading bytes were right, and a few thousand measured attempts recover the password one byte at a time. A second program never prints its secret, yet copies one bit of it into a public variable inside a branch. Neither program has a bug in the usual sense. Both leak, and security is the study of such leaks and of the algorithms that prevent, detect or bound them.

This volume collects the algorithms of computer security and privacy: how information flows through programs, how memory errors are stopped and found, how secrets leak through time and caches, how networks and the web are attacked and defended, how intrusions and malware are detected, how data are released without exposing the people in them, and how learning systems are attacked. It has nine chapters. In this edition only two entries are written, [noninterference](/noninterference/) in Chapter 45.1 and the [timing attack](/timing-attack/) in Chapter 45.4. The other seven chapters have no written entries yet; their pages say what they will cover and point to written entries elsewhere in the handbook.

## Why security gets a volume of its own

A few ideas run through the whole subject:

- **An adversary, not a distribution.** Most of the handbook assumes inputs from a user or from a known distribution. Here the inputs are chosen by someone who knows the algorithm and wants it to fail, so every claim names its threat model: what the attacker sees, controls and can compute.
- **Properties of many runs.** Correctness is a property of each run. Noninterference compares two runs that differ only in secrets, and differential privacy compares the output distributions on two data sets that differ in one person. Such properties cannot be checked one trace at a time.
- **Proved for a model, measured in practice.** Type systems for information flow are sound but reject some secure programs. Constant-time code removes a timing channel only for the leakage model it was written against. Detectors and fuzzers are judged by measurements on the programs and traffic tried.
- **Undecidable in general.** Whether a program is noninterfering, or is a virus, cannot be decided by any algorithm, by [Rice's theorem](/rice-theorem/). Practical tools approximate: they accept a safe subset or search for counterexamples.

## The chapters

**Chapter 45.1, Access control and information flow**, has one written entry, [noninterference](/noninterference/): the definition that public outputs do not depend on secret inputs, its termination-insensitive and termination-sensitive forms, and the type systems and self-composition that check it. Access control matrices, role-based access control, lattice models of security and declassification are still to be written.

**Chapter 45.2, Memory safety defenses**, will cover bounds checking, temporal safety, control-flow integrity and randomization. Meanwhile read the allocators of Volume 26, such as the [free list](/free-list/), and [borrow checking](/borrow-checking/) in Volume 34.

**Chapter 45.3, Fuzzing and vulnerability discovery**, will cover mutation and generation fuzzers, their schedules and the use of symbolic execution. Meanwhile read [coverage-guided fuzzing](/coverage-guided-fuzzing/) and [concolic testing](/concolic-testing/) in Volume 34.

**Chapter 45.4, Side channels**, has one written entry, the [timing attack](/timing-attack/): how the running time of square-and-multiply and of Montgomery reduction reveals an RSA key, how attacks are run statistically over many measurements, and how constant-time code and blinding remove the leak for a stated model. Cache, power, electromagnetic and fault attacks are still to be written.

**Chapter 45.5, Network and web security**, will cover web attacks such as cross-site scripting and SQL injection, SYN flooding, DNS poisoning and route hijacking, IP traceback, password models and Sybil attacks. Meanwhile read the [Border Gateway Protocol](/bgp/) and [packet classification](/packet-classification/) in Volume 26 and [password hashing](/password-hashing/) in Volume 23.

**Chapter 45.6, Intrusion and malware detection**, will cover misuse and anomaly detection, the base-rate problem, outlier detectors, scan and worm detection, disassembly and malware similarity, obfuscation and attack graphs. Meanwhile read [precision and recall](/precision-and-recall/) in Volume 25 and the [sequential probability ratio test](/sequential-probability-ratio-test/) in Volume 33.

**Chapter 45.7, Anonymization and disclosure control**, will cover re-identification, k-anonymity and its successors, statistical disclosure control and private record linkage. Meanwhile read [k-means](/k-means/) in Volume 25, which microaggregation resembles, and the [Bloom filter](/bloom-filter/) in Volume 3.

**Chapter 45.8, Differential privacy**, will cover the definition, the Laplace, Gaussian and exponential mechanisms, composition and privacy accounting, query release, private learning, local privacy and lower bounds. Meanwhile read the [Chernoff bound](/chernoff-bound/) in Volume 1 and the [multiplicative weights update](/multiplicative-weights-update/) method in Volume 19.

**Chapter 45.9, Adversarial machine learning**, will cover evasion attacks, poisoning and backdoors, membership inference and model extraction, certified defenses and attacks on language models. Meanwhile read [adversarial training](/adversarial-training/) in Volume 25 and [projected gradient descent](/projected-gradient-descent/) in Volume 15.

## How to read this volume

The two written entries can be read in either order. Read [noninterference](/noninterference/) for the formal side of the subject, a property defined over pairs of runs and checked by a type system or by an analysis. Read the [timing attack](/timing-attack/) for the measured side, where an attack is a statistical experiment and a defense holds only for the leakage it models. Each entry stands on its own; its facts box lists what it needs, by entry number.

The opening pages of Chapters 45.2 to 45.9 work as reading lists for now. Each names the topics the chapter will hold and links the written entries elsewhere in the handbook that already treat the underlying algorithms.

## What you need first

For noninterference you need the [Hoare triple](/hoare-triple/) of Volume 1 and the [safety property](/safety-property/) of Volume 16, and it helps to have seen [taint analysis](/taint-analysis/) in Volume 34. For the timing attack you need [modular exponentiation](/modular-exponentiation/) and [Montgomery multiplication](/montgomery-multiplication/) from Volume 10 and the [RSA cryptosystem](/rsa-cryptosystem/) from Volume 23, with basic probability: means, variances and the [Chernoff bound](/chernoff-bound/) of Volume 1.

## The exercises

Chapters 45.1 and 45.4 end with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
