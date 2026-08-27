# Patterns

Pattern notes for coding interviews. One file per pattern, every file in the same shape:

**Recognition / Tricks / Template / Complexity / Problems / Mistakes / Keywords**

Same section vocabulary as the problem notes in `../Problems/Notes`, so a pattern note and a
problem note read the same way. Code is Python.

Structure follows the [AlgoMonster](https://algo.monster) Core Patterns curriculum and its 20
official code templates, extended with the families taught as chapters that have no template
page (stack, heap, Kadane, line sweep, divide & conquer, Dijkstra, MST, fast-and-slow,
segment tree, and the eight DP families). 35 patterns total.

**Start with [Pattern Decision Guide](Pattern%20Decision%20Guide.md)** — the
constraint-to-complexity table, the keyword-to-pattern table, the tie-breakers for ambiguous
wording, and a pre-submit checklist. Recognition is the skill; the templates are the easy part.

## How to use these

1. Read **Recognition** first. Do not read the template yet.
2. Re-derive the **Template** from memory, then compare.
3. Tick problems off in **Problems** as you solve them.
4. Every time you get one wrong, add a line to **Mistakes**. That section is the
   highest-value part of the note and it should grow over time.

## Index

### Arrays

* [Two Pointers](Arrays/Two%20Pointers.md)
* [Fast and Slow Pointers](Arrays/Fast%20and%20Slow%20Pointers.md)
* [Sliding Window](Arrays/Sliding%20Window.md)
* [Prefix Sum](Arrays/Prefix%20Sum.md)
* [Kadane](Arrays/Kadane.md)

### Binary Search

* [Binary Search](Binary%20Search/Binary%20Search.md)

### Trees

* [DFS on Tree](Trees/DFS%20on%20Tree.md)
* [BFS on Tree](Trees/BFS%20on%20Tree.md)

### Backtracking

* [Backtracking - Basic](Backtracking/Backtracking%20-%20Basic.md)
* [Backtracking - Aggregation](Backtracking/Backtracking%20-%20Aggregation.md)

### Graphs

* [BFS on Graph](Graphs/BFS%20on%20Graph.md)
* [DFS on Graph](Graphs/DFS%20on%20Graph.md)
* [Matrix as Graph](Graphs/Matrix%20as%20Graph.md)
* [Topological Sort](Graphs/Topological%20Sort.md)
* [Dijkstra](Graphs/Dijkstra.md)
* [Minimum Spanning Tree](Graphs/Minimum%20Spanning%20Tree.md)

### Heap

* [Top K](Heap/Top%20K.md)
* [Two Heaps](Heap/Two%20Heaps.md)

### Stack

* [Stack](Stack/Stack.md)
* [Monotonic Stack](Stack/Monotonic%20Stack.md)

### Intervals

* [Interval Merge and Sweep](Intervals/Interval%20Merge%20and%20Sweep.md)
* [Line Sweep](Intervals/Line%20Sweep.md)

### Greedy

* [Greedy](Greedy/Greedy.md)

### Divide and Conquer

* [Divide and Conquer](Divide%20and%20Conquer/Divide%20and%20Conquer.md)

### Advanced Data Structures

* [Union Find](Advanced%20Data%20Structures/Union%20Find.md)
* [Trie](Advanced%20Data%20Structures/Trie.md)
* [Segment Tree](Advanced%20Data%20Structures/Segment%20Tree.md)

### Dynamic Programming

* [Constant Transition](Dynamic%20Programming/Constant%20Transition.md)
* [Grid](Dynamic%20Programming/Grid.md)
* [Dual Sequence](Dynamic%20Programming/Dual%20Sequence.md)
* [Non-constant Transition](Dynamic%20Programming/Non-constant%20Transition.md)
* [Knapsack](Dynamic%20Programming/Knapsack.md)
* [Interval](Dynamic%20Programming/Interval.md)
* [Tree](Dynamic%20Programming/Tree.md)
* [Bitmask](Dynamic%20Programming/Bitmask.md)

## Study order by ROI

AlgoMonster's data-driven ranking, if short on time:

1. **Highest ROI** — DFS, BFS, Two Pointers, Sliding Window
2. **High ROI** — Binary Search, Prefix Sum, Stack, hashmap, sorting
3. **Medium ROI** — Heap, Monotonic Stack, Intervals
4. **Secondary** — Trie, Union Find, Topological Sort
5. **Lower ROI** — Dynamic Programming, Greedy, Segment Tree, Dijkstra, MST

## Where I am

Snapshot of my AlgoMonster roadmap (tailored for Uber / LinkedIn), 27 Aug 2026. Roughly 128
of 282 lessons done — the dashboard counts 117 *completed* while the roadmap counts 154
*remaining*, because tested-out chapters are counted differently.

| Chapter | State | Patterns that cover it |
|---------|-------|------------------------|
| Getting Started | 18 lessons, complete | [Pattern Decision Guide](Pattern%20Decision%20Guide.md) |
| Binary Search | tested out | [Binary Search](Binary%20Search/Binary%20Search.md) |
| Two Pointers | tested out | [Arrays](Arrays) — all 5 |
| Depth-First Search | tested out | [DFS on Tree](Trees/DFS%20on%20Tree.md), [DFS on Graph](Graphs/DFS%20on%20Graph.md) |
| Backtracking | tested out | [Backtracking](Backtracking) — both |
| Breadth-First Search | tested out | [BFS on Tree](Trees/BFS%20on%20Tree.md), [BFS on Graph](Graphs/BFS%20on%20Graph.md) |
| **Graph** | **21 / 26 — in progress** | [Graphs](Graphs) — all 6 |
| Priority Queue / Heap | 8 lessons left | [Heap](Heap) — both |
| Dynamic Programming | 50 lessons left | [Dynamic Programming](Dynamic%20Programming) — all 8 |
| Advanced Data Structures | 15 lessons left | [Advanced Data Structures](Advanced%20Data%20Structures) — all 3 |
| Miscellaneous | 26 lessons left | Stack, Intervals, Greedy, Divide and Conquer, Kadane |

Next up: **Clone Graph** (flagged START). The chapter then finishes with topological sort,
Dijkstra, MST and the two Graph Speedruns.

Worth noting the tension with the ROI list: the 50 remaining DP lessons are the largest block
of work and the lowest-ROI block, and the roadmap is tailored for Uber and LinkedIn, which
lean on graphs and two pointers more than on DP.

## Sources

* [AlgoMonster code templates](https://algo.monster/templates/sliding-window-shortest) — the 20 templates, captured verbatim
* [Keyword to Algo Cheat Sheet](https://algo.monster/problems/keyword_to_algo)
* [Runtime to Algo Cheat Sheet](https://algo.monster/problems/runtime_summary)
* [Coding Interview Patterns / ROI](https://algo.monster/problems/stats)
* [The flowchart](https://algo.monster/flowchart)
