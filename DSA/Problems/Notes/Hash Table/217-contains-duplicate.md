# LeetCode 217 - Contains Duplicate

Pattern: Hash Table

Difficulty: Easy

## Idea

Convert the array to a set, which automatically removes duplicates.

If the set's length is smaller than the original array's length, at least one duplicate existed.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Solved cleanly on the first accepted attempt. This is the simplest possible use of a hash set for deduplication; sorting first is an O(n log n) alternative with O(1) extra space.

## Recognition

Look for this pattern when you have:

* Need a quick existence/duplicate check across all elements
* A set naturally deduplicates, so comparing sizes answers the question directly

## Keywords

* Hash Table
* Set
* Deduplication
* Sorting (alternative)

## Similar Problems

* 1207. Unique Number of Occurrences
* 645. Set Mismatch
* 1. Two Sum