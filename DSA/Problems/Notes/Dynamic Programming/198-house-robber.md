# LeetCode 198 - House Robber

Pattern: Dynamic Programming

Difficulty: Medium

## Idea

Track two rolling values: last (best profit not including the current house) and now (best profit including the possibility of the current house).

For each house value i, update them together: last becomes the old now, and now becomes max(last + i, now) - either rob this house (adding to the profit from two houses back) or skip it (keep the previous best).

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. This space-optimized rolling-pair version avoids keeping a full DP array, since only the last two states are ever needed.

## Recognition

Look for this pattern when you have:

* A sequence where adjacent elements cannot both be selected
* Need to maximize a sum subject to that adjacency constraint
* The recurrence only depends on the previous one or two states

## Keywords

* Dynamic Programming
* Space Optimization
* Non-Adjacent Selection
* Rolling State

## Similar Problems

* 213. House Robber II
* 337. House Robber III
* 70. Climbing Stairs