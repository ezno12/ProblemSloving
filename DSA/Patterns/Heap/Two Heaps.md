# Two Heaps

**Pattern:** Two Heaps (Running Median / Balanced Split)
**Category:** Heap

## Recognition

* Median of a data stream
* "Median in a sliding window"
* Continuously split values into a smaller half and a larger half
* IPO / scheduling problems needing both extremes
* Any time you need the middle element as elements keep arriving

## Tricks

* MAX-heap for the lower half, MIN-heap for the upper half
* Invariant: `len(low) == len(high)` or `len(low) == len(high) + 1`
* Always push to `low` first, then move `low`'s top to `high`, then rebalance
* Median = `low[0]` (odd total) or the average of both tops (even total)
* Python: store negatives in `low` to fake a max-heap
* Sliding-window median needs lazy deletion (a `to_remove` counter map)

## Template

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.low = []    # max-heap (negated) - smaller half
        self.high = []   # min-heap          - larger half

    def add(self, num):
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))   # top of low -> high
        if len(self.high) > len(self.low):                    # rebalance
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def median(self):
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2
```

## Complexity

* **Time:** O(log n) per insert, O(1) per median query
* **Space:** O(n)

## Problems

- [ ] Median of Data Stream
- [ ] Sliding Window Median
- [ ] IPO
- [ ] Find Median from Data Stream II

## Mistakes

* Rebalancing before the cross-push, so a small number ends up stuck in the upper heap.
* Forgetting the sign flip when reading `low[0]`.
* Integer division for the even-count median (`// 2` instead of `/ 2`).
* Allowing the sizes to drift by more than 1.
* Trying to delete an arbitrary element from a heap directly — use lazy deletion.

## Keywords

* Two Heaps
* Running Median
* Max-heap and Min-heap
* Balanced Split
* Data Stream
* Rebalancing
* Lazy Deletion
* Negation Trick
