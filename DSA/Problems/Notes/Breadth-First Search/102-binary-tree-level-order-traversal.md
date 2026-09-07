# LeetCode 102 - Binary Tree Level Order Traversal

Pattern: Breadth-First Search (Level Order)

Difficulty: Medium

## Idea

Use a queue starting with the root. While the queue is not empty, record its current size n (the number of nodes in this level), then pop exactly n nodes, collecting their values and pushing their children for the next level.

Append each level's collected values as one sub-list in the result.

## Complexity

* Time: O(n)
* Space: O(w), where w is the maximum width of the tree

## Mistakes

* Solved cleanly on the first accepted attempt. This is the foundational BFS pattern that many other tree problems (zigzag, right side view, bottom-up order) build directly on top of.

## Recognition

Look for this pattern when you have:

* A binary tree where nodes must be grouped and processed level by level
* Snapshotting the queue's length at the start of each level is the key trick to separate levels cleanly

## Keywords

* Breadth-First Search
* Level Order Traversal
* Binary Tree
* Queue

## Similar Problems

* 103. Binary Tree Zigzag Level Order Traversal
* 107. Binary Tree Level Order Traversal II
* 199. Binary Tree Right Side View