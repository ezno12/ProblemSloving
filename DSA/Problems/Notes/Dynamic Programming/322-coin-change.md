# LeetCode 322 - Coin Change

Pattern: Dynamic Programming (Top-Down Memoization)

Difficulty: Medium

## Idea

Use recursion with memoization: min_coins(sum) is the minimum number of coins needed to go from the current sum up to the target amount.

At each step, try adding every coin denomination and recurse; take the minimum of all resulting coin counts, adding 1 for the coin used. If sum exceeds amount, that path is invalid (infinity).

## Complexity

* Time: O(amount * number of coin denominations)
* Space: O(amount) for memoization

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from not properly handling the case where no combination of coins can reach the amount (should return -1, not the sentinel infinity value directly).

## Recognition

Look for this pattern when you have:

* Need the minimum (or maximum) number of items from an unlimited supply to reach an exact target
* Each choice reduces the remaining target, and results overlap between subproblems, making memoization valuable

## Keywords

* Dynamic Programming
* Memoization
* Unbounded Knapsack
* Minimum Coins

## Similar Problems

* 139. Word Break
* 4040. Minimum Operations to Form Subset Sum I
* 518. Coin Change II