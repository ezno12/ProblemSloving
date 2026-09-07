# LeetCode 107 - Binary Tree Level Order Traversal II

Pattern: Breadth-First Search (Level Order)

Difficulty: Medium

## Idea

Do a standard level-order BFS with a queue, collecting each level into its own sub-list.

The only difference from the standard level-order traversal is that the final result is reversed (or built by inserting at the front), so the leaf levels appear first and the root level appears last.

## Complexity

* Time: O(n)
* Space: O(w), where w is the maximum width of the tree

## Mistakes

* Solved cleanly on the first accepted attempt. Simplest approach: do a normal level-order BFS, then reverse the final list of levels once at the end.

## Recognition

Look for this pattern when you have:

* A binary tree that needs a bottom-up level order traversal
* A regular top-down BFS can be adapted by reversing the result at the end

## Keywords

* Breadth-First Search
* Level Order Traversal
* Binary Tree
* Bottom-Up

## Similar Problems

* 102. Binary Tree Level Order Traversal
* 103. Binary Tree Zigzag Level Order Traversal
* 199. Binary Tree Right Side View