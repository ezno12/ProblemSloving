# LeetCode 3718 - Smallest Missing Multiple of K

Pattern: Math

Difficulty: Easy

## Idea

Starting from i = 1, repeatedly check whether k * i is present in nums.

The first multiple of k that is NOT found in nums is the answer.

## Complexity

* Time: O(answer / k * n) in the worst case, since each membership check against a list is O(n)
* Space: O(1) extra (or O(n) if nums is converted to a set for faster lookup, which would be a good optimization)

## Mistakes

* Solved cleanly on the first accepted attempt. A performance improvement worth remembering: converting nums to a set first would make each "in nums" check O(1) instead of O(n).

## Recognition

Look for this pattern when you have:

* Need the smallest positive multiple of a number not present in a collection
* A simple incremental search works when the answer is expected to be small

## Keywords

* Math
* Multiples
* Membership Check
* Hash Table (optimization)

## Similar Problems

* 268. Missing Number
* 1. Two Sum
* 645. Set Mismatch