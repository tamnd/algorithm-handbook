## History

Paul Kocher opened the subject in 1996 with *Timing attacks on implementations of Diffie-Hellman, RSA, DSS, and other systems*, at CRYPTO. He showed that the running time of a modular exponentiation, measured over many inputs, gives the private exponent bit by bit through a statistical test, and he named the countermeasures that are still used: constant work and blinding. Three years later Kocher, Joshua Jaffe and Benjamin Jun published *Differential power analysis*, which applied the same statistics to the power drawn by a smart card, and power analysis became a field of its own.

For some years timing attacks were thought to need a measurement close to the device. David Brumley and Dan Boneh ended that belief in 2003 with *Remote timing attacks are practical*. They used the extra reduction of Montgomery multiplication and the switch between schoolbook and Karatsuba multiplication in OpenSSL, and recovered a factor of a 1024-bit RSA key from another machine on the same network. OpenSSL answered with an advisory in March 2003 that turned blinding on by default.

The cache became the next channel. In 2005 Daniel Bernstein showed in *Cache-timing attacks on AES* that the table lookups of a standard AES implementation leak the key through the time they take, and Colin Percival read the exponent windows of OpenSSL RSA through the cache shared by two threads of one core. Dag Arne Osvik, Adi Shamir and Eran Tromer set out the Evict+Time and Prime+Probe methods in 2006, and Yuval Yarom and Katrina Falkner's Flush+Reload of 2014 used the shared last-level cache to read a GnuPG key with little noise.

Protocol code leaks too. Nadhem AlFardan and Kenneth Paterson's Lucky Thirteen attack of 2013 rebuilt a padding oracle in TLS from a difference of a few hash compression calls. The Minerva and TPM-Fail work of 2019 and 2020 timed ECDSA signing, saw the bit length of the nonces, and recovered keys with lattice methods. Each attack broke an implementation of a sound algorithm, and each pushed the libraries further toward code whose branches and addresses do not depend on secrets.

## Further reading

- Paul C. Kocher, *Timing attacks on implementations of Diffie-Hellman, RSA, DSS, and other systems*, CRYPTO 1996. The original attack and its countermeasures, in a few pages.
- David Brumley and Dan Boneh, *Remote timing attacks are practical*, USENIX Security Symposium 2003. How a leak of a few reductions survives a network, with the details of OpenSSL.
- Daniel J. Bernstein, *Cache-timing attacks on AES*, 2005. Why a table lookup at a secret index is not constant time.
- Dag Arne Osvik, Adi Shamir and Eran Tromer, *Cache attacks and countermeasures: the case of AES*, CT-RSA 2006. The standard methods for measuring cache use from another process.
- Stefan Mangard, Elisabeth Oswald and Thomas Popp, *Power Analysis Attacks: Revealing the Secrets of Smart Cards*, Springer, 2007. A textbook on the statistics of side channels, written for power but useful for time as well.
