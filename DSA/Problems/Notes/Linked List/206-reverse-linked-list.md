# LeetCode 206 - Reverse Linked List

Pattern: Linked List

Difficulty: Easy

## Idea

Use a dummy node whose next pointer will always point to the already-reversed portion of the list.

For each original node, save its next node, then insert the current node right after dummy (making it the new front of the reversed section), and move on to the saved next node.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. The more common iterative pattern uses a plain prev/curr/next trio without a dummy node; both achieve the same in-place reversal.

## Recognition

Look for this pattern when you have:

* A singly linked list that needs to be reversed in place
* Need O(1) extra space (as opposed to O(n) with a recursive/stack approach)

## Keywords

* Linked List
* In-Place Reversal
* Pointer Rewiring

## Similar Problems

* 92. Reverse Linked List II
* 25. Reverse Nodes in k-Group
* 24. Swap Nodes in Pairs