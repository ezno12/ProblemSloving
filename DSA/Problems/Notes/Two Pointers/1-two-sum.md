# LeetCode 1 - Two Sum

Pattern: Hash Table (contrast with Two Pointers)

Difficulty: Easy

## Idea

Iterate through the array once, keeping a hash map of value -> index seen so far.

For each number, compute its complement (target - num) and check if the complement already exists in the map.

If it does, return the two indices. Otherwise, store the current number and its index in the map.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from checking the map before inserting the current number, or from an edge case where the same value appears twice.

## Recognition

Look for this pattern when you have:

* An unsorted array
* Need to find a pair (or complement) satisfying a sum condition
* Need O(n) time, and the array is not sorted (so two pointers do not directly apply)

## Keywords

* Hash Table
* Complement
* One Pass
* Index Lookup
* Pair Sum

## Similar Problems

* 167. Two Sum II - Input Array Is Sorted
* 15. 3Sum
* 18. 4Sum
* 1679. Max Number of K-Sum Pairs