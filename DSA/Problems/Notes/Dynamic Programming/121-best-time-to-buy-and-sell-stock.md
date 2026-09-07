# LeetCode 121 - Best Time to Buy and Sell Stock

Pattern: Dynamic Programming / Greedy (single pass)

Difficulty: Easy

## Idea

Track the lowest price seen so far (buy_price) while scanning through the prices array once.

At each day, if the current price is lower than buy_price, update buy_price. Otherwise, check if selling today (prices[i] - buy_price) beats the best profit found so far, and update profit if so.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from initializing profit or buy_price incorrectly, or from allowing a "sell before buy" scenario by not properly tracking the running minimum.

## Recognition

Look for this pattern when you have:

* Need the best single buy/sell pair from a price sequence, in one pass
* Only one transaction is allowed (contrast with variants allowing multiple transactions, which need true DP with states)

## Keywords

* Dynamic Programming
* Greedy
* Single Pass
* Running Minimum

## Similar Problems

* 122. Best Time to Buy and Sell Stock II
* 123. Best Time to Buy and Sell Stock III
* 198. House Robber