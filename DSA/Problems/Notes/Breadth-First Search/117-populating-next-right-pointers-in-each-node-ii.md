# LeetCode 117 - Populating Next Right Pointers in Each Node II

Pattern: Breadth-First Search (Level Order)

Difficulty: Medium

## Idea

Do a standard level-order BFS with a queue, processing one full level at a time.

Within each level, keep a prev pointer; when moving to the next node in the same level, set prev.next = current node before advancing prev.

The last node in each level naturally keeps its next as None.

## Complexity

* Time: O(n)
* Space: O(w), where w is the maximum width of the tree

## Mistakes

* Solved cleanly on the first accepted attempt. This works for ANY binary tree (not just perfect ones), which is what makes it a "II" variant of problem 116.

## Recognition

Look for this pattern when you have:

* A binary tree where sibling nodes at the same level need to be linked together
* Level-order BFS naturally groups nodes by level, making linking straightforward

## Keywords

* Breadth-First Search
* Level Order Traversal
* Binary Tree
* Pointer Rewiring

## Similar Problems

* 116. Populating Next Right Pointers in Each Node
* 102. Binary Tree Level Order Traversal
* 199. Binary Tree Right Side View