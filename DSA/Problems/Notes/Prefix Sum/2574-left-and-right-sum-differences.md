# LeetCode 2574 - Left and Right Sum Differences

Pattern: Prefix Sum

Difficulty: Easy

## Idea

Build a prefix sum array where prefix_sum[i] is the sum of the first i elements.

For each index i, the left sum is prefix_sum[i] and the right sum is total - prefix_sum[i+1]; the answer at that index is the absolute difference between them.

## Complexity

* Time: O(n)
* Space: O(n) for the prefix sum array

## Mistakes

* Solved cleanly on the first accepted attempt. Using Python's accumulate() function to build the prefix sum array in one line is a clean shortcut worth remembering.

## Recognition

Look for this pattern when you have:

* Need the sum of elements to the left and/or right of every index
* A single prefix sum array can answer both left-sum and right-sum queries in O(1) per index after O(n) preprocessing

## Keywords

* Prefix Sum
* Suffix Sum
* Array
* Accumulate

## Similar Problems

* 724. Find Pivot Index
* 238. Product of Array Except Self
* 1480. Running Sum of 1d Array