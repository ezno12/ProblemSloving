# Pattern Decision Guide

**Category:** Patterns

Read this before the individual pattern notes. Pattern **recognition** is the interview
skill; the templates are the easy part.

Three questions, in order:

1. What do the **constraints** allow? (rules out whole families of algorithms)
2. What **keywords** does the wording leak?
3. Which **invariant** can I state in one sentence? (if you cannot, you have the wrong pattern)

## Step 1 - Constraints tell you the complexity

Judges allow roughly 10-20 million operations. Read `n` off the constraints and the allowed
complexity follows. This is the single fastest way to eliminate wrong approaches.

The caps below are AlgoMonster's, which are deliberately conservative and Python-flavoured.
In C++/Java an O(n) pass comfortably handles 10^8. The rule that actually generalizes is the
operation budget: if `n` times your per-element work exceeds ~2 x 10^7, you need a better
complexity.

| Input size | You can afford | Which means |
|------------|----------------|-------------|
| n > 10^9 | O(1) | math formula, hashmap lookup, direct indexing |
| n > 10^8 | O(log n) | binary search, balanced BST, digits of a number |
| n <= 10^6 | O(n) | one pass, two pointers, tree/graph traversal, stack/queue |
| n <= 10^6 | O(n log k) | heap held at size k, n pushes (top-K) |
| n <= 10^6 | O(n log n) | sorting, divide & conquer with a linear merge |
| n <= 3000 | O(n^2) | nested loops, most 2D DP, many brute forces |
| n <= 20 | O(2^n) | subsets, bitmask DP, backtracking |
| n <= 12 | O(n!) | permutations |

Read it backwards too: `n <= 20` is practically an announcement that the answer is a bitmask
or subset enumeration. `n = 10^5` with an O(n^2) idea means you are missing a pattern.

## Step 2 - Keywords leak the pattern

| Wording in the problem | Pattern |
|------------------------|---------|
| "sorted", "rotated sorted", "in O(log n)" | [Binary Search](Binary%20Search/Binary%20Search.md) |
| "minimum X such that", "maximum X such that" | [Binary Search](Binary%20Search/Binary%20Search.md) |
| "two sum", "k sum", pair from a sorted array | [Two Pointers](Arrays/Two%20Pointers.md) |
| "palindrome" — verify one string | [Two Pointers](Arrays/Two%20Pointers.md) |
| in-place filter, "remove duplicates", "move zeros" | [Two Pointers](Arrays/Two%20Pointers.md) |
| "cycle", "n-th from the end", "middle of the list" | [Fast and Slow](Arrays/Fast%20and%20Slow%20Pointers.md) |
| "substring" / "subarray" with a fixed size k | [Sliding Window](Arrays/Sliding%20Window.md) |
| "longest" + contiguous + "at most K" | [Sliding Window](Arrays/Sliding%20Window.md) |
| "shortest" + contiguous + "contains all of" | [Sliding Window](Arrays/Sliding%20Window.md) |
| "subarray sum equals", range sums, negatives present | [Prefix Sum](Arrays/Prefix%20Sum.md) |
| "maximum sum subarray", contiguous with negatives | [Kadane](Arrays/Kadane.md) |
| "tree" + sums, heights, paths | [DFS on Tree](Trees/DFS%20on%20Tree.md) |
| "tree" + level order, depth, side view | [BFS on Tree](Trees/BFS%20on%20Tree.md) |
| "return all", "generate every", permutations/subsets | [Backtracking - Basic](Backtracking/Backtracking%20-%20Basic.md) |
| "how many ways", "minimum number of" over choices | [Backtracking - Aggregation](Backtracking/Backtracking%20-%20Aggregation.md) |
| "shortest path" / "fewest steps", unweighted | [BFS on Graph](Graphs/BFS%20on%20Graph.md) |
| "connectivity", "flood fill", "count regions" | [DFS on Graph](Graphs/DFS%20on%20Graph.md) |
| "matrix", "grid", "islands" | [Matrix as Graph](Graphs/Matrix%20as%20Graph.md) |
| "prerequisites", "build order", "course", "schedule" | [Topological Sort](Graphs/Topological%20Sort.md) |
| "shortest path" with non-negative WEIGHTS | [Dijkstra](Graphs/Dijkstra.md) |
| "connect everything at minimum cost" | [Minimum Spanning Tree](Graphs/Minimum%20Spanning%20Tree.md) |
| "top K", "K closest", "K most frequent", "merge K" | [Top K](Heap/Top%20K.md) |
| "median of a stream" | [Two Heaps](Heap/Two%20Heaps.md) |
| "parentheses", "brackets", nested, "evaluate" | [Stack](Stack/Stack.md) |
| "next greater", "next smaller", "warmer day", histogram | [Monotonic Stack](Stack/Monotonic%20Stack.md) |
| "merge intervals", "meeting rooms", "overlapping" | [Interval Merge and Sweep](Intervals/Interval%20Merge%20and%20Sweep.md) |
| "maximum concurrent", covered area, skyline | [Line Sweep](Intervals/Line%20Sweep.md) |
| "jump", reachability, "minimum number of X to cover" | [Greedy](Greedy/Greedy.md) |
| "count smaller to the right", merge-sort flavour | [Divide and Conquer](Divide%20and%20Conquer/Divide%20and%20Conquer.md) |
| "same group?", "connected component", edges arriving | [Union Find](Advanced%20Data%20Structures/Union%20Find.md) |
| "prefix", "starts with", "autocomplete", "dictionary" | [Trie](Advanced%20Data%20Structures/Trie.md) |
| range query AND point update on one array | [Segment Tree](Advanced%20Data%20Structures/Segment%20Tree.md) |
| depends on the last one or two positions | [DP - Constant Transition](Dynamic%20Programming/Constant%20Transition.md) |
| grid + "paths" or "minimum cost to reach" | [DP - Grid](Dynamic%20Programming/Grid.md) |
| TWO strings compared, edit distance, LCS | [DP - Dual Sequence](Dynamic%20Programming/Dual%20Sequence.md) |
| "longest increasing", depends on ALL earlier indices | [DP - Non-constant Transition](Dynamic%20Programming/Non-constant%20Transition.md) |
| "capacity", "target sum", "coins", subset-sum | [DP - Knapsack](Dynamic%20Programming/Knapsack.md) |
| range `[i..j]`, burst/merge, two-player from the ends | [DP - Interval](Dynamic%20Programming/Interval.md) |
| tree + "cannot pick a node and its child" | [DP - Tree](Dynamic%20Programming/Tree.md) |
| "visit every node once", n <= 20 | [DP - Bitmask](Dynamic%20Programming/Bitmask.md) |
| "transitive": A~B and B~C implies A~C | it is a graph — [BFS on Graph](Graphs/BFS%20on%20Graph.md) or [Union Find](Advanced%20Data%20Structures/Union%20Find.md) |
| "game", "can the player to move force a win" | DP on game states — [DP - Interval](Dynamic%20Programming/Interval.md) |

