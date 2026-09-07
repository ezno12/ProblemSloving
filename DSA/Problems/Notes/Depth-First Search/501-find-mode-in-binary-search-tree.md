# LeetCode 501 - Find Mode in Binary Search Tree

Pattern: Depth-First Search

Difficulty: Easy

## Idea

Do a DFS over the whole tree, counting the occurrences of every value in a Counter (hash map).

After the traversal, find the maximum frequency and collect every value whose count equals that maximum.

## Complexity

* Time: O(n)
* Space: O(n) for the counter

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an early attempt that tried to exploit the BST inorder property without a hash map but mishandled ties for the mode.

## Recognition

Look for this pattern when you have:

* A tree (or BST) where the most frequent value(s) must be found
* A hash-map frequency count is the simplest correct approach, even though an O(1)-space inorder-traversal trick exists for BSTs specifically

## Keywords

* Depth-First Search
* Hash Table
* Frequency Counting
* Binary Search Tree

## Similar Problems

* 98. Validate Binary Search Tree
* 230. Kth Smallest Element in a BST
* splay/mode-tracking variants