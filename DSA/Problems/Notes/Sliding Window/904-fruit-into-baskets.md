# LeetCode 904 - Fruit Into Baskets

Pattern: Sliding Window

Difficulty: Medium

## Idea

This is equivalent to finding the longest subarray containing at most 2 distinct values.

Use a variable-size window with a hash map (state) counting occurrences of each fruit type inside the window.

Whenever the window contains more than 2 distinct fruit types, shrink from the left (decrementing counts and removing zero-count entries) until only 2 types remain, then update the maximum window length.

## Complexity

* Time: O(n)
* Space: O(1) (at most 3 distinct types are ever tracked at once)

## Mistakes

* Solved cleanly on the first accepted attempt. Recognizing that "two baskets, one fruit type each" translates directly into "longest subarray with at most 2 distinct values" is the key reframing for this problem.

## Recognition

Look for this pattern when you have:

* Need the longest subarray/substring with at most k distinct values
* A hash map counting frequencies inside the window, shrinking whenever the distinct-count constraint is violated

## Keywords

* Sliding Window
* Hash Table
* At Most K Distinct
* Variable Size Window

## Similar Problems

* 3. Longest Substring Without Repeating Characters
* 159. Longest Substring with At Most Two Distinct Characters
* 340. Longest Substring with At Most K Distinct Characters