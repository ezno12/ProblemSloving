# LeetCode 645 - Set Mismatch

Pattern: Hash Table

Difficulty: Easy

## Idea

Count the occurrences of every number using a Counter over nums.

Scan through every possible value from 1 to n: the value that appears twice is the duplicate, and the value that appears zero times is the missing one.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an off-by-one in the range checked (1 to n inclusive) or from mixing up which value is the duplicate vs which is missing.

## Recognition

Look for this pattern when you have:

* An array that should contain each number in a range exactly once, but has one duplicate and one missing value
* A frequency count directly exposes both anomalies

## Keywords

* Hash Table
* Frequency Counting
* Bit Manipulation (alternative XOR trick)
* Sorting (alternative)

## Similar Problems

* 448. Find All Numbers Disappeared in an Array
* 287. Find the Duplicate Number
* 1. Two Sum