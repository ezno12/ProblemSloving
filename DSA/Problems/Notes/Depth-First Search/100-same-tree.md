# LeetCode 100 - Same Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Define a helper that compares two nodes p and q: both None means equal, only one None means not equal, otherwise their values must match and both the left and right subtrees must also be equal (checked recursively).

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. This is the direct building block reused (with a crossed comparison) to solve 101. Symmetric Tree.

## Recognition

Look for this pattern when you have:

* Two binary trees that must be compared node by node for structural and value equality

## Keywords

* Depth-First Search
* Binary Tree
* Structural Equality
* Recursion

## Similar Problems

* 101. Symmetric Tree
* 572. Subtree of Another Tree
* 226. Invert Binary Tree