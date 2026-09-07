# LeetCode 876 - Middle of the Linked List

Pattern: Two Pointers (Fast/Slow)

Difficulty: Easy

## Idea

Use a slow pointer that moves one step at a time and a fast pointer that moves two steps at a time.

When fast reaches the end of the list (or None), slow is exactly at the middle.

If the list has an even length, this naturally lands on the second middle node.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Edge case to double check: an empty list, and lists of length 1 or 2.

## Recognition

Look for this pattern when you have:

* A singly linked list with unknown length
* Need to find the middle (or a fractional position) in one pass
* Cannot easily index into the structure like an array

## Keywords

* Two Pointers
* Fast/Slow Pointer
* Linked List
* Single Pass

## Similar Problems

* 19. Remove Nth Node From End of List
* 141. Linked List Cycle
* 234. Palindrome Linked List