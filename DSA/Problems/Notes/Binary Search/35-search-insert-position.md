# LeetCode 35 - Search Insert Position

Pattern: Binary Search

Difficulty: Easy

## Idea

Binary search over the sorted array; if the target is found, return its index directly.

If not found, track the position (index) where the loop's low boundary ends up when nums[mid] < target, since that marks where the target would be inserted to keep the array sorted.

## Complexity

* Time: O(log n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. A cleaner version tracks left as the final answer directly (since after the loop, left is always the correct insert position), instead of a separate index variable.

## Recognition

Look for this pattern when you have:

* A sorted array where the target may or may not be present
* Need the position where it is, or where it would be inserted

## Keywords

* Binary Search
* Insert Position
* Sorted Array
* Boundary Search

## Similar Problems

* 704. Binary Search
* 34. Find First and Last Position of Element in Sorted Array
* 744. Find Smallest Letter Greater Than Target