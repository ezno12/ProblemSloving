# LeetCode 704 - Binary Search

Pattern: Binary Search

Difficulty: Easy

## Idea

Maintain a left and right boundary over the sorted array.

At each step, check the midpoint; if it equals the target, return it. If it is greater than the target, move right to mid - 1; if smaller, move left to mid + 1.

Stop when left and right cross, meaning the target is not present.

## Complexity

* Time: O(log n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. This is the textbook binary search template that all other binary-search-on-array problems build on.

## Recognition

Look for this pattern when you have:

* A sorted array
* Need an exact value lookup in O(log n) time

## Keywords

* Binary Search
* Sorted Array
* Divide and Conquer

## Similar Problems

* 35. Search Insert Position
* 744. Find Smallest Letter Greater Than Target
* 33. Search in Rotated Sorted Array