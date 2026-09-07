# LeetCode 125 - Valid Palindrome

Pattern: Two Pointers

Difficulty: Easy

## Idea

Use two pointers, one starting at the left and one at the right of the string.

Skip any character that is not alphanumeric by advancing the corresponding pointer.

Compare the lowercase version of both characters; if they differ, the string is not a palindrome.

Move both pointers toward the center until they meet.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from forgetting to skip non-alphanumeric characters or from comparing case-sensitively before lowering both characters.

## Recognition

Look for this pattern when you have:

* A string (or array) that should be checked from both ends inward
* A palindrome-style symmetry check
* Need to ignore certain characters while comparing

## Keywords

* Two Pointers
* Palindrome
* Alphanumeric Filtering
* Case Insensitive Comparison

## Similar Problems

* 167. Two Sum II - Input Array Is Sorted
* 680. Valid Palindrome II
* 5. Longest Palindromic Substring