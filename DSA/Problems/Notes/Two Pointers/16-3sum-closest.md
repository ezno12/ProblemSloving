# LeetCode 16 - 3Sum Closest

Pattern: Two Pointers

Difficulty: Medium

## Idea

Sort the array. Fix the first number with an outer loop, then use two pointers (left, right) over the rest of the array to find the pair that brings the three-sum closest to the target.

Track the closest sum found so far, updating it whenever a smaller absolute difference from the target is found.

Move left up if the current sum is below target, or right down if it is above.

## Complexity

* Time: O(n^2)
* Space: O(1) extra

## Mistakes

* Solved cleanly on the first accepted attempt. The tricky part to remember is updating closest_sum by comparing absolute differences, not the raw sums.

## Recognition

Look for this pattern when you have:

* Need the best (closest) sum of three numbers to a target
* Sorting plus fixing one element reduces it to a two-pointer two-sum search

## Keywords

* Two Pointers
* Sorting
* Fix One, Search Two
* Closest Sum

## Similar Problems

* 15. 3Sum
* 18. 4Sum
* 611. Valid Triangle Number