# LeetCode 61 - Rotate List

Pattern: Linked List

Difficulty: Medium

## Idea

Find the length n and the tail of the list by walking to the end.

Connect tail.next = head to make the list circular, then reduce k with k % n to avoid redundant full rotations.

Walk (n - k - 1) steps from head to find the new tail, set the new head as new_tail.next, and break the circle by setting new_tail.next = None.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail to remember: always reduce k with k % n first, otherwise large k values cause unnecessary work or wrong results.

## Recognition

Look for this pattern when you have:

* A singly linked list that needs to be rotated by k positions
* Making the list temporarily circular simplifies finding the new head/tail

## Keywords

* Linked List
* Circular Trick
* Modulo Reduction
* Pointer Rewiring

## Similar Problems

* 19. Remove Nth Node From End of List
* 206. Reverse Linked List
* 24. Swap Nodes in Pairs