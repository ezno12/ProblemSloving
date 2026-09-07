# LeetCode 1679 - Max Number of K-Sum Pairs

Pattern: Two Pointers

Difficulty: Medium

## Idea

Sort the array first.

Use two pointers, left at the start and right at the end.

If nums[left] + nums[right] equals k, count a pair and move both pointers inward.

If the sum is too large, move right left; if too small, move left right.

## Complexity

* Time: O(n log n) for the sort
* Space: O(1) extra

## Mistakes

* Solved cleanly on the first accepted attempt. This is a direct variant of the sorted two-sum pattern, just counting pairs instead of returning indices.

## Recognition

Look for this pattern when you have:

* Need to count/find pairs summing to a target
* Sorting first turns the problem into the classic two-pointer sum pattern

## Keywords

* Two Pointers
* Sorting
* Pair Sum
* Counting

## Similar Problems

* 167. Two Sum II - Input Array Is Sorted
* 1. Two Sum
* 15. 3Sum