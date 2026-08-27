# Interval Merge and Sweep

**Pattern:** Interval (Sort by Start, Sweep)
**Category:** Intervals

## Recognition

* List of `[start, end]` pairs
* Merge overlapping intervals
* Insert an interval
* "Can all meetings be attended" / minimum rooms
* Remove the fewest intervals to make them non-overlapping
* Partition labels / last occurrence grouping

## Tricks

* Sort by START for merging; sort by END for "maximum non-overlapping count" (greedy)
* Overlap test: `start <= last_end` (use `<` if touching endpoints do not count)
* Merge by extending: `last_end = max(last_end, end)`
* Minimum meeting rooms = min-heap of end times, or a +1/-1 sweep over sorted events
* Erase-overlap-intervals: sort by end, greedily keep, count the drops
* Always ask whether `[1,2]` and `[2,3]` count as overlapping

## Template

```python
def interval_pattern(intervals):
    # 1. Sort by start time
    intervals.sort(key=lambda x: x[0])
    result = []
    for start, end in intervals:
        # 2. Overlap with the last kept interval? end >= next start
        if result and start <= result[-1][1]:
            # Merge: extend the end of the last interval
            result[-1][1] = max(result[-1][1], end)
        else:
            # 3. No overlap: keep this interval as-is
            result.append([start, end])
    return result
```

## Complexity

* **Time:** O(n log n) dominated by the sort
* **Space:** O(n) for the output, O(1) extra

## Problems

- [ ] Merge Intervals
- [ ] Insert Interval
- [ ] Meeting Rooms
- [ ] Meeting Rooms II
- [ ] Non-overlapping Intervals
- [ ] Minimum Number of Arrows to Burst Balloons
- [ ] Partition Labels

## Mistakes

* `result[-1][1] = end` instead of `max(...)` — a fully contained interval then shrinks the merged range.
* Sorting by start when the greedy needs end (Non-overlapping Intervals / Arrows).
* Mutating the input list of lists when the caller still needs it (or getting a TypeError on tuples).
* Not clarifying the inclusive/exclusive endpoint convention.
* Forgetting to append the final in-progress interval in a manual loop variant.

## Keywords

* Intervals
* Merge Intervals
* Sort by Start
* Sort by End
* Overlap Test
* Meeting Rooms
* Greedy
* Endpoint Convention
