# LeetCode 485 - Max Consecutive Ones

Pattern: Array (Running Window)

Difficulty: Easy

## Idea

Track a left boundary marking the start of the current run of 1s.

Scan through the array; whenever a 0 is found, reset left to just after that position (right + 1). Otherwise, update the maximum run length using (right - left + 1).

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. This is essentially a simplified sliding window: instead of shrinking gradually, the window start jumps directly past any disqualifying zero.

## Recognition

Look for this pattern when you have:

* Need the longest run of consecutive elements satisfying a simple condition
* A single running boundary (reset on failure) is simpler than a full two-pointer shrink

## Keywords

* Array
* Running Window
* Consecutive Run Tracking

## Similar Problems

* 1004. Max Consecutive Ones III
* 561. Array Partition
* 209. Minimum Size Subarray Sum