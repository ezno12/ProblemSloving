# LeetCode 559 - Maximum Depth of N-ary Tree

Pattern: Breadth-First Search (Level Order)

Difficulty: Easy

## Idea

Do a level-order BFS with a queue. For every level processed, increment a level counter.

At each step, pop all nodes currently in the queue (one full level) and push all of their children for the next round.

The final level counter is the maximum depth.

## Complexity

* Time: O(n)
* Space: O(w), where w is the maximum width of the tree

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an off-by-one error in when the level counter is incremented relative to processing the root level.

## Recognition

Look for this pattern when you have:

* A tree with an arbitrary number of children per node (not just binary)
* Need the maximum depth/height, which BFS level-counting handles naturally

## Keywords

* Breadth-First Search
* N-ary Tree
* Level Order Traversal
* Depth Calculation

## Similar Problems

* 104. Maximum Depth of Binary Tree
* 111. Minimum Depth of Binary Tree
* 429. N-ary Tree Level Order Traversal