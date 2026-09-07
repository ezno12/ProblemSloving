# LeetCode 153 - Find Minimum in Rotated Sorted Array

Pattern: Binary Search

Difficulty: Medium

## Idea

Use binary search comparing nums[mid] to nums[-1] (the last element).

If nums[mid] is less than or equal to the last element, the minimum must be at mid or to its left, so move right to mid. Otherwise, the minimum is strictly to the right, so move left to mid + 1.

The loop ends when left == right, which is the index of the minimum.

## Complexity

* Time: O(log n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from comparing nums[mid] against nums[left] instead of nums[-1], which behaves incorrectly for certain rotation offsets.

## Recognition

Look for this pattern when you have:

* A rotated sorted array where the minimum (pivot point) needs to be found
* Comparing against a fixed reference point (like the last element) simplifies deciding which half to search

## Keywords

* Binary Search
* Rotated Sorted Array
* Pivot Detection

## Similar Problems

* 33. Search in Rotated Sorted Array
* 154. Find Minimum in Rotated Sorted Array II
* 704. Binary Search