# LeetCode 103 - Binary Tree Zigzag Level Order Traversal

Pattern: Breadth-First Search (Level Order)

Difficulty: Medium

## Idea

Do a standard level-order BFS with a queue, collecting each level into its own sub-list.

Keep an order_index (or direction flag) that alternates each level; when the direction is reversed, reverse the collected sub-list for that level before adding it to the result.

## Complexity

* Time: O(n)
* Space: O(w), where w is the maximum width of the tree

## Mistakes

* Solved cleanly on the first accepted attempt. Simplest approach: do a normal level-order BFS and simply reverse every other level's list at the end, rather than trying to traverse in zigzag order directly.

## Recognition

Look for this pattern when you have:

* A binary tree where levels must alternate between left-to-right and right-to-left order
* A normal BFS plus a post-processing reversal handles the alternation cleanly

## Keywords

* Breadth-First Search
* Level Order Traversal
* Binary Tree
* Alternating Direction

## Similar Problems

* 102. Binary Tree Level Order Traversal
* 107. Binary Tree Level Order Traversal II
* 199. Binary Tree Right Side View