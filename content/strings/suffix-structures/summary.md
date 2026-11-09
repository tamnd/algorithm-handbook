## What to remember

- Every substring of a text is a prefix of a suffix. A structure that holds the suffixes in sorted order answers substring questions in time that depends on the pattern, not on the text.
- A **sentinel** at the end of the text makes every suffix end at its own leaf and fixes the sorted order. Without it, a suffix that is a prefix of another hides inside the tree.
- The **suffix array** takes $n$ integers. The occurrences of a pattern form one block of it, found with $O(m \log n)$ comparisons, or $O(m + \log n)$ with stored LCP values.
- **Suffix sorting** takes $O(n \log n)$ time by prefix doubling, which sorts by the first $2h$ symbols using the ranks of the first $h$, and $O(n)$ time over an integer alphabet by SA-IS or DC3.
- The **LCP array** gives the common prefix of neighbors in sorted order. Kasai's algorithm builds it in $O(n)$ time because the value drops by at most one from suffix $i$ to suffix $i + 1$. The common prefix of any two suffixes is a range minimum of it.
- One scan of the suffix array and the LCP array gives the number of distinct substrings, $n(n+1)/2 - \sum LCP$, the longest repeated substring, the longest common substring of two strings, and shortest unique substrings.
- The **suffix tree** has at most $2n + 1$ nodes. Ukkonen, McCreight and Weiner build it in $O(n)$ time for a constant alphabet with **suffix links**; Farach does so for an integer alphabet.
- The **suffix automaton** has at most $2n - 1$ states and $3n - 4$ transitions, and is built online. Each state stands for the substrings with one set of end positions.
- The **FM-index** stores the Burrows-Wheeler transform with rank structures. It counts a pattern with $m$ steps of backward search in space close to the compressed text.

## The structures side by side

| Structure | Space in words | Build time | Count occurrences | Online |
|---|---|---|---|---|
| [Suffix trie](/suffix-trie/) | $\Theta(n^2)$ worst | $\Theta(n^2)$ worst | $O(m)$ | yes |
| [Suffix tree](/suffix-tree/) | $\Theta(n)$, large constant | $O(n)$ | $O(m)$ | yes, by Ukkonen |
| [Suffix array](/suffix-array/) with [LCP array](/lcp-array/) | $2n$ | $O(n)$ | $O(m + \log n)$ | no |
| [Suffix automaton](/suffix-automaton/) | $\Theta(n)$ | $O(n)$ | $O(m)$ | yes |
| [FM-index](/fm-index/) | about the compressed text | $O(n)$ after suffix sorting | $O(m)$ rank steps | no |

: Full-text indexes for a text of length $n$ and a pattern of length $m$, with times for a constant alphabet. Counting with the tree and the automaton needs a count stored at each node. The tree and the automaton are larger than the array by a constant factor; the FM-index can be smaller than the text itself.

## Choosing a method

- To search a fixed text for many patterns, build the suffix array with SA-IS or a library suffix sorter, add the LCP array with Kasai's algorithm, and search by binary search.
- For problems on repeats and common substrings, try one scan of the LCP array first. Most answers that a suffix tree gives by a depth-first walk come from the arrays with a stack.
- When the text arrives one symbol at a time, or in contest problems on the substrings of one string, use the suffix automaton, which is short to write and online.
- Use a suffix tree when an algorithm needs suffix links or tree navigation and memory is not tight, as in matching statistics.
- For texts of many gigabytes, such as genomes, use the FM-index; for collections of near copies, such as many versions of one genome, use the r-index.
- For a collection of documents, use a generalized structure with a document array, and the document listing methods when the documents that match matter more than the positions.
