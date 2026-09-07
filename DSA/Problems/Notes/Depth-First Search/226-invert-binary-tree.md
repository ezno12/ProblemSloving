# LeetCode 226 - Invert Binary Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Recursively build a new tree where the left and right children are swapped at every level.

Return a new TreeNode with the same value, but with invertTree(root.right) as the new left child and invertTree(root.left) as the new right child.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. The implemented version builds new nodes rather than mutating in place; both approaches are valid, but mutating root.left/root.right directly avoids extra allocations.

## Recognition

Look for this pattern when you have:

* A binary tree that must be mirrored/flipped
* Left and right children need to be swapped recursively at every node

## Keywords

* Depth-First Search
* Binary Tree
* Mirror
* Recursion

## Similar Problems

* 101. Symmetric Tree
* 100. Same Tree
* 951. Flip Equivalent Binary Trees