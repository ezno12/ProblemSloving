# LeetCode 110 - Balanced Binary Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Do a DFS that returns the height of a subtree, but use -1 as a special "already unbalanced" sentinel that short-circuits further checks.

At each node, get the left and right heights; if either is -1, or if they differ by more than 1, propagate -1 upward. Otherwise, return 1 + max(left_height, right_height) as normal.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Using a single DFS that returns height AND detects imbalance (via the -1 sentinel) avoids the naive O(n^2) approach of recomputing height at every node separately.

## Recognition

Look for this pattern when you have:

* A binary tree where a global balance property depends on heights of every subtree
* Combining a height calculation with an early-exit failure signal avoids redundant work

## Keywords

* Depth-First Search
* Binary Tree
* Height Calculation
* Early Termination Sentinel

## Similar Problems

* 104. Maximum Depth of Binary Tree
* 543. Diameter of Binary Tree
* 111. Minimum Depth of Binary Tree