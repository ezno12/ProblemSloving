# LeetCode 4 - Median of Two Sorted Arrays

Pattern: Binary Search (intended); Brute Force (as implemented)

Difficulty: Hard

## Idea

The optimal O(log(min(n, m))) approach uses binary search on the partition point of the smaller array to split both arrays into two halves such that all left elements are <= all right elements, then reads the median directly from the four boundary elements.

The accepted solution here instead merged and sorted both arrays directly and used a median library helper, which is correct but does not meet the intended time complexity.

## Complexity

* Time: O((n + m) log(n + m)) as implemented (concatenate + sort); the optimal binary search approach is O(log(min(n, m)))
* Space: O(n + m) for the merged array

## Mistakes

* Passed on the first submission, but the solution does not use the expected binary-search partitioning technique. Revisit this problem specifically to practice binary search on an answer/partition index, since this is a classic hard-level binary search problem.

## Recognition

Look for this pattern when you have:

* Two sorted arrays where a combined statistic (median, kth element) is needed
* Need better than O(n + m) time, which rules out simple merging
* Binary search on a partition index (not on a value) is the key technique

## Keywords

* Binary Search
* Partition Search
* Divide and Conquer
* Median
* Sorted Arrays

## Similar Problems

* 88. Merge Sorted Array
* 215. Kth Largest Element in an Array
* 1533. Find the Index of the Large Integer