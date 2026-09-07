# LeetCode 91 - Decode Ways

Pattern: Dynamic Programming (Top-Down Memoization)

Difficulty: Medium

## Idea

Use recursion with memoization: dfs(i) is the number of ways to decode the substring starting at index i.

If s[i] is "0", there is no valid decoding from here, so return 0. Otherwise, always count decoding just one digit (dfs(i+1)), and additionally count decoding two digits together if that two-digit number is between 10 and 26 (dfs(i+2)).

## Complexity

* Time: O(n)
* Space: O(n) for memoization and recursion stack

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from mishandling leading zeros (a digit "0" cannot stand alone or start a two-digit group starting with 0) or an off-by-one in the two-digit range check.

## Recognition

Look for this pattern when you have:

* A string of digits that must be decoded/partitioned using a small set of valid group sizes (here 1 or 2 digits)
* Counting the number of ways naturally leads to a Fibonacci-like recurrence with memoization

## Keywords

* Dynamic Programming
* Memoization
* String Partitioning
* Recursion

## Similar Problems

* 70. Climbing Stairs
* 139. Word Break
* 639. Decode Ways II