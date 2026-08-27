# Binary Search

**Category:** Binary Search

## Recognition

* Sorted array
* Monotonic / boolean predicate ("first true")
* Search space of answers, not just indices
* "Minimum X such that condition holds"
* "Maximum X such that condition holds"
* Rotated sorted array
* O(log n) required by constraints (n up to 1e9)

## Tricks

* Find the first `True` in a `False False ... True True` array
* Reduce to a `feasible(mid)` boolean function
* Binary search the answer, not the index (Newspapers / Koko style)
* `mid = (left + right) // 2` and shrink the side that keeps the invariant
* Use `left < right` + no answer variable when the answer must exist
* `bisect_left` / `bisect_right` for plain lookups

## Template

```python
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    first_true_index = -1
    while left <= right:
        mid = (left + right) // 2
        if feasible(mid):
            first_true_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return first_true_index
```

## Complexity

* **Time:** O(log n) for index search, O(n log(range)) when `feasible` scans the input
* **Space:** O(1)

## Problems

- [ ] First True
- [ ] First Element Not Smaller Than Target
- [ ] First Occurrence
- [ ] Square Root Estimation
- [ ] Minimum in Rotated Sorted Array
- [ ] Peak of Mountain Array
- [ ] Newspapers (binary search on answer)

## Mistakes

* Off-by-one: pick ONE convention (`left <= right` + `mid ± 1`) and never mix it with `left < right`.
* Forgetting to record the candidate before shrinking right.
* Assuming the array is sorted when it is only "implicitly sorted" — check the predicate is truly monotonic.
* `(left + right) // 2` overflow is a non-issue in Python but real in Java/C++ — use `left + (right - left) // 2` habitually.
* Binary searching a predicate that flips more than once. No monotonicity, no binary search.

* From your own AlgoMonster note on **Newspapers**:
- Be careful about the loop condition.
- Be careful declaring and assigning `low` / `high`.
- Dig deep on the monotonic function and learn to detect it.
- Find the feasible condition for the problem first.
- Newspapers is hard-level — worth solving again from scratch.

## Keywords

* Binary Search
* Sorted Array
* Monotonic Predicate
* First True
* Search Space
* Feasible Condition
* Logarithmic Time
* Rotated Array
* Binary Search on Answer
