# LeetCode 111 - Minimum Depth of Binary Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Recursively compute the depth of the left and right subtrees.

If either subtree is missing (depth 0), the minimum depth must go through the other subtree, so return left_depth + right_depth + 1 (this correctly handles one-sided nodes).

Otherwise, return 1 + min(left_depth, right_depth).

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Key edge case: a node with only one child is NOT a leaf, so the minimum depth cannot simply take the min of two subtree depths when one side is 0.

## Recognition

Look for this pattern when you have:

* A binary tree where the SHORTEST root-to-leaf path is needed
* Nodes with only one child must be excluded from being treated as leaves

## Keywords

* Depth-First Search
* Binary Tree
* Minimum Depth
* One-Sided Node Edge Case

## Similar Problems

* 104. Maximum Depth of Binary Tree
* 110. Balanced Binary Tree
* 543. Diameter of Binary Tree