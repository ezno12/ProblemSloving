# LeetCode 438 - Find All Anagrams in a String

Pattern: Sliding Window (Fixed Size)

Difficulty: Medium

## Idea

Maintain a fixed-size window of length k (the length of p) sliding across s, tracking a running character count (sCount) inside the window.

As the window slides forward by one character, add the new character entering and remove the character leaving from the left (decrementing or deleting it from sCount).

Whenever sCount matches pCount exactly, the current window start is a valid anagram starting index.

## Complexity

* Time: O(n)
* Space: O(1) (bounded alphabet size for the counters)

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail: comparing two Counter objects directly for equality is a clean way to check "same character multiset" without manually comparing every key.

## Recognition

Look for this pattern when you have:

* Need to find all positions where a fixed-length substring is an anagram/permutation of another string
* A fixed-size window that slides one step at a time, updating counts incrementally instead of recomputing from scratch

## Keywords

* Sliding Window
* Fixed Size Window
* Anagram
* Character Counting

## Similar Problems

* 3. Longest Substring Without Repeating Characters
* 76. Minimum Window Substring
* 567. Permutation in String