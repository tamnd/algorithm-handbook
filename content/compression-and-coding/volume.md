Compression and coding are about the bits that represent data: how few of them a file needs, and how many extra ones a link needs so that the data survives errors. A PNG image is stored with DEFLATE, which replaces repeated strings by references to earlier text and then writes the result with Huffman codes. A JPEG photo is cut into blocks of 8 by 8 pixels, and each block keeps its cosine coefficients only as precisely as the eye can tell. A QR code still scans when part of it is torn off, because Reed-Solomon codes carry enough extra symbols to rebuild the lost ones. A 5G phone decodes its data with LDPC codes. Every Ethernet frame and every gzip file carries a CRC, and the last digit of a payment card number is a check digit.

This volume is about those algorithms and the limits they work against. It starts with entropy coding, the step that turns a model of the data into bits, and goes on to dictionary methods, transforms for images, sound and text, codes that correct errors, and checksums that only detect them.

## Why compression and coding get a volume of their own

Most volumes measure an algorithm by its time and space. Here a third cost comes first: the number of bits written. A few ideas recur in every chapter:

- **Information has a measure.** [Shannon entropy](/shannon-entropy/) gives the least mean number of bits per symbol for a source, and the [channel capacity](/channel-capacity/) gives the most bits per channel use that a noisy link can carry. Both are limits that no algorithm can beat, and both can be reached as closely as you like with long enough blocks.
- **Every bound names its model.** A compression bound says what it assumes about the data: a memoryless source, a Markov source, a stationary ergodic source, or no source at all, in which case the bound is a worst case stated with the empirical entropy of the input. A coding bound says whether it holds for all codes, for linear codes only, or only as the block length grows.
- **Counting sets the limits.** The [incompressibility argument](/incompressibility-argument/) shows by counting that no compressor shortens every input. The [Hamming bound](/hamming-bound/) counts disjoint balls around the words of a code. Many lower bounds in the volume are counts of this kind.
- **The model and the coder are separate.** A compressor predicts the next symbol and an entropy coder spends about $\log_2(1/p)$ bits on a symbol of probability $p$. [Arithmetic coding](/arithmetic-coding/) and [asymmetric numeral systems](/asymmetric-numeral-systems/) do the second part almost perfectly, so the quality of a compressor is the quality of its model.
- **Redundancy is removed, then added back.** Compression removes the redundancy that the data has by chance. Error correction adds redundancy of a chosen form, and a checksum adds a few bits that only detect a change.
- **Formats are standards.** DEFLATE, Zstandard, JPEG and CRC-32 are fixed by documents, and a decoder must follow them bit for bit. The entries name the standard and the section that fixes each detail.

## How this volume relates to the others

- **Volume 1, foundations**, has [discrete probability](/discrete-probability-distribution/), [expected value](/expected-value/) and the [law of large numbers](/law-of-large-numbers/), on which every bound of Chapters 24.1 and 24.4 rests.
- **Volume 2, techniques**, has [bit operations](/bitwise-operations/), [bit packing](/bit-packing/) and the [greedy method](/greedy-algorithm/) that builds a Huffman code.
- **Volume 3, data structures**, gives the [priority queue](/priority-queue/) of Huffman's algorithm and the [hash table](/hash-table/) of fast match finders.
- **Volume 8, strings**, has the [suffix array](/suffix-array/). The Burrows-Wheeler transform is read off it, and the Lempel-Ziv factorization takes linear time once it is built.
- **Volume 11, algebra**, has [polynomial long division](/polynomial-long-division/), on which the CRC rests, and the [fast Fourier transform](/fast-fourier-transform/), on which the fast cosine transforms rest.
- **Volume 17, randomized algorithms**, has the [Markov chain](/markov-chain/), the simplest source with memory.
- **Volume 23, cryptography**, has the [cryptographic hash function](/cryptographic-hash-function/). A checksum catches accidental errors; only a cryptographic hash resists an attacker who changes the data on purpose.

## The chapters

**Chapter 24.1, Entropy coding**, covers [self-information](/self-information/) and entropy, the [prefix code](/prefix-code/) and the [Kraft inequality](/kraft-inequality/), the [source coding theorem](/source-coding-theorem/), [Huffman coding](/huffman-coding/) and the optimal codes under extra constraints, codes for the integers from [Elias gamma](/elias-gamma-coding/) to [Golomb codes](/golomb-coding/), arithmetic coding and [range coding](/range-coding/), asymmetric numeral systems, and the adaptive and context models that feed the coders.

