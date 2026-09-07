# LeetCode 1991 - Find the Middle Index in Array

Pattern: Prefix Sum (Running Sums)

Difficulty: Easy

## Idea

Track the total sum of the whole array and a running left_sum while scanning left to right.

At each index, the implied right sum is total_sum - left_sum - nums[i] (everything except the left part and the current element); if that equals left_sum, this index is the middle index.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. This is essentially the same running-sum technique as 724. Find Pivot Index, just phrased slightly differently (excluding the current element from both sides explicitly).

## Recognition

Look for this pattern when you have:

* Need an index where the sum to the left equals the sum to the right (excluding the current element)
* A single running total avoids recomputation at every index

## Keywords

* Prefix Sum
* Running Total
* Pivot Search

## Similar Problems

* 724. Find Pivot Index
* 2574. Left and Right Sum Differences
* 238. Product of Array Except Self