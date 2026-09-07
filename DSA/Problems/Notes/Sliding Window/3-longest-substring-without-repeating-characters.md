# LeetCode 3 - Longest Substring Without Repeating Characters

Pattern: Sliding Window

Difficulty: Medium

## Idea

Use a variable-size window tracked by a start pointer, and a hash map (charMap) recording the last seen index of each character.

As end advances, if the current character was seen before AND that occurrence is inside the current window, jump start forward to just after that previous occurrence.

Update charMap with the current index and track the maximum window length (end - start + 1) seen so far.

## Complexity

* Time: O(n)
* Space: O(min(n, alphabet size))

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from moving start backward incorrectly (not using max() to prevent start from moving backward when the repeated character's last occurrence is outside the current window).

## Recognition

Look for this pattern when you have:

* Need the longest substring/subarray satisfying a "no repeats" or uniqueness constraint
* A hash map tracking last-seen positions allows jumping the window start directly instead of shrinking one step at a time

## Keywords

* Sliding Window
* Hash Table
* Variable Size Window
* Last Seen Index

## Similar Problems

* 438. Find All Anagrams in a String
* 76. Minimum Window Substring
* 904. Fruit Into Baskets