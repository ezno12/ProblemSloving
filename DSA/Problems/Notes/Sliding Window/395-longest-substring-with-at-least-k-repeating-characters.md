# LeetCode 395 - Longest Substring with At Least K Repeating Characters

Pattern: Divide and Conquer (implemented) / Sliding Window (alternative)

Difficulty: Medium

## Idea

The implemented solution uses divide and conquer: within a given [start, end] range, count character frequencies; any character appearing fewer than k times cannot be part of a valid answer, so split the string at that character's positions and recurse on the pieces on either side.

Take the maximum valid length found across all recursive splits.

## Complexity

* Time: O(26 * n) roughly, since there are at most 26 possible split characters and each recursion level scans the substring
* Space: O(n) for recursion and substring slicing

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an off-by-one when computing substring boundaries after finding a disqualifying character, or from not handling the base case where the whole range already satisfies the constraint.

## Recognition

Look for this pattern when you have:

* A substring validity constraint based on character frequency counts
* An offending character can be used as a natural split point to recurse on smaller independent pieces
* An alternative sliding-window-with-fixed-unique-character-count approach also works

## Keywords

* Divide and Conquer
* Sliding Window (alternative)
* String
* Frequency Counting
* Recursive Splitting

## Similar Problems

* 3. Longest Substring Without Repeating Characters
* 904. Fruit Into Baskets
* 76. Minimum Window Substring