**Chapter 24.2, Dictionary compression**, covers [LZ77](/lz77/) and [LZ78](/lz78/) and their variants such as [LZW](/lzw/), how to find matches and how to parse the text into them, the formats [DEFLATE](/deflate/), [LZMA](/lzma/) and [Zstandard](/zstandard/), grammar compression with [Re-Pair](/re-pair/) and the [smallest grammar problem](/smallest-grammar-problem/), and the [Ziv-Lempel theorem](/ziv-lempel-entropy-theorem/): on a stationary ergodic source, LZ78 reaches the entropy rate with no model of the source.

**Chapter 24.3, Transforms for compression**, covers the transforms that make data easier to code. [Delta encoding](/delta-encoding/), [run-length encoding](/run-length-encoding/) and [predictive coding](/predictive-coding/) are lossless. The [Burrows-Wheeler transform](/burrows-wheeler-transform/) with [move-to-front](/move-to-front-transform/) is the base of bzip2. The chapter goes on to [lossy compression](/lossy-compression/), [scalar quantization](/scalar-quantization/), [transform coding](/transform-coding/) with the [discrete cosine transform](/discrete-cosine-transform/) and [JPEG](/jpeg-compression/), and subband coding and JPEG 2000.

**Chapter 24.4, Error correcting codes**, covers the [Hamming distance](/hamming-distance/), [linear codes](/linear-code/) and [syndrome decoding](/syndrome-decoding/), the [Hamming code](/hamming-code/), the channel models and the [noisy-channel coding theorem](/channel-coding-theorem/), the bounds on codes from Hamming and Singleton to [Gilbert-Varshamov](/gilbert-varshamov-bound/), [Reed-Solomon codes](/reed-solomon-code/) and their decoders, BCH and cyclic codes, convolutional and [turbo codes](/turbo-code/), [LDPC codes](/ldpc-code/) with belief propagation, [fountain codes](/fountain-codes/), and [polar codes](/polar-code/).

**Chapter 24.5, Checksums**, covers the [checksum](/checksum/) and the [parity bit](/parity-bit/), additive checksums, [Fletcher](/fletcher-checksum/) and [Adler-32](/adler-32/), the [Internet checksum](/internet-checksum/), the [cyclic redundancy check](/cyclic-redundancy-check/) with its [guarantees](/crc-error-detection-guarantees/) and its fast table and carry-less versions, check digits such as the [Luhn algorithm](/luhn-algorithm/), and [rolling checksums](/rolling-checksum/).

## How to read this volume

If this is your first course on compression and coding, read these entries in this order. From Chapter 24.1: Shannon entropy, the prefix code, the Kraft inequality, Huffman coding, the source coding theorem, Elias gamma coding and arithmetic coding. From Chapter 24.2: LZ77, LZ78 and DEFLATE. From Chapter 24.3: the Burrows-Wheeler transform, the discrete cosine transform and JPEG. From Chapter 24.4: linear codes, the Hamming code, channel capacity and Reed-Solomon codes. From Chapter 24.5: the parity bit and the cyclic redundancy check. Do the exercises marked ◦ and • at the end of these chapters. That is a complete first unit on the subject.

Chapter 24.1 comes first, since Chapters 24.2 and 24.3 end every method with one of its coders. Chapter 24.4 uses its entropy and its binary entropy function but can be read next to it. Chapter 24.5 can be read at any time; its CRCs are cyclic codes, which Chapter 24.4 treats in general. If you already know the basics, start with the opening page of each chapter. It names the groups in the chapter and the order to read them.

Each entry stands on its own. Its facts box lists what it needs, with the number of the entry where each prerequisite is explained. Entries in other volumes are cited by number too.

## What you need first

You should be able to read a short program and follow a proof by counting or by induction. From Volume 1 you need logarithms, discrete probability and expectation; the law of large numbers is used in the proofs of the coding theorems. You should be at ease with bits and bytes, shifts and masks. Chapter 24.3 uses linear algebra: matrices, orthogonal bases and eigenvectors. Chapters 24.4 and 24.5 use arithmetic modulo a prime and polynomials over the field of two elements; Chapter 24.5 explains the second from the start.

## The exercises

Each chapter ends with exercises in three bands. Exercises marked ◦ check that you read the entries closely; you should be able to do them in a few minutes. Exercises marked • ask you to use an idea in a new place; each takes some thought, and some need a short program. Exercises marked ★ are harder; some are results from research papers. Hints for many exercises are in the appendix *Hints to the exercises* at the end of the volume.
