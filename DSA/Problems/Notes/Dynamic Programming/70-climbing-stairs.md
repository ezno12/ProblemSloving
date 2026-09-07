# LeetCode 70 - Climbing Stairs

Pattern: Dynamic Programming (Fibonacci-style)

Difficulty: Easy

## Idea

The number of ways to reach step n is the sum of the ways to reach step n-1 and step n-2 (since you can take a 1-step or 2-step move from either).

Iterate from step 3 to n, keeping only the previous two values (pre and curr) instead of a full array, updating them each step.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. This is the classic Fibonacci-recurrence DP, reduced from O(n) space to O(1) by keeping only the last two values.

## Recognition

Look for this pattern when you have:

* Counting the number of ways to reach a target using a small fixed set of step sizes
* The recurrence for step n depends only on a small constant number of previous steps

## Keywords

* Dynamic Programming
* Fibonacci Sequence
* Space Optimization
* Memoization

## Similar Problems

* 91. Decode Ways
* 746. Min Cost Climbing Stairs
* 509. Fibonacci Number