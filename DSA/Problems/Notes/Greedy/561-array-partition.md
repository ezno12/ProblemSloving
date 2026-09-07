# LeetCode 561 - Array Partition

Pattern: Greedy + Sorting

Difficulty: Easy

## Idea

Sort the array first. Pairing adjacent elements after sorting and always taking the smaller of each pair maximizes the total sum of minimums.

After sorting, every element at an even index (0, 2, 4, ...) is guaranteed to be the minimum of its pair, so summing every other element (nums[::2]) gives the answer directly.

## Complexity

* Time: O(n log n) for the sort
* Space: O(1) extra

## Mistakes

* Solved cleanly on the first accepted attempt. The greedy insight to remember: sorting first, then pairing adjacent elements, always maximizes the sum of per-pair minimums.

## Recognition

Look for this pattern when you have:

* Need to pair up all elements to maximize/minimize a sum of per-pair extremes
* Sorting first exposes an optimal adjacent-pairing strategy

## Keywords

* Greedy
* Sorting
* Pairing Strategy
* Counting Sort (alternative)

## Similar Problems

* 881. Boats to Save People
* 455. Assign Cookies