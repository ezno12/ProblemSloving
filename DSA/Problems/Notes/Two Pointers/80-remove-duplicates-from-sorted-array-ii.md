# LeetCode 80 - Remove Duplicates from Sorted Array II

Pattern: Two Pointers

Difficulty: Medium

## Idea

Since the array is sorted, allow each value to appear at most twice.

Keep a slow pointer starting at index 2 (the first two elements are always kept).

For each fast index, compare nums[fast] with nums[slow - 2]; if they differ, it is safe to keep nums[fast], so copy it to nums[slow] and advance slow.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. The key insight to internalize is comparing against slow - 2 (not slow - 1) to allow exactly two duplicates.

## Recognition

Look for this pattern when you have:

* A sorted array
* Need to keep at most k duplicates in place
* Need O(1) extra space

## Keywords

* Two Pointers
* Sorted Array
* In-Place Modification
* Duplicate Limit

## Similar Problems

* 26. Remove Duplicates from Sorted Array
* 27. Remove Element
* 283. Move Zeroes