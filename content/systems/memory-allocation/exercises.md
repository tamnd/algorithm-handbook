1. ◦ The free blocks of a heap have 6, 10, 4 and 12 words. Compute the [external fragmentation](/external-fragmentation/) $1 - L/T$, where $L$ is the largest free block and $T$ the free total. In the heap model of [first fit](/first-fit-allocation/), where a request for $n$ words needs a block of $\max(4, n + 2)$ words, what is the largest request that can succeed?

2. ◦ Use the heap of the first-fit entry: $H = 64$, used blocks of 4 words at 12, 24 and 44, and free blocks $(0, 12)$, $(16, 8)$, $(28, 16)$ and $(48, 16)$, written as (start, size). Every block has the tag $2s + u$ in its first and last word, with $u = 1$ when it is used. Free the block at 44 with [boundary tags](/boundary-tags/). Which three tag words does the free read, and what values do they hold? Which block results, and which tag values are written where?

3. ◦ A [bitmap allocator](/bitmap-allocator/) with words of 16 bits has the free mask $f$ whose 1 bits are the units 1, 2, 5, 6, 7, 10, 11, 12, 13 and 14 (bit $j$ is unit $j$). Run RUN-OF-ONES$(f, 4)$: write the set of 1 bits after each AND step, and give the unit where a block of 4 units starts.

4. ◦ Three requests of 17, 33 and 100 bytes are rounded up by [size classes](/size-classes/). Give the total block size and the total waste with classes that are multiples of 16, with powers of two, and with four classes per doubling (…, 16, 20, 24, 28, 32, 40, 48, 56, 64, 80, 96, 112, 128).

5. ◦ A [buddy system](/buddy-system/) manages a heap of 32 words, all free at the start, and gives each request the smallest power of two that holds it. Serve requests for 5, 3 and 9 words; a split keeps the lower half and puts the upper half on its free list. Give the address of each block and the free lists after the three requests. Then free the block of 5 words and then the block of 3 words, and give the free lists after each free.

6. ◦ A [slab allocator](/slab-allocator/) uses pages of 4096 bytes and colors slabs in steps of 8 bytes. For objects of 200 bytes, how many objects fit in a slab, how many bytes are left over, and how many different color offsets are there? Answer the same for objects of 256 bytes.

7. ◦ A [bump-pointer allocator](/bump-pointer-allocation/) has top $= 13$ and computes $p = (top + a - 1) \text{ AND NOT } (a - 1)$. Serve three requests: 8 bytes with alignment 8, 3 bytes with alignment 1, and 16 bytes with alignment 16. Give each address, the final top and the total padding.

8. ◦ A heap, read from its low end to its high end, is free, used, used, free, used, free, used, used. Count the used blocks with two, one and no free neighbours, and check the identity $2M = 2A + B + e$ of [Knuth's fifty-percent rule](/knuth-fifty-percent-rule/). Then take $N = 600$ blocks in use and $p = 0.9$: give the range of the expected number of free blocks, the share of all blocks that are free, and the share of memory that is free if an average free block is twice the size of an average used block.

9. ◦ A heap of 20 words holds live blocks $(2, 3)$, $(7, 2)$, $(10, 4)$ and $(17, 1)$. Give the largest hole before and after a sliding [memory compaction](/memory-compaction/), the new address of each block, and the number of words copied.

10. • On the heap of Exercise 2, before the free, serve malloc(2), malloc(10) and malloc(12) with address-ordered first fit, [best fit](/best-fit-allocation/) and [worst fit](/worst-fit/). A remainder of fewer than 4 words is not split off, ties go to the lowest address, and best fit stops at an exact fit. For each policy give the blocks used, the probes per request and the free list at the end. Which policy fails, and with how many free words?

11. • With four size classes per doubling, sizes 1 to 8 have a class each and every doubling above 8 adds four classes. How many classes cover the sizes up to $2^{10}$? Which request wastes the largest share of its block among the requests 9 to 64, and what is that share? Show that the request $2^k + 1$ wastes less than $1/5$ of its block and that the share tends to $1/5$.

12. • [TLSF](/tlsf/) runs with $J = 4$. Find the class $(fl, sl)$ that holds a free block of 1000 words, and the class that MAPPING-SEARCH returns for malloc(1000). To what size is the request rounded, and what is the largest free block that this malloc does not see?

13. • In the [Fibonacci buddy system](/fibonacci-buddy-system/) the block sizes are 1, 2, 3, 5, 8, 13, 21, … and each request gets the smallest size that holds it. Among the requests from 1 to 100 words, which one wastes the largest share of its block, and what is that share? Show that the share is always below $2/5$, and find its limit.

14. • Take $M = 1024$ live words and sizes up to $n = 16$. Compute Robson's exact optimum for power-of-two sizes, the bound of one region per size, and the bound $2M(\log_2 n + 1)$ for any sizes ([Robson's bound](/robson-bound/)). What lower bound do you get for sizes up to $n = 20$? For $n = 2^{10}$ and large $M$, by what factor does the bound for any sizes exceed the exact optimum for powers of two?

