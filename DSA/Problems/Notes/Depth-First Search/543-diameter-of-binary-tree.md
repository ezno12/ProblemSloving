# LeetCode 543 - Diameter of Binary Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Do a DFS that returns the height of each subtree (using -1 as the height of an empty node, so a single leaf has height 0).

At every node, update a running best diameter (res[0]) with 2 + left_height + right_height, since the diameter through this node is the sum of the two subtree heights plus the two edges connecting them.

Return 1 + max(left, right) as the height contribution upward.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Key insight: the diameter is tracked in a mutable outer variable (res[0]) updated during the same traversal that computes height, avoiding an O(n^2) approach of recomputing height separately for every node.

## Recognition

Look for this pattern when you have:

* A binary tree where the longest path BETWEEN ANY TWO NODES (not necessarily through the root) is needed
* Combining a height calculation with tracking a running global best in one pass avoids redundant work

## Keywords

* Depth-First Search
* Binary Tree
* Diameter
* DP on Trees

## Similar Problems

* 104. Maximum Depth of Binary Tree
* 110. Balanced Binary Tree
* 1448. Count Good Nodes in Binary Tree