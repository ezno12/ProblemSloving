# LeetCode 203 - Remove Linked List Elements

Pattern: Linked List

Difficulty: Easy

## Idea

First strip away any leading nodes that match val by advancing head while it matches.

Then walk through the rest of the list with curr, and whenever curr.next matches val, skip over it by setting curr.next = curr.next.next; otherwise advance curr normally.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Edge case to double check: multiple consecutive matching values at the very start of the list.

## Recognition

Look for this pattern when you have:

* A singly linked list
* Need to remove all nodes matching a given value
* Head itself might need removal, which is why leading matches are handled separately

## Keywords

* Linked List
* In-Place Removal
* Head Edge Case

## Similar Problems

* 83. Remove Duplicates from Sorted List
* 82. Remove Duplicates from Sorted List II
* 237. Delete Node in a Linked List