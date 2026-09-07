# LeetCode 101 - Symmetric Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Define a helper that compares two nodes p and q for mirror symmetry: both None is symmetric, only one None is not, otherwise their values must match and p.left must mirror q.right while p.right mirrors q.left.

Call this helper on (root.left, root.right).

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail to remember: compare p.left against q.right (crossed), not p.left against q.left, since the check is for mirror symmetry.

## Recognition

Look for this pattern when you have:

* A binary tree that must be checked for mirror symmetry around its center
* Two subtrees need to be compared against each other in a crossed (mirrored) fashion

## Keywords

* Depth-First Search
* Binary Tree
* Mirror Comparison
* Recursion

## Similar Problems

* 100. Same Tree
* 226. Invert Binary Tree
* 951. Flip Equivalent Binary Trees