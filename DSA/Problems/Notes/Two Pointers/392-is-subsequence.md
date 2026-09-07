# LeetCode 392 - Is Subsequence

Pattern: Two Pointers

Difficulty: Easy

## Idea

Use one pointer for the shorter string s and iterate through the longer string t.

Whenever the current character of t matches the current character of s, advance the s pointer.

If the s pointer reaches the end of s, every character was matched in order, so s is a subsequence of t.

## Complexity

* Time: O(len(t))
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an off-by-one bound when checking subIndex against len(s) - 1 instead of len(s), which can skip matching the last character.

## Recognition

Look for this pattern when you have:

* Two strings where one must appear as an ordered (not necessarily contiguous) subsequence of the other
* Need a single pass over the longer string

## Keywords

* Two Pointers
* Subsequence
* String Matching
* Greedy Matching

## Similar Problems

* 727. Minimum Window Subsequence
* 1143. Longest Common Subsequence
* 115. Distinct Subsequences