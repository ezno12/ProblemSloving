# LeetCode 33 - Search in Rotated Sorted Array

Pattern: Binary Search

Difficulty: Medium

## Idea

Use a modified binary search. At each midpoint, first check if it equals target directly.

Then determine which half is "sorted" by comparing nums[mid] to nums[left]. If the left half is sorted and target falls within its range, search left; otherwise search right (and mirror the logic for when the right half is the sorted one).

## Complexity

* Time: O(log n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an incorrect boundary check when determining which half is sorted (off-by-one on the comparisons with nums[left] or nums[right]).

## Recognition

Look for this pattern when you have:

* An array that is sorted but has been rotated at an unknown pivot
* Need O(log n) search, which rules out a linear scan
* One half of any given midpoint split is always properly sorted

## Keywords

* Binary Search
* Rotated Sorted Array
* Pivot Detection

## Similar Problems

* 153. Find Minimum in Rotated Sorted Array
* 81. Search in Rotated Sorted Array II
* 704. Binary Search