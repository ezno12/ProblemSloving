# LeetCode 283 - Move Zeroes

Pattern: Two Pointers

Difficulty: Easy

## Idea

Keep a pointer (LastNoZeroIndex) marking where the next non-zero element should go.

Iterate through the array; whenever a non-zero element is found, swap it into the LastNoZeroIndex position and advance that pointer.

This preserves the relative order of non-zero elements while pushing zeros to the end.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from copying values instead of swapping, which can duplicate elements instead of truly moving the zero.

## Recognition

Look for this pattern when you have:

* Need to partition an array in place based on a condition (zero vs non-zero)
* Order of the "kept" elements must be preserved
* Need O(1) extra space

## Keywords

* Two Pointers
* In-Place Swap
* Array Partitioning
* Stable Order

## Similar Problems

* 27. Remove Element
* 26. Remove Duplicates from Sorted Array
* 75. Sort Colors