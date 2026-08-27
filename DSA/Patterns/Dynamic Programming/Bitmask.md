# Bitmask

**Pattern:** DP - Bitmask
**Category:** Dynamic Programming

## Recognition

* Small n (roughly n ≤ 20)
* "Visit every node/task exactly once" (travelling salesman shape)
* Assign n tasks to n people
* Subset of items as a compact state
* Minimum cost to visit every node
* The constraint `n <= 15` or `n <= 20` is the giveaway

## Tricks

* State = an integer whose bits mark which items are used
* `mask | (1 << i)` sets bit i; `mask & (1 << i)` tests it
* `bin(mask).count('1')` (or `mask.bit_count()`) gives how many are used — often doubles as the step index
* Iterate masks ascending; every submask is a smaller integer, so the order is already valid
* TSP state is `(mask, last_node)`, not just `mask`
* Enumerate submasks with `sub = (sub - 1) & mask`
* 2^20 × 20 is about 2e7 — fine; 2^25 is not

## Template

```python
def bitmask_dp(n, cost):
    full = (1 << n) - 1
    INF = float('inf')
    # dp[mask][last] = min cost having visited `mask`, currently at `last`
    dp = [[INF] * n for _ in range(1 << n)]
    for i in range(n):
        dp[1 << i][i] = 0
    for mask in range(1 << n):
        for last in range(n):
            if dp[mask][last] == INF or not (mask & (1 << last)):
                continue
            for nxt in range(n):
                if mask & (1 << nxt):
                    continue
                nm = mask | (1 << nxt)
                dp[nm][nxt] = min(dp[nm][nxt], dp[mask][last] + cost[last][nxt])
    return min(dp[full])
```

## Complexity

* **Time:** O(2^n × n^2) for the TSP shape, O(2^n × n) for the simple assignment shape
* **Space:** O(2^n × n)

## Problems

- [ ] Bitmask Introduction
- [ ] Bitmask DP
- [ ] Minimum Cost to Visit Every Node
- [ ] Partition to K Equal Sum Subsets
- [ ] Shortest Path Visiting All Nodes

## Mistakes

* `1 << i` vs `i << 1` — a genuinely common typo.
* Operator precedence differs by language: in Python `&` binds tighter than `==`, so
* `mask & (1 << i) == 0` is fine; in C/C++/Java `==` binds tighter and it becomes
* `mask & ((1 << i) == 0)`. Parenthesize `(mask & (1 << i)) == 0` everywhere out of habit.
* Using only `mask` as the state when the transition cost depends on where you currently are.
* Applying bitmask DP with n = 30 and running out of memory.
* Off-by-one on `full = (1 << n) - 1` (writing `1 << n` instead).
* Iterating masks in an order where a needed submask has not been computed yet.

## Keywords

* Dynamic Programming
* Bitmask
* Subset as Integer
* Small n
* TSP
* Bit Operations
* Submask Enumeration
* State Compression
