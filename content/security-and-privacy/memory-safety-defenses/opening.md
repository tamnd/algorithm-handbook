A program in C or C++ can write past the end of an array, read memory after it has been freed, or follow a pointer that was never set. The language does not check, and the result is undefined. For an attacker such an error is a tool: an overflow on the stack can replace a return address, and a freed object that is used again can be filled with chosen bytes first. Vendors of browsers and operating systems report memory errors of this kind among the most common causes of their serious vulnerabilities. Memory safety defenses either make these errors impossible, by checking every access against the bounds and the lifetime of its object, or make them hard to exploit, by hiding or guarding what an attacker needs.

The two approaches trade cost for strength. Full checking stops the error where it happens, but costs time and memory on every access. Mitigations are cheap but probabilistic or partial, and each one has been followed by an attack that works around it.

## What the chapter will cover

The entries of this chapter are being written. They will cover:

1. **Memory errors and their exploits.** Memory safety as a property, the buffer overflow and stack smashing, the return-to-libc attack, return-oriented programming, data-oriented programming and control-flow bending.
2. **Mitigations.** Stack canaries, data execution prevention, address space layout randomization and its derandomization by brute force, and shadow stacks.
3. **Control-flow integrity.** Control-flow integrity, code-pointer integrity and software fault isolation, which confine where a jump may go and what a module may touch.
4. **Bounds checking.** Fat pointers, Jones-Kelly bounds checking, baggy bounds checking, SoftBound, shadow memory and AddressSanitizer.
5. **Temporal safety and hardware support.** Lock and key temporal checking, dangling pointer nullification, memory tagging and the CHERI capability model.

## What to read meanwhile

The layout that these attacks exploit is in Volume 26: [stack allocation](/stack-allocation/), the [free list](/free-list/) and [boundary tags](/boundary-tags/) of a heap allocator, and [region-based memory management](/region-based-memory-management/). Garbage collection removes use after free, at a cost; read [mark-and-sweep](/mark-and-sweep/) and [reference counting](/reference-counting/) there. [Integer overflow](/integer-overflow/) in Volume 11 explains the wrapped size computations that often come before a buffer overflow.

Languages can rule the errors out at compile time. [Linear types](/linear-types/) and [borrow checking](/borrow-checking/) in Volume 34 give each object one owner and bound the lifetime of every reference, and [escape analysis](/escape-analysis/) decides when an object may live on the stack. [Separation logic](/separation-logic/) in Volume 1 proves that a program touches only the memory it owns.
