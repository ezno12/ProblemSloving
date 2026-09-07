# LeetCode 98 - Validate Binary Search Tree

Pattern: Depth-First Search (Inorder Traversal)

Difficulty: Medium

## Idea

Do an inorder DFS traversal, which visits nodes in ascending order for a valid BST.

Keep track of the previously visited value; if the current node's value is not strictly greater than the previous one, the tree is not a valid BST.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from checking only the immediate parent-child relationship instead of the full inorder ordering, which misses violations from ancestors further up the tree.

## Recognition

Look for this pattern when you have:

* A binary search tree that needs a global ordering property verified
* Inorder traversal naturally exposes whether values are strictly increasing

## Keywords

* Depth-First Search
* Inorder Traversal
* Binary Search Tree
* Global Constraint Checking

## Similar Problems

* 99. Recover Binary Search Tree
* 230. Kth Smallest Element in a BST
* 700. Search in a Binary Search Tree