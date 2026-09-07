# LeetCode 235 - Lowest Common Ancestor of a Binary Search Tree

Pattern: Depth-First Search (BST property)

Difficulty: Medium

## Idea

Use the BST ordering property instead of a general tree LCA algorithm.

At the current node, if both p and q have values greater than the node, the LCA must be in the right subtree; if both are smaller, it must be in the left subtree.

Otherwise, the current node is the split point where p and q diverge, so it is the LCA.

## Complexity

* Time: O(h), where h is tree height
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. This BST-specific approach is much simpler than the general binary tree LCA algorithm (used in problem 236), which cannot rely on value ordering.

## Recognition

Look for this pattern when you have:

* A binary SEARCH tree (ordering matters) where the lowest common ancestor of two nodes must be found
* Node values can be compared directly to decide which subtree to descend into

## Keywords

* Depth-First Search
* Binary Search Tree
* Lowest Common Ancestor
* Ordering Property

## Similar Problems

* 236. Lowest Common Ancestor of a Binary Tree
* 230. Kth Smallest Element in a BST
* 98. Validate Binary Search Tree