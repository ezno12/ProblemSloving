# LeetCode 19 - Remove Nth Node From End of List

Pattern: Two Pointers (Fast/Slow)

Difficulty: Medium

## Idea

Use a dummy node before head so removing the head itself is not a special case.

Advance a fast pointer n + 1 steps ahead of a slow pointer.

Then move both pointers forward together until fast reaches the end (None); at that point, slow is right before the node to remove.

Unlink slow.next by pointing it to slow.next.next.

## Complexity

* Time: O(L) where L is the list length
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. The trick to remember is using a dummy node and advancing fast by n + 1 (not n) so slow lands just before the target node.

## Recognition

Look for this pattern when you have:

* A singly linked list
* Need to find a node relative to the end without knowing the length in advance
* Want a single pass instead of first counting the length then a second pass

## Keywords

* Two Pointers
* Fast/Slow Pointer
* Dummy Node
* Linked List
* Single Pass

## Similar Problems

* 876. Middle of the Linked List
* 141. Linked List Cycle
* 61. Rotate List