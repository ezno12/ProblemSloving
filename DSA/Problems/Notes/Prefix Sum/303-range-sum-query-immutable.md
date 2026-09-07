# LeetCode 303 - Range Sum Query - Immutable

Pattern: Prefix Sum (Design)

Difficulty: Easy

## Idea

Precompute a prefix sum array once in the constructor, where prefix_sum[i] holds the sum of the first i elements.

Each sumRange(left, right) query then becomes a simple O(1) subtraction: prefix_sum[right + 1] - prefix_sum[left].

## Complexity

* Time: O(n) to build, O(1) per query
* Space: O(n) for the prefix sum array

## Mistakes

* Solved cleanly on the first accepted attempt. This is the textbook use case for prefix sums: the array is immutable, so precomputing once and answering many range queries in O(1) each is the ideal design.

## Recognition

Look for this pattern when you have:

* An immutable array with MANY repeated range-sum queries
* Need O(1) per query after O(n) preprocessing

## Keywords

* Prefix Sum
* Design
* Range Query
* Immutable Array

## Similar Problems

* 1480. Running Sum of 1d Array
* 307. Range Sum Query - Mutable
* 238. Product of Array Except Self