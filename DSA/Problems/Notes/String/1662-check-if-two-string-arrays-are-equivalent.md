# LeetCode 1662 - Check If Two String Arrays are Equivalent

Pattern: String (Direct Comparison)

Difficulty: Easy

## Idea

Join each array of string fragments into a single combined string using "".join(...), then compare the two combined strings directly for equality.

## Complexity

* Time: O(total characters)
* Space: O(total characters) for the joined strings

## Mistakes

* Solved cleanly on the first accepted attempt. Joining first and comparing once is simpler and just as efficient as trying to compare character-by-character across fragment boundaries manually.

## Recognition

Look for this pattern when you have:

* Two sequences of string fragments that represent one logical string when concatenated
* Need to check if the concatenated results are identical

## Keywords

* String
* Concatenation
* Direct Comparison

## Similar Problems

* 1929. Concatenation of Array
* 392. Is Subsequence