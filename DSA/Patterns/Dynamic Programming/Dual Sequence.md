# Dual Sequence

**Pattern:** DP - Dual Sequence (Two Strings)
**Category:** Dynamic Programming

## Recognition

* TWO strings or arrays compared against each other
* Longest common subsequence
* Edit distance / minimum operations to transform
* "How many ways to form B from A"
* Interleaving, wildcard or regex matching
* Delete operation for two strings

## Tricks

* `dp[i][j]` = answer for the first i chars of A and first j chars of B
* `dp` is `(m+1) × (n+1)` — row/col 0 means "empty prefix"
* If `a[i-1] == b[j-1]`: extend the diagonal `dp[i-1][j-1]`
* Else: take the best of `dp[i-1][j]` (delete) and `dp[i][j-1]` (insert)
* Edit distance adds `dp[i-1][j-1]` (replace) to that max/min
* Only the previous row matters -> O(n) space
* Base row/column are the "convert to/from empty string" costs

## Template

```python
def dual_sequence_dp(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = base_row(i)
    for j in range(n + 1):
        dp[0][j] = base_col(j)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + match_value
            else:
                dp[i][j] = combine(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]
```

## Complexity

* **Time:** O(m × n)
* **Space:** O(m × n), reducible to O(min(m, n))

## Problems

- [ ] Longest Common Subsequence
- [ ] Edit Distance
- [ ] Delete String
- [ ] Distinct Subsequences
- [ ] Shortest Common Supersequence

## Mistakes

* Indexing `a[i]` instead of `a[i-1]` when `dp` is 1-indexed. This is THE bug in this family.
* Forgetting to initialize row 0 and column 0 (edit distance needs `dp[i][0] = i`).
* Confusing subSEQUENCE (not contiguous) with subSTRING (contiguous — that needs a reset to 0 on mismatch).
* Space-optimizing while still reading `dp[i-1][j-1]` after it was overwritten — cache it in a temp.
* Returning `dp[m-1][n-1]` instead of `dp[m][n]`.

## Keywords

* Dynamic Programming
* Dual Sequence
* Two Strings
* LCS
* Edit Distance
* Diagonal Transition
* Empty Prefix
* 1-indexed DP
