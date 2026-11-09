A [dynamic array](/dynamic-array/) appends an item in one step until it is full. Then it allocates an array twice as large and copies every item into it, which takes as many steps as there are items. One append in a million can cost a million steps. Yet a million appends from an empty array cost fewer than three million steps in all: the copies cost $1 + 2 + 4 + \cdots$, a geometric series less than twice the final size. Averaged over the whole sequence, an append costs less than 3 steps, and this holds for every sequence, not only for typical ones.

Amortized analysis makes this kind of statement precise. It bounds the total cost of a sequence of operations and charges each operation a share, its amortized cost, so that the shares always cover the actual total. The analyses of many data structures in later volumes, from [union-find](/union-find-amortized-bound/) to [splay trees](/splay-tree/) and [Fibonacci heaps](/fibonacci-heap/), are amortized, and this chapter gives the methods they use.

An amortized bound is a guarantee, not an estimate. It assumes nothing about the input and uses no probability: an adversary who chooses the worst possible sequence of operations still pays at most the amortized cost per operation on the whole. What it does not limit is the cost of a single operation, which can still be large. A program that must answer every request within a fixed time needs a worst-case bound, and the last group of the chapter shows how to get one.

## What the chapter covers

The chapter is in five groups, read in order.

1. **Cost over a sequence.** The [amortized cost](/amortized-cost/) and how an amortized bound differs from a [worst-case bound](/amortized-vs-worst-case/) on each operation.
2. **Two standard examples.** [Incrementing a binary counter](/binary-counter-increment/) and the [stack with multipop](/stack-with-multipop/).
3. **Three methods.** The [aggregate method](/aggregate-method/), the [accounting method](/accounting-method/), and the [potential method](/potential-method/) with its [potential function](/potential-function/).
4. **Tables that grow and shrink.** [Array doubling](/array-doubling/) and [contraction](/dynamic-table-contraction/) of a table that has become too empty.
5. **Other kinds of guarantee.** [Amortized versus expected cost](/amortized-vs-expected-cost/), and [global rebuilding](/global-rebuilding/), which turns some amortized bounds into worst-case ones.

## A first reading

For a first reading, take these entries in order: [amortized cost](/amortized-cost/), [amortized versus worst-case cost](/amortized-vs-worst-case/), [binary counter increment](/binary-counter-increment/), [stack with multipop](/stack-with-multipop/), [aggregate method](/aggregate-method/), [accounting method](/accounting-method/), [potential function](/potential-function/), [potential method](/potential-method/) and [array doubling](/array-doubling/). That is the whole method; the rest of the chapter applies it. Read [dynamic table contraction](/dynamic-table-contraction/) when you need a table that also shrinks, and the last group when an amortized bound is not enough for your purpose, for example in a program that must answer within a fixed time.

## Before you start

You need [asymptotic notation](/asymptotic-notation/) and the [geometric series](/geometric-series/) from Chapter 1.2, and the idea of a [stack](/stack/) from Volume 3. The entry on amortized versus expected cost uses [expected values](/expected-value/), which Chapter 1.6 defines; you can read that entry after Chapter 1.6. No other chapter of this volume is needed.
