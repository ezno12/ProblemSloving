# LeetCode 611 - Valid Triangle Number

Pattern: Two Pointers

Difficulty: Medium

## Idea

Sort the array first. Fix the largest side at index i and move it from right to left.

For each fixed largest side, use two pointers left and right within the remaining prefix [0, i-1].

If nums[left] + nums[right] > nums[i], then every pair from left up to right - 1 paired with right also forms a valid triangle, so add (right - left) to the count and decrease right.

Otherwise, increase left since the sum is too small.

## Complexity

* Time: O(n^2) after sorting
* Space: O(1) extra

## Mistakes

* Solved cleanly on the first accepted attempt. Key insight: fixing the largest side and counting all valid (left, right) pairs at once (instead of checking every triple individually) avoids an O(n^3) brute force.

## Recognition

Look for this pattern when you have:

* Need to count triples satisfying a sum/inequality condition
* Sorting exposes a way to fix one element and two-pointer the rest
* Can count multiple valid pairs at once instead of one at a time

## Keywords

* Two Pointers
* Sorting
* Triangle Inequality
* Counting Triples

## Similar Problems

* 15. 3Sum
* 16. 3Sum Closest
* 18. 4Sum