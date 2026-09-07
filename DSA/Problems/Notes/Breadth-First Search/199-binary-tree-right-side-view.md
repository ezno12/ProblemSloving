# LeetCode 199 - Binary Tree Right Side View

Pattern: Breadth-First Search (Level Order)

Difficulty: Medium

## Idea

Do a level-order BFS with a queue. For each level, the rightmost node is whichever node is at the front of the queue when that level starts being processed (since children are pushed left then right, the front of the queue for the NEXT level's first pop corresponds to tracking queue[0] at the right moment).

Record that one value per level into the result.

## Complexity

* Time: O(n)
* Space: O(w), where w is the maximum width of the tree

## Mistakes

* Solved cleanly on the first accepted attempt. A simpler and more common approach records the LAST node processed in each level's inner loop, rather than peeking at queue[0] at the start.

## Recognition

Look for this pattern when you have:

* A binary tree where only one representative node per level is needed (leftmost or rightmost view)
* Level-order BFS naturally exposes level boundaries

## Keywords

* Breadth-First Search
* Level Order Traversal
* Binary Tree
* Rightmost Node

## Similar Problems

* 102. Binary Tree Level Order Traversal
* 103. Binary Tree Zigzag Level Order Traversal
* 107. Binary Tree Level Order Traversal II