# LeetCode 26 - Remove Duplicates from Sorted Array

Pattern: Two Pointers

Difficulty: Easy

## Idea

Since the array is sorted, duplicates are always adjacent.

Keep a slow pointer for the position of the last unique element written so far.

For every fast index, if nums[fast] differs from nums[slow], advance slow and write nums[fast] there.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. This is the simplest version of the "allow at most k duplicates" family, worth remembering as the base case for 80. Remove Duplicates from Sorted Array II.

## Recognition

Look for this pattern when you have:

* A sorted array
* Need to remove duplicates in place
* Need O(1) extra space

## Keywords

* Two Pointers
* Sorted Array
* In-Place Modification
* Deduplication

## Similar Problems

* 80. Remove Duplicates from Sorted Array II
* 27. Remove Element
* 283. Move Zeroes