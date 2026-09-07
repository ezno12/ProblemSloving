# LeetCode 82 - Remove Duplicates from Sorted List II

Pattern: Linked List + Two Pointers

Difficulty: Medium

## Idea

Use a dummy node before head, with slow pointing to the last confirmed unique node and fast scanning ahead.

Whenever fast.next has the same value as fast, keep advancing fast through the whole run of duplicates.

If a run of duplicates was found, unlink the entire run by setting slow.next = fast.next; otherwise, advance slow normally.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. The subtlety to remember is that ALL nodes with a duplicated value must be removed, not just the extra copies.

## Recognition

Look for this pattern when you have:

* A sorted linked list
* Need to remove every node whose value is duplicated (not just keep one copy)
* Need O(1) extra space

## Keywords

* Linked List
* Two Pointers
* Dummy Node
* Duplicate Removal

## Similar Problems

* 83. Remove Duplicates from Sorted List
* 26. Remove Duplicates from Sorted Array
* 80. Remove Duplicates from Sorted Array II