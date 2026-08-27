# Segment Tree

**Pattern:** Segment Tree / Fenwick Tree
**Category:** Advanced Data Structures

## Recognition

* Range queries AND point updates on the same array
* Range sum / min / max / gcd with mutation
* Prefix sum is not enough because the array changes
* "Count smaller numbers after self" (Fenwick over compressed values)
* Range assignment / range add (with lazy propagation)

## Tricks

* Segment tree = array of size 4n, node i has children 2i+1 and 2i+2
* Any associative merge works: `+`, `min`, `max`, `gcd`, matrix product
* Fenwick (BIT) is shorter and faster for pure prefix sums: `i & -i` walks the tree
* Lazy propagation only when you need RANGE updates, not point updates
* Coordinate-compress values first when the domain is huge
* In an interview, say "Fenwick tree" for sums and "segment tree" for min/max — and confirm it is actually needed

## Template

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, lo, hi):
        if lo == hi:
            self.tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        self._build(arr, 2 * node + 1, lo, mid)
        self._build(arr, 2 * node + 2, mid + 1, hi)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, i, val, node=0, lo=0, hi=None):
        if hi is None:
            hi = self.n - 1
        if lo == hi:
            self.tree[node] = val
            return
        mid = (lo + hi) // 2
        if i <= mid:
            self.update(i, val, 2 * node + 1, lo, mid)
        else:
            self.update(i, val, 2 * node + 2, mid + 1, hi)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r, node=0, lo=0, hi=None):
        if hi is None:
            hi = self.n - 1
        if r < lo or hi < l:              # no overlap
            return 0                      # identity of the merge
        if l <= lo and hi <= r:           # total overlap
            return self.tree[node]
        mid = (lo + hi) // 2              # partial overlap
        return (self.query(l, r, 2 * node + 1, lo, mid)
                + self.query(l, r, 2 * node + 2, mid + 1, hi))
```

## Complexity

* **Time:** O(n) build, O(log n) per update, O(log n) per query
* **Space:** O(n)

## Problems

- [ ] Segment Tree Intro
- [ ] Range Max
- [ ] Range Sum Query - Mutable
- [ ] Count of Smaller Numbers After Self

## Mistakes

* Wrong identity in the no-overlap case: `0` for sum, but `inf` for min and `-inf` for max.
* Allocating `2n` instead of `4n` and indexing out of range.
* Forgetting to recombine (`tree[node] = merge(children)`) after an update.
* Using a segment tree when a prefix sum array would do (no updates) — over-engineering.
* Off-by-one between the inclusive `[lo, hi]` node range and a half-open query range.

## Keywords

* Segment Tree
* Fenwick Tree
* BIT
* Range Query
* Point Update
* Lazy Propagation
* Associative Merge
* Identity Value
* Coordinate Compression
