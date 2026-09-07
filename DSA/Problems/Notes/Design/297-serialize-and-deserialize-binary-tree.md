# LeetCode 297 - Serialize and Deserialize Binary Tree

Pattern: Design + Depth-First Search

Difficulty: Hard

## Idea

For serialization, do a preorder DFS: append the current node's value to a list, using a sentinel string "x" to represent None/missing children, then recurse into left and right.

For deserialization, reverse the process: consume the encoded values in the same preorder order, rebuilding None for sentinels and reconstructing each node with its left and right children recursively.

## Complexity

* Time: O(n) for both serialize and deserialize
* Space: O(n) for the encoded representation and recursion stack

## Mistakes

* Solved cleanly on the first accepted attempt. The key design decision is using preorder traversal with an explicit sentinel for null nodes, which makes deserialization unambiguous without needing extra structural information.

## Recognition

Look for this pattern when you have:

* Need to convert a tree structure to a string (and back) while preserving exact structure
* A single traversal order with explicit null markers avoids ambiguity during reconstruction

## Keywords

* Design
* Depth-First Search
* Serialization
* Binary Tree
* Sentinel Value

## Similar Problems

* 449. Serialize and Deserialize BST
* 428. Serialize and Deserialize N-ary Tree
* 105. Construct Binary Tree from Preorder and Inorder Traversal