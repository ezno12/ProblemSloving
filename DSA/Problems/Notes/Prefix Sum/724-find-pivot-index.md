# LeetCode 724 - Find Pivot Index

Pattern: Prefix Sum (Running Sums)

Difficulty: Easy

## Idea

Track sum_left (starting at 0) and sum_right (starting as the sum of everything except the first element).

At each index, check if sum_left equals sum_right; if so, that index is the pivot. Otherwise, advance both running sums by adding/removing the appropriate element as the index moves forward.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Maintaining two running totals (instead of building a full prefix sum array) keeps this O(1) extra space rather than O(n).

## Recognition

Look for this pattern when you have:

* Need to find an index where the sum of everything to the left equals the sum of everything to the right
* Running totals updated incrementally avoid recomputing sums from scratch at every index

## Keywords

* Prefix Sum
* Running Total
* Pivot Search

## Similar Problems

* 2574. Left and Right Sum Differences
* 238. Product of Array Except Self
* 1991. Find the Middle Index in Array