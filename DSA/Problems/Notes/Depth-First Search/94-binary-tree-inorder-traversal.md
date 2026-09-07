# LeetCode 94 - Binary Tree Inorder Traversal

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Recursively visit the left subtree first, then append the current node's value, then visit the right subtree.

This ordering (left, node, right) is the definition of inorder traversal, and for a BST it produces values in ascending order.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Worth practicing the iterative version with an explicit stack, since inorder traversal is the trickiest of the three to do iteratively.

## Recognition

Look for this pattern when you have:

* A binary tree that must be visited in left-node-right order
* Values need to come out in sorted order (if the tree is a BST)

## Keywords

* Depth-First Search
* Binary Tree
* Inorder Traversal
* Binary Search Tree

## Similar Problems

* 144. Binary Tree Preorder Traversal
* 145. Binary Tree Postorder Traversal
* 230. Kth Smallest Element in a BST