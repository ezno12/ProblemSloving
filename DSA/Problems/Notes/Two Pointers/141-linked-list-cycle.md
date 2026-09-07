# LeetCode 141 - Linked List Cycle

Pattern: Two Pointers (Floyd's Cycle Detection)

Difficulty: Easy

## Idea

Use a slow pointer moving one step at a time and a fast pointer moving two steps at a time.

If there is a cycle, the fast pointer will eventually lap the slow pointer and they will meet.

If the fast pointer reaches the end (None) first, there is no cycle.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from not checking fast.next before accessing fast.next.next, which can crash on odd-length cycles or short lists.

## Recognition

Look for this pattern when you have:

* A linked list that might contain a cycle
* Need to detect the cycle without extra memory (as opposed to using a hash set of visited nodes)

## Keywords

* Two Pointers
* Floyd's Cycle Finding Algorithm
* Fast/Slow Pointer
* Linked List

## Similar Problems

* 142. Linked List Cycle II
* 876. Middle of the Linked List
* 202. Happy Number