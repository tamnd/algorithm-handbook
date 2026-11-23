C and C++ let a program compute any address and write there. A loop that copies nine bytes into an eight-byte buffer writes one byte that belongs to something else, and nothing in the language stops it. If the buffer is on the stack, the bytes after it include the saved return address of the function. In 1988 the Morris worm spread partly through such an overflow in the `fingerd` service, which read a request with `gets`, a function with no length bound. The same bug, a write past the end of a buffer, is still near the top of the lists of serious weaknesses.

The chapter is about the defenses against this class of bug and about the attacks that each defense left open. They differ in what they promise. A checker such as [AddressSanitizer](/addresssanitizer/) or [SoftBound](/softbound/) *detects* an unsafe access when it happens and stops the run. A policy such as [data execution prevention](/data-execution-prevention/), [control-flow integrity](/control-flow-integrity/) or [software fault isolation](/software-fault-isolation/) *prevents* one kind of effect, such as running written bytes or jumping to a target outside a static graph, and lets the memory error itself happen. A secret such as a [stack canary](/stack-canary/) or the random offsets of [address space layout randomization](/address-space-layout-randomization/) only *mitigates*: it makes an attack fail with high probability, and an information leak or a forking server that keeps the secret removes the protection. Keep the three words apart when you read the entries. The history of the field is a sequence of mitigations followed by attacks that go around them, from injected code to [return-oriented programming](/return-oriented-programming/) to attacks that use only data.

## What the chapter covers

1. **Memory errors.** [Memory safety](/memory-safety/) is defined by a spatial and a temporal condition on every access. A [buffer overflow](/buffer-overflow/) breaks the first, and [stack smashing](/stack-smashing/) is the classic attack built on it.
2. **Guarding the stack and the pages.** A [stack canary](/stack-canary/) catches a contiguous overwrite at the function's return, data execution prevention stops injected code from running, and a [shadow stack](/shadow-stack/) keeps a protected copy of each return address.
3. **Code reuse and randomization.** The [return-to-libc attack](/return-to-libc-attack/) and return-oriented programming run code that already exists. Address space layout randomization hides its addresses behind $k$ random bits, and the [derandomization attack](/aslr-derandomization-attack/) recovers 16 bits in minutes.
4. **Confining control flow and memory.** Control-flow integrity checks each indirect transfer against labels from a static graph. [Code-pointer integrity](/code-pointer-integrity/) protects the code pointers themselves, and software fault isolation keeps a module's stores and jumps inside its own domain.
5. **Attacks that stay inside the policy.** [Control-flow bending](/control-flow-bending/) works against fully precise static CFI, and [data-oriented programming](/data-oriented-programming/) builds Turing-complete attacks by corrupting only data.
6. **Checking bounds.** [Fat pointers](/fat-pointer/), [shadow memory](/shadow-memory/), AddressSanitizer's redzones, [Jones-Kelly checking](/jones-kelly-bounds-checking/), [baggy bounds](/baggy-bounds-checking/) and SoftBound are different answers to one question: where to keep the bounds of each object, and when to check them.
7. **Temporal safety and hardware support.** [Lock-and-key checking](/lock-and-key-temporal-checking/) and [dangling pointer nullification](/dangling-pointer-nullification/) catch uses after free. [Memory tagging](/memory-tagging/) and the [CHERI capability model](/cheri-capability-model/) move the checks into the processor.

## A first reading

Read these in order:

1. [Memory safety](/memory-safety/)
2. [Buffer overflow](/buffer-overflow/)
3. [Stack smashing](/stack-smashing/)
4. [Stack canary](/stack-canary/)
5. [Data execution prevention](/data-execution-prevention/)
6. [Return-oriented programming](/return-oriented-programming/)
7. [Address space layout randomization](/address-space-layout-randomization/)
8. [Shadow stack](/shadow-stack/)
9. [Control-flow integrity](/control-flow-integrity/)
10. [Shadow memory](/shadow-memory/)
11. [AddressSanitizer](/addresssanitizer/)
12. [Fat pointer](/fat-pointer/)

The return-to-libc attack is a gentler way into return-oriented programming; read it first if the gadgets seem abrupt. The advanced checkers (Jones-Kelly, baggy bounds, SoftBound, lock-and-key), the two attacks inside the policy and the hardware designs can wait. Each of them refines something in the first reading, and nothing in the first reading needs them.

## Before you start

Stack smashing rests on the layout of an [activation record](/activation-record/) and the [stack](/stack/) of pending calls. Control-flow integrity starts from a [control-flow graph](/control-flow-graph/) and a [call graph](/call-graph/) from program analysis, and its labels come from a [disjoint set](/disjoint-set/) structure. The bounds checkers sit on top of an allocator: a [free list](/free-list/) or the [buddy system](/buddy-system/), and Jones-Kelly checking keeps its objects in a [splay tree](/splay-tree/). Software fault isolation is the classic [inline reference monitor](/inline-reference-monitor/), a [reference monitor](/reference-monitor/) built into the code it watches. The probability arguments for canaries, randomization and tags use the [geometric distribution](/geometric-distribution/) and the [union bound](/union-bound/), and memory safety is a [safety property](/safety-property/) in the sense of model checking. The examples use a little C and a little x86: pointers and arrays, calls and returns, and the fact that the stack grows down.
