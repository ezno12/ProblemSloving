# LeetCode 145 - Binary Tree Postorder Traversal

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Recursively visit the left subtree, then the right subtree, and only then append the current node's value.

This ordering (left, right, node) is the definition of postorder traversal.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Worth practicing the iterative version with an explicit stack as a follow-up, since interviewers often ask for both.

## Recognition

Look for this pattern when you have:

* A binary tree that must be visited in left-right-node order
* Simple recursive DFS directly expresses the traversal order

## Keywords

* Depth-First Search
* Binary Tree
* Postorder Traversal

## Similar Problems

* 94. Binary Tree Inorder Traversal
* 144. Binary Tree Preorder Traversal
* 102. Binary Tree Level Order Traversal