# LeetCode 104 - Maximum Depth of Binary Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Recursively compute the depth of the left and right subtrees, and return 1 + max(left_depth, right_depth).

An empty tree (None) has depth 0, which serves as the base case.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. This is the simplest tree-depth pattern, and it is the base building block for 110. Balanced Binary Tree and 543. Diameter of Binary Tree.

## Recognition

Look for this pattern when you have:

* A binary tree where the longest root-to-leaf path length is needed

## Keywords

* Depth-First Search
* Binary Tree
* Maximum Depth
* Recursion

## Similar Problems

* 111. Minimum Depth of Binary Tree
* 110. Balanced Binary Tree
* 543. Diameter of Binary Tree