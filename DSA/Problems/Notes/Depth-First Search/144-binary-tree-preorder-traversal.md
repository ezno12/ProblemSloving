# LeetCode 144 - Binary Tree Preorder Traversal

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Recursively append the current node's value first, then visit the left subtree, then the right subtree.

This ordering (node, left, right) is the definition of preorder traversal.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Worth practicing the iterative version with an explicit stack (append right child before left child so left is processed first) as a follow-up.

## Recognition

Look for this pattern when you have:

* A binary tree that must be visited in node-left-right order

## Keywords

* Depth-First Search
* Binary Tree
* Preorder Traversal
* Stack (iterative alternative)

## Similar Problems

* 94. Binary Tree Inorder Traversal
* 145. Binary Tree Postorder Traversal
* 102. Binary Tree Level Order Traversal