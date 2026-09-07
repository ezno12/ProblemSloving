# LeetCode 257 - Binary Tree Paths

Pattern: Depth-First Search / Backtracking

Difficulty: Easy

## Idea

Do a DFS from the root, carrying the path built so far as a string.

At each node, append its value; if it is a leaf, record the completed path in the results list.

Otherwise, recurse into both children with the updated path.

## Complexity

* Time: O(n^2) in the worst case (string concatenation per path)
* Space: O(h) for recursion, O(n) for results

## Mistakes

* Solved cleanly on the first accepted attempt. Note that because Python strings are immutable, each recursive call naturally gets its own copy of path, so no explicit backtracking (undoing an append) is needed like it would be with a mutable list.

## Recognition

Look for this pattern when you have:

* A binary tree where every root-to-leaf path must be reported individually
* Need to build a path incrementally through recursion

## Keywords

* Depth-First Search
* Backtracking
* Binary Tree
* Path Building

## Similar Problems

* 129. Sum Root to Leaf Numbers
* 112. Path Sum
* 113. Path Sum II