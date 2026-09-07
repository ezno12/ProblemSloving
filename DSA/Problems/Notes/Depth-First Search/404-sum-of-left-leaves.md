# LeetCode 404 - Sum of Left Leaves

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Do a DFS from the root. At each node, check if its left child exists and is itself a leaf (no children); if so, add that left child's value to the running total.

Recurse into both children and sum the contributions from the whole subtree.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail to remember: a node only counts if it is specifically a LEFT child AND a leaf; right leaves must be excluded.

## Recognition

Look for this pattern when you have:

* A binary tree where a value must be conditionally summed based on a node's position (left vs right) and role (leaf vs internal)

## Keywords

* Depth-First Search
* Binary Tree
* Conditional Accumulation
* Leaf Detection

## Similar Problems

* 129. Sum Root to Leaf Numbers
* 257. Binary Tree Paths
* 112. Path Sum