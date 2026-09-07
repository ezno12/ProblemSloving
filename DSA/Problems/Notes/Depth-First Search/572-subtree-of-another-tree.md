# LeetCode 572 - Subtree of Another Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Reuse a "same tree" helper (isSameTree) that checks two trees for exact structural and value equality.

Then do a DFS over the main tree: at every node, check if the subtree rooted there is identical to subRoot using isSameTree; if not, recurse into the left and right children to keep searching.

## Complexity

* Time: O(n * m) in the worst case, where n and m are the sizes of the two trees
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. This combines two DFS routines: one to compare trees for equality, another to search every node as a potential match root.

## Recognition

Look for this pattern when you have:

* Need to check if one tree structure appears anywhere within another tree
* A helper for exact tree equality can be reused at every candidate root

## Keywords

* Depth-First Search
* Binary Tree
* Tree Equality
* Subtree Search

## Similar Problems

* 100. Same Tree
* 226. Invert Binary Tree
* 951. Flip Equivalent Binary Trees