# LeetCode 633 - Sum of Square Numbers

Pattern: Two Pointers

Difficulty: Medium

## Idea

Search for two non-negative integers a and b such that a*a + b*b == c.

Start left at 0 and right at floor(sqrt(c)) (the code computes this bound with i = int(c**0.5)).

If the sum of squares equals c, return true. If it is smaller, increase the left value; if larger, decrease the right value.

This works because the sum of squares changes monotonically as either pointer moves, just like a sorted-array two-sum problem.

## Complexity

* Time: O(sqrt(c))
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an off-by-one error in the search bound (using sqrt(c) incorrectly) or from not handling the perfect square case separately.

## Recognition

Look for this pattern when you have:

* Need to find two numbers satisfying a sum-like condition (here, a sum of squares)
* The search space can be framed as a monotonic range that shrinks from both ends

## Keywords

* Two Pointers
* Binary Search (bound)
* Math
* Monotonic Property

## Similar Problems

* 167. Two Sum II - Input Array Is Sorted
* 367. Valid Perfect Square
* 1. Two Sum