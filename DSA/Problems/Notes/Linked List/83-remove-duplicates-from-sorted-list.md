# LeetCode 83 - Remove Duplicates from Sorted List

Pattern: Linked List

Difficulty: Easy

## Idea

Since the list is sorted, duplicates are always adjacent.

Walk through the list with curr; if curr.val equals curr.next.val, skip the duplicate by setting curr.next = curr.next.next (without advancing curr, so the new curr.next can be checked too).

Otherwise, advance curr normally.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. This is the simplest version of the "remove duplicates in a sorted list" family, the base case for 82's "remove all duplicated values" variant.

## Recognition

Look for this pattern when you have:

* A sorted linked list
* Need to keep only one copy of each value
* Need O(1) extra space

## Keywords

* Linked List
* Sorted List
* In-Place Deduplication

## Similar Problems

* 82. Remove Duplicates from Sorted List II
* 26. Remove Duplicates from Sorted Array
* 203. Remove Linked List Elements