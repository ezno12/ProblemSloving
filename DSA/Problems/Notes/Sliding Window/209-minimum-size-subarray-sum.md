# LeetCode 209 - Minimum Size Subarray Sum

Pattern: Sliding Window

Difficulty: Medium

## Idea

Use a variable-size window with a running sum (state).

Expand the window by moving end forward and adding nums[end] to state. Whenever state meets or exceeds target, record the window length and shrink from start (subtracting nums[start] from state) to try to find an even smaller valid window.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail: the shrink step happens in a while loop (not just an if), so multiple elements can be removed from the left in a single iteration if the sum stays above target.

## Recognition

Look for this pattern when you have:

* Need the SHORTEST subarray meeting a sum (or other monotonic) condition
* All values are non-negative, so growing the window only increases the sum and shrinking only decreases it

## Keywords

* Sliding Window
* Variable Size Window
* Prefix Sum (alternative with binary search)
* Minimum Length Subarray

## Similar Problems

* 1423. Maximum Points You Can Obtain from Cards
* 3. Longest Substring Without Repeating Characters
* 76. Minimum Window Substring