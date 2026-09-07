# LeetCode 1423 - Maximum Points You Can Obtain from Cards

Pattern: Sliding Window (Complement Trick)

Difficulty: Medium

## Idea

Taking k cards from either end is equivalent to REMOVING a contiguous window of size (n - k) from the middle and keeping the rest.

So instead of tracking picks from both ends directly, slide a window of fixed size (n - k) across the array and find the MINIMUM sum inside that window; the answer is total sum minus that minimum window sum.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. The key insight to remember is the reframing: "maximize the sum of k cards from the ends" becomes "minimize the sum of a fixed-size window in the middle," which turns a two-pointer-from-both-ends problem into a simpler single sliding window.

## Recognition

Look for this pattern when you have:

* Need to pick items from both ends of an array to maximize/minimize a sum
* The complement (what is NOT picked) forms a contiguous block, which can be tackled with a fixed-size sliding window instead

## Keywords

* Sliding Window
* Fixed Size Window
* Complement Trick
* Prefix Sum

## Similar Problems

* 209. Minimum Size Subarray Sum
* 643. Maximum Average Subarray I
* 11. Container With Most Water