15. • Show that address-ordered first fit never uses more than $M$ words when every request has size 1, and that this is optimal. Check that Robson's formula $M(1 + \tfrac12 \log_2 n) - n + 1$ gives the same value for $n = 1$.

16. • An online allocator serves requests of 1 and 2 words with at most 4 words live. Show that an adversary can force it to use at least 5 words, with three requests of 1 word, one free and one request of 2 words. Show that if the lifetimes of the same items were known in advance, 4 words would be enough.

17. • Items of [offline dynamic storage allocation](/offline-dynamic-storage-allocation/), written (start, end, size), are A $= (0, 2, 1)$, B $= (0, 5, 1)$, C $= (1, 5, 1)$ and D $= (3, 5, 2)$. Compute LOAD, the memory used by first fit by start time, and an optimal placement.

18. • [dlmalloc](/dlmalloc/) with 32-bit sizes uses a chunk of $\max(16, \lceil (r + 4)/8 \rceil \cdot 8)$ bytes for a request of $r$ bytes. Find the chunk size for $r = 1$, 12, 13, 100 and 252, and say which of them are served from the small bins.

19. • [Hoard](/hoard-allocator/) runs with superblocks of $S = 64$ bytes, $f = 1/4$ and $K = 1$. A heap holds 4 superblocks. Below which value of $u_i$ does it cross the emptiness threshold? Derive from the invariant the largest number of superblocks that a heap may hold after a free when $u_i = 150$, and when $u_i = 30$.

20. • The anchor of the [lock-free allocator](/lock-free-memory-allocator/) has a tag of 42 bits that grows by 1 at every pop. If the pops of one superblock run at $10^9$ per second, how long does the tag take to come back to the same value? How long with a tag of 16 bits?

21. ★ A buddy system manages $2^m$ words, merges two free buddies at once, and allows blocks of one word. Find the largest number of free words at which a request for $2^k$ words can fail, prove that no state has more, and give a sequence of requests and frees that reaches it.

22. ★ Requests have 1 or 2 words, at most 4 words are live, and the allocator is address-ordered first fit. Prove that first fit never uses more than 6 words. With the trace in the entry on Robson's bound, this shows that 6 is its worst case.

23. ★ Under the same rules, design an online allocator that never uses more than 5 words, which matches Robson's exact value for $M = 4$ and $n = 2$. Prove that it never fails inside 5 words.

24. ★ Requests have 1, 2 or 4 words and at most 8 words are live. Give a sequence of requests and frees that forces address-ordered first fit to use 16 words, three more than the optimum of [online memory allocation](/online-memory-allocation/) for these sizes.

25. ★ Hoard checks the emptiness threshold only after a free. With $S = 64$ bytes, $f = 1/4$ and $K = 0$, give a short sequence of mallocs and one free in one heap, with three size classes, after which the free must move three superblocks to the global heap before the invariant holds again.
