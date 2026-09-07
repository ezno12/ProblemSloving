# LeetCode 367 - Valid Perfect Square

Pattern: Binary Search

Difficulty: Easy

## Idea

Binary search over the range [1, num] for a value mid such that mid * mid equals num.

If mid*mid is too small, move left up; if too large, move right down; if exactly equal, num is a perfect square.

## Complexity

* Time: O(log n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an off-by-one in the search bounds or from integer overflow concerns in other languages (less relevant in Python).

## Recognition

Look for this pattern when you have:

* Need to search over a numeric range for a value satisfying an equation
* The relationship (mid*mid vs num) is monotonic, allowing binary search on the answer

## Keywords

* Binary Search
* Search on Answer
* Math
* Monotonic Function

## Similar Problems

* 69. Sqrt(x)
* 633. Sum of Square Numbers
* 704. Binary Search