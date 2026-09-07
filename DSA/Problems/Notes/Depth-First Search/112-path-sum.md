# LeetCode 112 - Path Sum

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Do a DFS from the root, subtracting each node's value from the remaining targetSum as you descend.

At a leaf, the path is valid if the remaining targetSum exactly equals the leaf's value.

Otherwise, recurse into both children and return true if either path finds a match.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Edge case to double check: a completely empty tree (root is None) should return False immediately.

## Recognition

Look for this pattern when you have:

* A binary tree where a root-to-leaf sum must equal a target
* Only leaf-ending paths count, not any arbitrary path

## Keywords

* Depth-First Search
* Binary Tree
* Path Sum
* Leaf Condition

## Similar Problems

* 113. Path Sum II
* 129. Sum Root to Leaf Numbers
* 257. Binary Tree Paths