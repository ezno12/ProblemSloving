# LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points

Pattern: Linked List Traversal

Difficulty: Medium

## Idea

Walk the list with prev, curr, and curr.next to detect "critical points": local maxima or minima.

Track the index of the first critical point found and the index of the previous critical point.

The maximum distance is simply (last critical index - first critical index). The minimum distance is the smallest gap between two consecutive critical points, updated as you go.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from mishandling the case where fewer than two critical points exist (should return [-1, -1]).

## Recognition

Look for this pattern when you have:

* A singly linked list that must be scanned once to detect local pattern changes (peaks/valleys)
* Need both a running minimum gap and an overall maximum gap in a single pass

## Keywords

* Linked List
* Single Pass
* Local Maxima/Minima
* Distance Tracking

## Similar Problems

* 876. Middle of the Linked List
* 141. Linked List Cycle
* 82. Remove Duplicates from Sorted List II