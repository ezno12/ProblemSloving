# Backtracking - Aggregation

**Pattern:** Backtracking - Aggregation (Count / Optimize)
**Category:** Backtracking

## Recognition

* "How many ways" (count, don't list)
* "Minimum / maximum number of ..." over a combinatorial space
* Word break: can it be segmented
* Decode ways
* Coin change (min coins / number of ways)
* The natural bridge from DFS to Dynamic Programming

## Tricks

* Return a NUMBER up the recursion instead of collecting paths
* `aggregate` = `sum` for counting, `min`/`max` for optimizing
* Base case returns the identity: 1 for counting, 0 or inf for min/max
* Add `@cache` / `functools.lru_cache` the moment the state repeats — that is memoization, i.e. top-down DP
* Keep the state small and hashable so caching actually works
* If the state is only `start_index`, this is a 1D DP in disguise

## Template

```python
def dfs(start_index, [...additional states]):
    if is_leaf(start_index):
        return 1
    ans = initial_value
    for edge in get_edges(start_index, [...additional states]):
        if additional states:
            update([...additional states])
        ans = aggregate(ans, dfs(start_index + len(edge), [...additional states]))
        if additional states:
            revert([...additional states])
    return ans
```

## Complexity

* **Time:** exponential without memo; O(states × edges per state) with memo
* **Space:** O(states) for the cache + O(depth) stack

## Problems

- [ ] Word Break
- [ ] Num Ways to Decode a Message
- [ ] Min Coins to Make Change
- [ ] Climbing Stairs (as aggregation)
- [ ] Unique Paths (as aggregation)

## Mistakes

* Wrong identity: starting `ans = 0` for a `min` aggregation, or `inf` for a sum.
* Memoizing on a mutable argument (list, set) — `@cache` needs hashable state, convert to tuple/frozenset.
* Memoizing a state that does not fully determine the sub-answer (missing a dimension).
* Returning `inf` from an unreachable branch and then adding 1 to it — guard before adding.
* Reverting shared mutable state before you have used the return value.

## Keywords

* Backtracking
* Aggregation
* Counting
* Memoization
* Top-down DP
* Word Break
* Decode Ways
* State Design
* Identity Value
