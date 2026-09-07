# LeetCode 1480 - Running Sum of 1d Array

Pattern: Prefix Sum

Difficulty: Easy

## Idea

Keep a running total (temp_num) while iterating through the array once, adding the current element to it and overwriting the array in place with that running total.

## Complexity

* Time: O(n)
* Space: O(1) extra (modifies in place)

## Mistakes

* Solved cleanly on the first accepted attempt. This is the most basic prefix sum problem, a direct building block for problems like 724 and 238.

## Recognition

Look for this pattern when you have:

* Need a running/cumulative sum of an array
* The simplest possible prefix sum construction

## Keywords

* Prefix Sum
* Running Total
* In-Place Modification

## Similar Problems

* 724. Find Pivot Index
* 2574. Left and Right Sum Differences
* 303. Range Sum Query - Immutable