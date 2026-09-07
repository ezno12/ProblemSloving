# LeetCode 733 - Flood Fill

Pattern: Breadth-First Search / Depth-First Search (Grid Traversal)

Difficulty: Easy

## Idea

Starting from (sr, sc), explore all connected cells that share the same original color, changing each one to the new color.

For each cell, check its four neighbors (up, down, left, right) using row/col deltas; if a neighbor is within bounds and matches the original color, continue the fill there too.

## Complexity

* Time: O(rows * cols)
* Space: O(rows * cols) for the visited/queue tracking

## Mistakes

* Solved cleanly on the first accepted attempt. Edge case to double check: if the new color is the same as the original color, no changes are needed (and naive recursion could loop forever without a visited check).

## Recognition

Look for this pattern when you have:

* A grid where connected regions of the same value must be explored/relabeled
* Movement is restricted to four (or eight) directional neighbors

## Keywords

* Breadth-First Search
* Depth-First Search
* Grid/Matrix
* Connected Region
* Flood Fill

## Similar Problems

* 200. Number of Islands
* 130. Surrounded Regions
* 695. Max Area of Island