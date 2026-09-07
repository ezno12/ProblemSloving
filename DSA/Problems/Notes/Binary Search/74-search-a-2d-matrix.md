# LeetCode 74 - Search a 2D Matrix

Pattern: Binary Search (Staircase Search)

Difficulty: Medium

## Idea

Treat the matrix as sorted both by row and by column, and search from the top-right corner.

If the current cell equals the target, return true. If it is larger than the target, move left (decrease column); if smaller, move down (increase row).

This "staircase" walk eliminates one row or one column at each step.

## Complexity

* Time: O(rows + cols) as implemented (staircase search); a true binary search on a flattened index gives O(log(rows*cols))
* Space: O(1)

## Mistakes

* The last submission for this problem was a Wrong Answer, suggesting the staircase boundary condition (i < n && j >= 0) or the row/column decrement logic needs re-checking; revisit to confirm all edge cases (single row, single column, target smaller/larger than every element) are handled.

## Recognition

Look for this pattern when you have:

* A 2D grid sorted along both rows and columns
* Need to search efficiently without a full O(rows*cols) scan

## Keywords

* Binary Search
* Matrix
* Staircase Search
* Sorted Grid

## Similar Problems

* 240. Search a 2D Matrix II
* 704. Binary Search
* 378. Kth Smallest Element in a Sorted Matrix