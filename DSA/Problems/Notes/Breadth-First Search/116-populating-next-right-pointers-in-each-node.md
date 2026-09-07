# LeetCode 116 - Populating Next Right Pointers in Each Node

Pattern: Breadth-First Search (Level Order)

Difficulty: Medium

## Idea

Do a level-order BFS with a queue, processing one level at a time.

Within each level, keep a prev pointer that links to the current node as next before moving on, so all nodes in the level get chained left to right.

## Complexity

* Time: O(n)
* Space: O(w) for the queue (though an O(1) pointer-based approach is possible since this tree is perfect)

## Mistakes

* Solved cleanly on the first accepted attempt. Since this tree is guaranteed perfect, an O(1) space solution is possible by using the next pointers already set on the level above to traverse without a queue; worth revisiting for the space-optimal version.

## Recognition

Look for this pattern when you have:

* A perfect binary tree where sibling nodes at the same level need to be linked
* Level-order BFS naturally groups nodes for linking, though the perfect-tree structure also allows an O(1) space trick

## Keywords

* Breadth-First Search
* Level Order Traversal
* Perfect Binary Tree
* Pointer Rewiring

## Similar Problems

* 117. Populating Next Right Pointers in Each Node II
* 102. Binary Tree Level Order Traversal
* 199. Binary Tree Right Side View