# LeetCode 27 - Remove Element

Pattern: Two Pointers

Difficulty: Easy

## Idea

Use a slow pointer that marks the position where the next kept element should be written.

Iterate with a fast pointer over every element; whenever the current element is not equal to val, copy it to the slow position and advance slow.

At the end, slow is the count of elements that are not equal to val.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Main risk area is forgetting that order does not need to be preserved, which allows this simple overwrite-in-place technique.

## Recognition

Look for this pattern when you have:

* Need to remove elements matching a condition in place
* Order of the remaining elements does not matter (or only order of kept elements matters)
* Need O(1) extra space

## Keywords

* Two Pointers
* In-Place Modification
* Slow/Fast Pointer
* Array Compaction

## Similar Problems

* 26. Remove Duplicates from Sorted Array
* 80. Remove Duplicates from Sorted Array II
* 283. Move Zeroes