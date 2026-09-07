# LeetCode 881 - Boats to Save People

Pattern: Two Pointers + Greedy

Difficulty: Medium

## Idea

Sort the people by weight.

Use two pointers: left at the lightest person, right at the heaviest.

Try to pair the heaviest remaining person with the lightest remaining person. If their combined weight fits the limit, move both pointers; otherwise, the heaviest person must go alone, so only move the right pointer.

Each iteration uses exactly one boat.

## Complexity

* Time: O(n log n) for the sort
* Space: O(1) extra (ignoring sort space)

## Mistakes

* Solved cleanly on the first accepted attempt. Key insight: always send the heaviest remaining person, and greedily pair them with the lightest remaining person if possible.

## Recognition

Look for this pattern when you have:

* Need to pair elements optimally under a capacity/weight constraint
* Sorting first exposes a greedy two-pointer strategy
* Each pairing decision only depends on the current extremes

## Keywords

* Two Pointers
* Greedy
* Sorting
* Pairing Under Constraint

## Similar Problems

* 11. Container With Most Water
* 167. Two Sum II - Input Array Is Sorted
* 455. Assign Cookies