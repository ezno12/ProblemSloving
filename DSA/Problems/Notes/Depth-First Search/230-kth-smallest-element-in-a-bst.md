# LeetCode 230 - Kth Smallest Element in a BST

Pattern: Depth-First Search (Inorder Traversal)

Difficulty: Medium

## Idea

An inorder traversal of a BST visits values in ascending order.

Do an inorder DFS while decrementing a counter (self.count) starting at k. When the counter reaches 0, the current node's value is the kth smallest, so store it and stop descending further.

## Complexity

* Time: O(h + k) in the best case, O(n) worst case
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Once self.res is set, further recursive calls should short-circuit immediately (checked at the top of dfs) to avoid unnecessary work after finding the answer.

## Recognition

Look for this pattern when you have:

* A binary search tree where the kth smallest/largest value is needed
* Inorder traversal naturally visits values in sorted order

## Keywords

* Depth-First Search
* Inorder Traversal
* Binary Search Tree
* Early Termination

## Similar Problems

* 98. Validate Binary Search Tree
* 235. Lowest Common Ancestor of a Binary Search Tree
* 501. Find Mode in Binary Search Tree