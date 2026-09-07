# LeetCode 238 - Product of Array Except Self

Pattern: Prefix Sum (Prefix/Suffix Product)

Difficulty: Medium

## Idea

Do two passes without using division. In the first pass (left to right), store the running product of all elements to the LEFT of each index into the result array.

In the second pass (right to left), multiply each result entry by the running product of all elements to the RIGHT of that index.

## Complexity

* Time: O(n)
* Space: O(1) extra (result array itself is required output)

## Mistakes

* Solved cleanly on the first accepted attempt. The key constraint driving this approach is that division is disallowed (or unsafe with zeros), so prefix and suffix products computed in two passes replace it.

## Recognition

Look for this pattern when you have:

* Need a value derived from "everything except the current element"
* Division is unsafe (zeros present) or disallowed
* Two passes (prefix then suffix) can compute the answer in O(1) extra space

## Keywords

* Prefix Sum
* Prefix Product
* Suffix Product
* Two Pass

## Similar Problems

* 2574. Left and Right Sum Differences
* 724. Find Pivot Index
* 42. Trapping Rain Water