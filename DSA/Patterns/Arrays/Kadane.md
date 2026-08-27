# Kadane

**Pattern:** Kadane's Algorithm (Maximum Subarray)
**Category:** Arrays

## Recognition

* "Maximum sum subarray" / "maximum sum contiguous"
* Contiguous, and the array contains negative numbers
* Best time to buy and sell stock (max profit = `max(0, max subarray of daily deltas)` —
  the 0 is the "do not trade" case, which plain Kadane cannot return)
* Maximum product subarray (track min and max together)
* Circular array variant
* Local decision at each index: extend the run, or start over

## Tricks

* At each index the choice is local: `extend` or `restart` — that is what makes it greedy
* `cur = max(x, cur + x)`, then `best = max(best, cur)`
* Initialize `best = -inf`, NOT 0, or an all-negative array returns 0
* Stock profit: run Kadane on the array of consecutive differences, then clamp with `max(0, ...)`
* Max PRODUCT subarray: track `cur_max` and `cur_min`, because a negative flips them
* Circular: answer is `max(normal Kadane, total - minimum subarray)`, with an all-negative guard
* Track the start/end indices by recording where the restart happened

## Template

```python
def max_subarray(nums):
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)       # restart at x, or extend the running sum
        best = max(best, cur)
    return best

def max_subarray_with_bounds(nums):
    best = cur = nums[0]
    start = best_start = best_end = 0
    for i, x in enumerate(nums[1:], 1):
        if x > cur + x:             # restarting
            cur, start = x, i
        else:
            cur = cur + x
        if cur > best:
            best, best_start, best_end = cur, start, i
    return best, best_start, best_end
```

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Problems

- [ ] Maximum Subarray
- [ ] Best Time to Buy and Sell Stock
- [ ] Maximum Product Subarray
- [ ] Maximum Sum Circular Subarray

## Mistakes

* Initializing `best = 0` — an all-negative array then wrongly returns 0 instead of the largest element.
* Starting the loop at index 0 after seeding `cur = nums[0]`, double-counting the first element.
* Applying it to a non-contiguous ("subsequence") problem — that is DP, not Kadane.
* Max product: carrying only the max and losing the negative-times-negative case.
* Circular variant: forgetting the all-negative special case, where `total - min_subarray` is 0 and invalid.
* Not handling an empty input array.

## Keywords

* Kadane
* Maximum Subarray
* Contiguous
* Extend or Restart
* Local Optimal
* Max Product Subarray
* Circular Subarray
* Stock Profit
