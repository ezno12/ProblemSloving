# Line Sweep

**Pattern:** Line Sweep (Event Sorting)
**Category:** Intervals

## Recognition

* Maximum concurrent events (rooms, cars, CPU load)
* Union of areas / total covered length
* Skyline problems
* "How many intervals cover point x"
* Rectangle overlap area
* Any geometry problem framed as "sweep a vertical line left to right"

## Tricks

* Turn each interval into two events: `(start, +1)` and `(end, -1)`
* Sort events; ties matter — process `-1` before `+1` if touching does not count as overlap
* Keep a running counter; the max counter is the answer
* For area problems, multiply the active length by the x-distance to the next event
* A heap of active items works when you need to know WHICH items are active, not just how many
* Coordinate compression when values are sparse but large

## Template

```python
def max_concurrent(intervals):
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()                 # (-1) sorts before (+1) at the same x
    active = best = 0
    for _, delta in events:
        active += delta
        best = max(best, active)
    return best
```

## Complexity

* **Time:** O(n log n)
* **Space:** O(n)

## Problems

- [ ] Line-Sweep Introduction
- [ ] Union Area of Rectangles
- [ ] Meeting Rooms II
- [ ] The Skyline Problem
- [ ] My Calendar III
- [ ] Car Pooling

## Mistakes

* Tie-breaking backwards: if `[1,2]` and `[2,3]` must NOT overlap, the `-1` at x=2 has to be processed first.
* Using `(x, +1)` / `(x, -1)` sort keys where `+1 < -1` in your language's ordering.
* Forgetting that the answer is the MAX of the running counter, not its final value (which is always 0).
* Double counting when intervals share endpoints.
* Skipping coordinate compression and building an array over the full value range.

## Keywords

* Line Sweep
* Event Sorting
* Plus One Minus One
* Running Counter
* Maximum Concurrent
* Skyline
* Coordinate Compression
* Tie-breaking
