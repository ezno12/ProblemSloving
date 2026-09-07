# LeetCode 4040 - Minimum Operations to Form Subset Sum I

Pattern: Dynamic Programming (Bounded Knapsack style)

Difficulty: Medium

## Idea

For each number, precompute the cheapest ways to reach nearby values by repeatedly halving (integer division) or doubling it, tracking how many operations each transformation costs.

Use a DP array dp[s] representing the minimum total operations to make some subset of processed numbers sum to s, updating it (like a knapsack) as each number's possible transformed values and their costs are considered.

## Complexity

* Time: O(n * sum * log(max value)) roughly, due to the halving/doubling options per number
* Space: O(sum)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from missing some reachable transformed values (e.g., not considering both directions - halving down and doubling up - for every number) or from an off-by-one in the DP update loop.

## Recognition

Look for this pattern when you have:

* Need to hit an exact target sum using a subset of transformable numbers
* Each number can be turned into several possible values at different costs
* A knapsack-style DP over achievable sums fits naturally

## Keywords

* Dynamic Programming
* Knapsack
* Subset Sum
* Cost Minimization

## Similar Problems

* 322. Coin Change
* 416. Partition Equal Subset Sum
* 494. Target Sum