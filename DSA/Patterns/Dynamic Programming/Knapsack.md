# Knapsack

**Pattern:** DP - Knapsack
**Category:** Dynamic Programming

## Recognition

* Choose a subset subject to a capacity / budget / target
* "Can we reach exactly sum S"
* "Maximum value within weight W"
* Coin change (min coins, or number of ways)
* Partition into equal-sum halves
* Target sum with +/- signs

## Tricks

* Weight-only (subset sum) -> boolean DP; weight+value -> numeric DP
* 0/1 knapsack: iterate capacity DESCENDING in the 1D version (each item once)
* Unbounded knapsack: iterate capacity ASCENDING (items reusable)
* Bounded (k copies): binary-split each item into 1, 2, 4, ... copies
* COMBINATIONS (order irrelevant): items outer loop, capacity inner
* PERMUTATIONS (order matters): capacity outer loop, items inner
* Partition Equal Subset Sum = subset sum with target `total // 2` (odd total -> impossible)

## Template

```python
# 0/1 knapsack, maximize value, 1D
def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):     # DESCENDING = use each item once
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]

# Unbounded: count ways to make each amount (combinations)
def coin_change_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:                            # coins outer -> combinations
        for c in range(coin, amount + 1):         # ASCENDING = reusable
            dp[c] += dp[c - coin]
    return dp[amount]
```

## Complexity

* **Time:** O(n × capacity)
* **Space:** O(capacity)

## Problems

- [ ] Weight-Only Knapsack
- [ ] Partition Equal Subset Sum
- [ ] Target Sum
- [ ] Coin Change II
- [ ] Coin Change, Optimization
- [ ] Perfect Squares
- [ ] 0/1 Knapsack Practice Problem
- [ ] Bounded Knapsack

## Mistakes

* Iterating capacity ASCENDING in 0/1 knapsack — items silently get reused.
* Swapping the loop order and counting permutations when the problem wants combinations (Coin Change II vs Combination Sum IV).
* Forgetting `dp[0] = 1` for counting, or `dp[0] = 0` with the rest `inf` for minimizing.
* Not checking `total % 2 != 0` early in Partition Equal Subset Sum.
* Returning `dp[amount]` as the answer for min-coins when it is still `inf` — that means impossible, return -1.

## Keywords

* Dynamic Programming
* Knapsack
* 0/1 Knapsack
* Unbounded Knapsack
* Subset Sum
* Coin Change
* Target Sum
* Loop Direction
* Combinations vs Permutations
