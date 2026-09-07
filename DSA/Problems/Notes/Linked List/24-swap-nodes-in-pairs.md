# LeetCode 24 - Swap Nodes in Pairs

Pattern: Linked List + Recursion

Difficulty: Medium

## Idea

Recursively swap each pair of nodes.

Base case: if head or head.next is None, there is nothing to swap, so return head as is.

Recursive case: recurse on head.next.next first to get the rest of the list already swapped, then make head.next the new head of this pair, point it to head, and point head to the recursively processed rest.

## Complexity

* Time: O(n)
* Space: O(n) due to recursion stack

## Mistakes

* Solved cleanly on the first accepted attempt. Worth remembering: this same pairwise-swap idea generalizes to k-group reversal problems like 25. Reverse Nodes in k-Group.

## Recognition

Look for this pattern when you have:

* A singly linked list where nodes must be rearranged in fixed-size groups
* Recursion naturally expresses "process the rest, then fix up the current group"

## Keywords

* Linked List
* Recursion
* Pairwise Swap
* Pointer Rewiring

## Similar Problems

* 25. Reverse Nodes in k-Group
* 206. Reverse Linked List
* 61. Rotate List