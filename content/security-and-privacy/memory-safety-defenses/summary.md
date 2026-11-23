## What to remember

- An access of $w$ bytes through $p$, derived from object $o$, is spatially safe when $\mathrm{base}(o) \le \mathrm{addr}(p)$ and $\mathrm{addr}(p) + w \le \mathrm{base}(o) + \mathrm{size}(o)$, and temporally safe when $o$ is live. Memory safety is a safety property: a run that stops at the first unsafe access counts as safe.
- A checker detects the unsafe access and stops the run. DEP, CFI, CPI, SFI and a shadow stack let the error happen and prevent one effect of it. A canary, ASLR and random tags only mitigate: they rest on a secret of $b$ bits, one blind attempt succeeds with probability $2^{-b}$, and a leak removes the protection.
- Without renewal a $k$-bit secret falls in $(2^k + 1)/2$ attempts on average, with renewal in $2^k$, so renewal gains about one bit. Learning the secret in parts makes the cost a sum over the parts instead of a product.
- DEP stops injected code only. Return-to-libc calls whole functions, and return-oriented programming chains short sequences that end in a return; Shacham found a Turing-complete set of them in the C library on x86.
- CFI with union-find labels accepts a transfer from $s$ exactly when the target lies in the component $T^*(s)$ of the site-target graph. It is exact when any two allowed sets are equal or disjoint, and no labeling with one label per target does better.
- Control-flow bending stays inside a fully precise static graph, and data-oriented programming changes no code pointer at all. A data-only attack is stopped only by defenses that protect data, from full memory safety to data-flow integrity.
- Bounds live with the pointer (fat pointers, SoftBound), with the object (Jones-Kelly, baggy bounds) or with the address (AddressSanitizer). Per-pointer bounds catch an access that lands in another live object; redzones miss an access that jumps over the redzone.
- Lock-and-key checking compares a key that is never reused, so it is complete for temporal errors. AddressSanitizer only delays reuse with a quarantine, and $k$-bit random tags miss a stale access with probability $2^{-k}$.

## The defenses side by side

| Defense | Promise | Cost in the entry | Measured in the entry | Gets past it |
|---|---|---|---|---|
| [Stack canary](/stack-canary/) | mitigates | $O(1)$ per call | none given | a leak, a write that skips it |
| [DEP](/data-execution-prevention/) | prevents running written bytes | page permissions | none given | code reuse |
| [ASLR](/address-space-layout-randomization/) | mitigates | at load time | 16 bits found in 216 s | leaks, forking servers |
| [Shadow stack](/shadow-stack/) | prevents changed returns | $O(1)$ per call | about 10%, or 3.5% parallel | forward edges, data attacks |
| [CFI](/control-flow-integrity/) | prevents transfers outside $T^*(s)$ | $O(1)$ per transfer | 16% average, 0 to 45% | control-flow bending |
| [CPI](/code-pointer-integrity/) | prevents corrupted code pointers | $O(1)$ per sensitive access | 2.9% on C, 8.4% on C/C++ | data attacks |
| [SFI](/software-fault-isolation/) | prevents stores outside the domain | $O(1)$ per store | 4% average | errors inside the domain |
| [AddressSanitizer](/addresssanitizer/) | detects | $\Theta(1)$, shadow $\Theta(m/8)$ | 73% on SPEC CPU2006 | jumps over a redzone |
| [Baggy bounds](/baggy-bounds-checking/) | detects | $\Theta(1)$, table $\Theta(m/16)$ | 8% less Apache throughput | accesses into padding |
| [SoftBound](/softbound/) | detects spatial errors | $\Theta(1)$, metadata $\Theta(s)$ | 67% for full checks | temporal errors |
| [Lock-and-key](/lock-and-key-temporal-checking/) | detects temporal errors | $\Theta(1)$ per access | none given | spatial errors |
| [Memory tagging](/memory-tagging/) | detects with probability $1 - 2^{-k}$ | a tag compare per access | none given | a chance tag match |

: Costs in the entries' models, with $m$ bytes of memory and $s$ locations that hold pointers. The percentages are the original papers' measurements on their own benchmarks and machines, so they do not rank the defenses against each other.

## Choosing a method

In testing, run AddressSanitizer under a fuzzer. It makes no false reports for aligned accesses and finds overflows and recent uses after free. When a missed error is not acceptable, SoftBound with lock-and-key checking gives complete spatial and temporal checks, at a measured cost of tens of percent.

In deployed code, combine the cheap defenses, because each covers a gap of another: a canary or a shadow stack for returns, DEP so that data never runs, ASLR so that code reuse needs a leak first, and CFI or CPI for forward edges. Renew canaries and layouts in forked workers. To run untrusted code in one address space, use software fault isolation, whose guarantee rests on the verifier and not on the compiler.
