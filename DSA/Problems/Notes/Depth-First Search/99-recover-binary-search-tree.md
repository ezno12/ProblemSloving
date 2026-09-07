# LeetCode 99 - Recover Binary Search Tree

Pattern: Depth-First Search (Inorder Traversal)

Difficulty: Medium

## Idea

An inorder traversal of a valid BST visits nodes in strictly increasing order. Exactly two nodes were swapped, which creates one or two places where this order is violated.

Do an inorder DFS while tracking the previously visited node (prev). Whenever prev.val > node.val, that pair identifies a misplaced node (first, then second).

After the traversal, swap the values of the two identified nodes back.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Subtlety to remember: the two violating positions might not be adjacent to each other, so both "first" and "second" candidates must be tracked and possibly updated more than once.

## Recognition

Look for this pattern when you have:

* A binary search tree with some property broken by a small, localized fault
* Inorder traversal exposes ordering violations directly

## Keywords

* Depth-First Search
* Inorder Traversal
* Binary Search Tree
* Constraint Violation Detection

## Similar Problems

* 98. Validate Binary Search Tree
* 230. Kth Smallest Element in a BST
* 501. Find Mode in Binary Search Tree