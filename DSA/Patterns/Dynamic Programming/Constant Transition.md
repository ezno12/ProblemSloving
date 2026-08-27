# Constant Transition

**Pattern:** DP - Constant Transition
**Category:** Dynamic Programming

## Recognition

* 1D array / sequence
* Each state depends on a FIXED number of previous states (i-1, i-2, ...)
* "Max / min / count ways" along a line
* Cannot take two adjacent items
* Climbing stairs, house robber, ticket costs
* The entry point to all DP — learn this shape first

## Tricks

* Define `dp[i]` in one English sentence before writing any code
* Transition looks like `dp[i] = f(dp[i-1], dp[i-2], ...)`
* Base cases are the first 1-2 entries; get them right and the rest follows
* Space optimize to O(1) once it works — you only need the last k values
* Top-down (`@cache` on a recursive function) is the same thing; write whichever you trust
* "Cannot take adjacent" -> `dp[i] = max(dp[i-1], dp[i-2] + value[i])`

## Template

```python
def dp_constant_transition(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = base_0
    dp[1] = base_1
    for i in range(2, n + 1):
        dp[i] = combine(dp[i - 1], dp[i - 2], arr[i - 1])
    return dp[n]

# O(1) space version
def dp_rolling(arr):
    prev2, prev1 = base_0, base_1
    for x in arr[1:]:
        prev2, prev1 = prev1, combine(prev1, prev2, x)
    return prev1
```

## Complexity

* **Time:** O(n)
* **Space:** O(n), reducible to O(1)

## Problems

- [ ] Climbing Stairs
- [ ] N-th Tribonacci Number
- [ ] House Robber
- [ ] Min Cost Climbing Stairs
- [ ] Minimum Cost For Tickets

## Mistakes

* Off-by-one between `dp` indices and array indices — pick 1-indexed `dp` and stick to it.
* Wrong base cases (the classic source of "works for n>2, fails for n=1").
* Initializing a `min` DP with 0 instead of infinity.
* Space-optimizing before the O(n) version is correct.
* Assigning `prev1` before `prev2` in the rolling version without a simultaneous swap.

## Keywords

* Dynamic Programming
* Constant Transition
* 1D DP
* House Robber
* Climbing Stairs
* Base Case
* Rolling Variables
* Space Optimization
