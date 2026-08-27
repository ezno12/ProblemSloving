# Top K

**Pattern:** Heap / Priority Queue - Top K
**Category:** Heap

## Recognition

* "K largest / K smallest / K closest / K most frequent"
* Merge K sorted lists or streams
* Kth element without full sorting
* Streaming data, n unknown or huge
* Repeatedly need the current best / worst item

## Tricks

* K LARGEST -> MIN-heap of size k; K SMALLEST -> MAX-heap of size k (counter-intuitive, memorize it)
* Python `heapq` is a min-heap: negate values for a max-heap
* Push, then pop when `len(heap) > k` — the heap stays size k
* `heapq.nlargest(k, it)` / `nsmallest` for quick solutions
* Tuples `(key, tiebreak, item)` to control ordering; make sure every field is comparable
* Merge K lists: seed the heap with one node per list, then push the successor of whatever you pop
* Quickselect is O(n) average if the interviewer pushes past O(n log k)

## Template

```python
import heapq

def top_k_largest(nums, k):
    heap = []                        # min-heap of the k largest so far
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)      # drop the smallest
    return heap                      # heap[0] is the kth largest

def merge_k_sorted(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    out = []
    while heap:
        val, i, j = heapq.heappop(heap)
        out.append(val)
        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))
    return out
```

## Complexity

* **Time:** O(n log k) for top-K, O(N log k) for merging K lists
* **Space:** O(k)

## Problems

- [ ] K Closest Points
- [ ] Merge K Sorted Lists
- [ ] Kth Largest Element in an Array
- [ ] Kth Smallest Element in a Sorted Matrix
- [ ] Top K Frequent Elements
- [ ] Reorganize String
- [ ] Ugly Number

## Mistakes

* Using a max-heap for "k largest" — it works but costs O(n log n) instead of O(n log k).
* Forgetting to negate consistently in a simulated max-heap (negate on push AND on read).
* Pushing a raw object with no ordering, causing a TypeError on the second comparison.
* Popping before checking `len(heap) > k`, so the heap never fills.
* Assuming the returned heap list is sorted — it is only heap-ordered.

## Keywords

* Heap
* Priority Queue
* Top K
* K Closest
* K Most Frequent
* Min-heap of Size K
* Merge K Lists
* Streaming
* Quickselect
