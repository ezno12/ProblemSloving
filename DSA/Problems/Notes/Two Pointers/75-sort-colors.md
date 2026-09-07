# LeetCode 75 - Sort Colors

Pattern: Two Pointers (intended: Dutch National Flag)

Difficulty: Medium

## Idea

The classic optimal approach uses three pointers (low, mid, high) to partition the array into 0s, 1s, and 2s in a single O(n) pass (the Dutch National Flag algorithm).

The accepted solution here instead used a simple nested-loop bubble sort, which sorts correctly but does not use the intended technique.

## Complexity

* Time: O(n^2) as implemented (bubble sort); the optimal Dutch Flag approach is O(n)
* Space: O(1)

## Mistakes

* Passed on the first submission, but the solution does not use the expected one-pass three-pointer partitioning. Revisit this problem to practice the true Dutch National Flag two/three-pointer technique instead of relying on a general sort.

## Recognition

Look for this pattern when you have:

* An array with only a small fixed number of distinct values (here 0, 1, 2)
* Need to sort in place in O(n) time and O(1) space
* Can partition the array into three regions using pointers

## Keywords

* Two Pointers
* Dutch National Flag
* In-Place Partitioning
* Counting Sort (alternative)

## Similar Problems

* 283. Move Zeroes
* 215. Kth Largest Element in an Array
* 905. Sort Array By Parity