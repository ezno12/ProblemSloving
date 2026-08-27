# Greedy

**Pattern:** Greedy (Sort, then One Pass)
**Category:** Greedy

## Recognition

* Local optimal choice provably leads to global optimum
* Scheduling by deadline / end time
* "Minimum number of X to cover Y"
* Assign / match / partition with a natural ordering
* Jump game, gas station, candy distribution
* When DP feels like overkill and a sort makes the answer obvious

## Tricks

* The whole pattern is: find the right SORT KEY, then one linear pass
* Common keys: deadline, end time, size, value/weight ratio, absolute difference
* Correctness needs an EXCHANGE ARGUMENT: swapping any pair away from the greedy order never improves the result
* Keep a small running `state` (current time, remaining capacity, last taken index)
* If you cannot state the exchange argument, suspect DP instead
* Greedy is low ROI in interviews precisely because each problem needs its own proof

## Template

```python
def greedy(items):
    # 1. Sort by the greedy key (deadline, end time, size, ratio, ...)
    items.sort(key=greedy_key)
    result = 0
    state = initial_state()
    for item in items:
        # 2. Take the item only if the locally best choice is valid
        if is_feasible(item, state):
            result += take(item, state)
    # 3. Correctness relies on an exchange argument, not just passing tests
    return result
```

## Complexity

* **Time:** O(n log n) for the sort + O(n) pass
* **Space:** O(1) extra

## Problems

- [ ] Greedy Introduction
- [ ] Gas Station
- [ ] Jump Game
- [ ] Task Assignment / Boats to Save People
- [ ] Non-overlapping Intervals

## Mistakes

* Picking a plausible sort key without proving it — greedy that passes the samples and fails the hidden tests.
* Sorting by start when the correct key is end (or by value when it should be value/weight).
* Greedy on a problem that needs 0/1 knapsack DP (fractional knapsack is greedy, 0/1 is not).
* Mutating `state` before the feasibility check.
* Forgetting the tie-break rule when two items share the greedy key.

## Keywords

* Greedy
* Sort then One Pass
* Greedy Key
* Exchange Argument
* Local Optimal
* Scheduling
* Deadline
* Proof Required
