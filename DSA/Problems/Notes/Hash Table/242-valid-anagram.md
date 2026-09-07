# LeetCode 242 - Valid Anagram

Pattern: Hash Table

Difficulty: Easy

## Idea

First check that both strings have equal length (a quick disqualifying check).

Then build a character frequency Counter for each string and compare them directly; two strings are anagrams if and only if their character counts are identical.

## Complexity

* Time: O(n)
* Space: O(1) (bounded alphabet size)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from comparing sorted strings inconsistently or missing the length check as an early exit, though the Counter-based approach here is already fairly robust.

## Recognition

Look for this pattern when you have:

* Need to check if two strings are permutations/anagrams of each other
* A character frequency count comparison (or sorting) directly answers this

## Keywords

* Hash Table
* Frequency Counting
* Anagram
* Sorting (alternative)

## Similar Problems

* 49. Group Anagrams
* 438. Find All Anagrams in a String
* 1. Two Sum