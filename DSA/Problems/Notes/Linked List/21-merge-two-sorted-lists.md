# LeetCode 21 - Merge Two Sorted Lists

Pattern: Linked List

Difficulty: Easy

## Idea

Use a dummy node and a curr pointer to build the merged list.

While both list1 and list2 have nodes, compare their values and attach the smaller one to curr.next, then advance that list and curr.

Once one list is exhausted, attach whatever remains of the other list directly.

## Complexity

* Time: O(n + m)
* Space: O(1) extra (reuses existing nodes)

## Mistakes

* Solved cleanly on the first accepted attempt. Remember the dummy-node trick: it avoids special-casing which list contributes the very first node.

## Recognition

Look for this pattern when you have:

* Two sorted linked lists (or arrays) that need to be merged into one sorted structure
* A dummy head simplifies building the result

## Keywords

* Linked List
* Merge
* Dummy Node
* Two Sorted Sequences

## Similar Problems

* 23. Merge k Sorted Lists
* 88. Merge Sorted Array
* 148. Sort List