# Prefix Sum

**Category:** Arrays

## Recognition

* Many range-sum queries on a static array
* Subarray sum equals target (with a hashmap)
* Contiguous
* Negative numbers present (sliding window fails)
* 2D region sums
* Running count / balance ("equal number of 0s and 1s")

## Tricks

* `sum(left..right) = prefix[right] - prefix[left-1]`
* Pad with a leading 0 (`prefix[0] = 0`) to kill the `left == 0` special case
* Hashmap of `prefix_sum -> count` (seeded with `{0: 1}`) counts subarrays summing to k
* Map a value to +1 / -1 to turn "equal counts" into "prefix sum equals 0"
* 2D: `P[r][c] - P[r0-1][c] - P[r][c0-1] + P[r0-1][c0-1]`
* Prefix product (left pass × right pass) for Product of Array Except Self

## Template

```python
def build_prefix_sum(arr):
    n = len(arr)
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum

# Query sum of range [left, right] (inclusive)
def query_range(prefix_sum, left, right):
    if left == 0:
        return prefix_sum[right]
    return prefix_sum[right] - prefix_sum[left-1]
```

## Complexity

* **Time:** O(n) build, O(1) per query
* **Space:** O(n)

## Problems

- [ ] Subarray Sum Equals Target
- [ ] Range Sum Query - Immutable
- [ ] Product of Array Except Self
- [ ] Contiguous Array (equal 0s and 1s)
- [ ] 2D Range Sum Query

## Mistakes

* Off-by-one on the inclusive/exclusive convention — write down which one you chose.
* Forgetting to seed the hashmap with `{0: 1}`, so subarrays starting at index 0 are missed.
* Recording the current prefix in the map BEFORE querying it, which lets a subarray count itself.
* Using prefix sum on an array that gets updated — that needs a Fenwick / segment tree.
* Integer overflow in Java/C++ on large sums.

## Keywords

* Prefix Sum
* Range Sum
* Cumulative Sum
* Hash Map of Prefixes
* Subarray Sum
* Negative Numbers
* Running Balance
* 2D Prefix Sum
* Prefix Product
