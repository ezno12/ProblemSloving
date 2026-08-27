# Non-constant Transition

**Pattern:** DP - Non-constant Transition
**Category:** Dynamic Programming

## Recognition

* `dp[i]` depends on ALL (or many) earlier states, not a fixed few
* Longest increasing subsequence
* Partition an array into groups with a size limit
* Largest divisible subset
* Word break where any earlier split point is allowed
* Game theory over a range (divisor game)

## Tricks

* Inner loop over all `j < i`, giving O(n^2)
* `dp[i] = max/min over j of f(dp[j], arr[j..i])`
* LIS: `dp[i] = 1 + max(dp[j] for j < i if arr[j] < arr[i])`
* LIS in O(n log n): patience sorting with `bisect_left` on a "tails" array
* Bounded inner loop (e.g. group size ≤ k) makes it O(nk)
* Reconstruct the sequence by storing a `parent[i]` pointer

## Template

```python
def non_constant_dp(arr):
    n = len(arr)
    dp = [base] * n
    for i in range(n):
        for j in range(i):
            if is_valid(arr[j], arr[i]):
                dp[i] = combine(dp[i], dp[j], arr[i])
    return best_of(dp)

# LIS in O(n log n)
import bisect
def lis(arr):
    tails = []
    for x in arr:
        i = bisect.bisect_left(tails, x)   # bisect_right for non-strict
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)
```

## Complexity

* **Time:** O(n^2) in general, O(n log n) for LIS with binary search
* **Space:** O(n)

## Problems

- [ ] Longest Increasing Subsequence
- [ ] Partition Array for Maximum Sum
- [ ] Largest Divisible Subset
- [ ] Divisor Game
- [ ] Longest String Chain

## Mistakes

* Returning `dp[n-1]` instead of `max(dp)` — the best subsequence rarely ends at the last element.
* Initializing `dp` to 0 when every single element is already a valid length-1 answer.
* `bisect_left` vs `bisect_right` decides strictly increasing vs non-decreasing — pick deliberately.
* Sorting the input for LIS (that destroys the problem) versus for Largest Divisible Subset (where sorting is required).
* Forgetting the validity guard, so invalid transitions leak in.

## Keywords

* Dynamic Programming
* Non-constant Transition
* LIS
* Inner Loop over j
* Patience Sorting
* Bisect
* Parent Pointer
* Quadratic DP
