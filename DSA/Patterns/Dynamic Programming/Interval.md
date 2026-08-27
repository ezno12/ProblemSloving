# Interval

**Pattern:** DP - Interval
**Category:** Dynamic Programming

## Recognition

* `dp[i][j]` describes a RANGE `[i..j]` of the input
* Palindromic substrings / subsequences
* Burst balloons, matrix chain multiplication
* Two-player games where both take from the ends
* Merge stones / minimum cost to combine adjacent items
* The answer for a range comes from splitting it, or from shrinking both ends

## Tricks

* Iterate by LENGTH (shortest ranges first) so subproblems are ready
* Or iterate `i` descending and `j` ascending — same effect
* Palindrome shape: `dp[i][j] = dp[i+1][j-1] and s[i] == s[j]`
* Split shape: `dp[i][j] = best over k in (i, j) of dp[i][k] + dp[k][j] + cost`
* Game shape: `dp[i][j] = max(a[i] - dp[i+1][j], a[j] - dp[i][j-1])` (score difference)
* Burst Balloons: think about the LAST balloon burst in the range, not the first

## Template

```python
def interval_dp(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):              # shortest ranges first
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = worst_value
            for k in range(i, j):               # split point
                dp[i][j] = best(dp[i][j], dp[i][k] + dp[k + 1][j] + cost(i, k, j))
    return dp[0][n - 1]
```

## Complexity

* **Time:** O(n^3) with a split loop, O(n^2) for the shrink-both-ends shape
* **Space:** O(n^2)

## Problems

- [ ] Interval DP Intro
- [ ] Palindromic Substrings
- [ ] Longest Palindromic Subsequence
- [ ] Coin Game
- [ ] Burst Balloons
- [ ] Matrix Chain Multiplication

## Mistakes

* Iterating `i` and `j` in the natural forward order, reading `dp[i+1][j-1]` before it is computed.
* Forgetting the length-1 base case (`dp[i][i]`), and length-2 for palindromes.
* Off-by-one in the split loop: `range(i, j)` vs `range(i, j+1)` changes whether a part can be empty.
* Burst Balloons: modelling the FIRST burst instead of the last, which makes the subproblems non-independent.
* Game DP: tracking absolute score instead of the score DIFFERENCE.

## Keywords

* Dynamic Programming
* Interval DP
* Range DP
* Iterate by Length
* Split Point
* Palindromic Subsequence
* Burst Balloons
* Game States
* Score Difference
