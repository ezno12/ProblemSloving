# LeetCode 338 - Counting Bits

Pattern: Bit Manipulation + Dynamic Programming

Difficulty: Easy

## Idea

For every integer from 0 to n, convert it to its binary string representation and count the number of '1' characters directly.

## Complexity

* Time: O(n log n) as implemented (converting each number to binary takes O(log n))
* Space: O(n) for the result

## Mistakes

* Solved cleanly on the first accepted attempt. A more optimal O(n) DP approach exists: ans[i] = ans[i >> 1] + (i & 1), building on previously computed results instead of recomputing bin() for every number; worth revisiting for the true O(n) solution.

## Recognition

Look for this pattern when you have:

* Need the number of set bits for every integer in a range
* A DP relation based on right-shifting (i >> 1) can reuse previously computed answers instead of recomputing from scratch

## Keywords

* Bit Manipulation
* Dynamic Programming
* Set Bit Counting

## Similar Problems

* 191. Number of 1 Bits
* 231. Power of Two
* branch-and-count variants