# LeetCode 129 - Sum Root to Leaf Numbers

Pattern: Depth-First Search (Binary Tree)

Difficulty: Medium

## Idea

Do a DFS from the root, carrying along the digit path built so far as a string.

At each node, append its value to the path. When a leaf is reached (no left or right child), the path represents one full number, so store it.

After the DFS collects every root-to-leaf number, sum them all.

## Complexity

* Time: O(n)
* Space: O(h) for recursion, where h is tree height (plus O(n) to store all path strings)

## Mistakes

* Solved cleanly on the first accepted attempt. A cleaner variant carries an integer (num = num * 10 + node.val) instead of a string, and sums directly during the DFS instead of collecting strings first.

## Recognition

Look for this pattern when you have:

* A binary tree where a value must be accumulated along each root-to-leaf path
* Need to process every leaf path independently

## Keywords

* Depth-First Search
* Binary Tree
* Root-to-Leaf Path
* Path Accumulation

## Similar Problems

* 257. Binary Tree Paths
* 112. Path Sum
* 113. Path Sum II