## Step 3 - One keyword, several patterns

The words below are ambiguous on purpose. These are the sub-signals that decide:

* **"subarray" vs "subsequence"** — subarray is CONTIGUOUS ([window](Arrays/Sliding%20Window.md) /
  [prefix sum](Arrays/Prefix%20Sum.md)); subsequence is not (DP). This single distinction decides
  more problems than any other.
* **"subarray" / "substring"** — fixed size or a monotonic constraint -> [Sliding Window](Arrays/Sliding%20Window.md).
  Range sums -> [Prefix Sum](Arrays/Prefix%20Sum.md). Sum equals a target -> prefix sums in a hashmap.
* **"shortest"** — unweighted graph -> [BFS](Graphs/BFS%20on%20Graph.md). Non-negative weights ->
  [Dijkstra](Graphs/Dijkstra.md). Cumulative cost on a grid/sequence -> [DP](Dynamic%20Programming/Grid.md).
* **"how many ways"** — choices form a decision tree -> DFS. Subproblems overlap -> DP.
  They are the same algorithm; memoization is the bridge
  ([see aggregation](Backtracking/Backtracking%20-%20Aggregation.md)).
* **"palindrome"** — verify one string -> [Two Pointers](Arrays/Two%20Pointers.md). Enumerate partitions ->
  [backtracking](Backtracking/Backtracking%20-%20Basic.md). Count or minimize cuts -> [interval DP](Dynamic%20Programming/Interval.md).
* **"tree"** — do you care about DEPTH? Yes -> [BFS on Tree](Trees/BFS%20on%20Tree.md). No -> [DFS on Tree](Trees/DFS%20on%20Tree.md).
* **"matrix"** — connectivity question -> [BFS/DFS](Graphs/Matrix%20as%20Graph.md). Optimization
  question -> [grid DP](Dynamic%20Programming/Grid.md).
* **"jump"** — is "reach as far as possible" provably optimal? Yes -> [Greedy](Greedy/Greedy.md). No -> DP.
* **"connected component"** — graph built once, few traversals -> [BFS/DFS](Graphs/DFS%20on%20Graph.md).
  Edges arriving over time, or many queries -> [Union Find](Advanced%20Data%20Structures/Union%20Find.md).
* **"longest"** — fixed window involved -> [Sliding Window](Arrays/Sliding%20Window.md) / monotonic deque. Position
  depends on earlier positions -> [DP](Dynamic%20Programming/Non-constant%20Transition.md).

## Step 4 - State the invariant

Before writing code, finish this sentence: *"At every step, X is true."*

* **Binary Search:** the answer, if it exists, is inside `[left, right]`
* **Two Pointers, same direction:** `arr[0:slow]` is the finished answer
* **Sliding Window, longest:** after the shrink loop, the window is valid
* **Sliding Window, shortest:** the answer is recorded while the window is still valid,
  before the shrink (on loop exit it is deliberately invalid)
* **BFS:** everything at distance d is dequeued before anything at distance d+1
* **Backtracking:** on entry and on exit, the state is identical
* **DP:** `dp[i]` is final and correct before any `dp[j>i]` reads it
* **Greedy:** swapping any pair away from this order never improves the result

If you cannot state it, you do not yet understand the solution — and that is exactly where
the off-by-one bugs come from.

## Before you submit

Derived from the recurring feedback on my own AlgoMonster submissions:

- [ ] **Empty input.** `arr[-1]`, `arr[0]`, `grid[0]` on an empty input raises IndexError.
      Handle `n == 0` explicitly, every time.
- [ ] **Syntax / undefined names / type mismatches.** These crash before the algorithm even
      runs and cost the whole submission. Re-read the code once, top to bottom.
- [ ] **Single-element and two-element inputs.** Most off-by-ones surface here.
- [ ] **All-negative / all-equal / all-duplicate inputs.**
- [ ] Did I return the right thing — length vs array, index vs value, `-1` vs `None`?
- [ ] Are the placeholder helpers (`feasible`, `is_valid`, `get_neighbors`, `find`) actually
      implemented, and not still stubs returning their input?

## Do not memorize any of this

AlgoMonster's own advice about their flowchart applies here too: it is a reference, not a
thing to memorize. Use it while solving, and you will stop needing it.

## Keywords

* Pattern Recognition
* Constraints
* Time Complexity
* Operation Budget
* Keyword Mapping
* Invariant
* Decision Tree
* Subarray vs Subsequence
