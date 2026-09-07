# LeetCode 4038 - Count Integers Appearing in a Single Block

Pattern: Hash Table

Difficulty: Easy

## Idea

For every number, track the first index it appeared (l), the last index it appeared (r), and how many times it occurred (occ), stored in a dictionary keyed by the number's value.

A number forms a single contiguous "block" if the span between its first and last occurrence (r - l + 1) exactly equals its occurrence count, meaning there are no other values interrupting its run.

## Complexity

* Time: O(n)
* Space: O(distinct values)

## Mistakes

* Solved cleanly on the first accepted attempt. The key insight is that "appearing in a single block" is equivalent to "the occurrence count matches the span between first and last occurrence."

## Recognition

Look for this pattern when you have:

* Need to determine if all occurrences of a value are contiguous
* Tracking first/last index plus a count per value in a hash map captures exactly what is needed

## Keywords

* Hash Table
* First/Last Occurrence Tracking
* Contiguity Check

## Similar Problems

* 645. Set Mismatch
* 1207. Unique Number of Occurrences
* 217. Contains Duplicate