# LeetCode 1207 - Unique Number of Occurrences

Pattern: Hash Table

Difficulty: Easy

## Idea

Build a frequency map counting how many times each number appears.

Collect all the frequency values into a set; if the set's size equals the number of distinct keys in the frequency map, every value's occurrence count is unique.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Solved cleanly on the first accepted attempt. The core trick is comparing the size of the set of frequencies against the size of the frequency map itself, rather than comparing frequencies pairwise.

## Recognition

Look for this pattern when you have:

* Need to check a uniqueness property not on the original values, but on their COUNTS
* Building a frequency map and then a set of those frequencies is a common two-level counting trick

## Keywords

* Hash Table
* Frequency Counting
* Set
* Uniqueness Check

## Similar Problems

* 217. Contains Duplicate
* 645. Set Mismatch
* 4038. Count Integers Appearing in a Single Block