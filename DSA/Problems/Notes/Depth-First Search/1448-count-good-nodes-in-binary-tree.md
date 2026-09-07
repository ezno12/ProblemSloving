# LeetCode 1448 - Count Good Nodes in Binary Tree

Pattern: Depth-First Search

Difficulty: Medium

## Idea

Do a DFS from the root, carrying along the maximum value seen on the path so far (max_so_far).

At each node, it is "good" if its value is greater than or equal to max_so_far. Update max_so_far for the recursive calls into both children and sum up the good-node counts returned from each subtree.

## Complexity

* Time: O(n)
* Space: O(h) for recursion

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail: a node counts as good if it is greater than or equal to (not strictly greater than) the max seen so far, so equal values still count.

## Recognition

Look for this pattern when you have:

* A tree where a property of a node depends on an aggregate (max/min/sum) of its ancestors
* Passing extra state down through the DFS call carries that ancestor information

## Keywords

* Depth-First Search
* Binary Tree
* Path Aggregate
* Ancestor State

## Similar Problems

* 129. Sum Root to Leaf Numbers
* 543. Diameter of Binary Tree
* 199. Binary Tree Right Side View