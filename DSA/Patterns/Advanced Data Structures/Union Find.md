# Union Find

**Pattern:** Union Find (Disjoint Set Union)
**Category:** Advanced Data Structures

## Recognition

* Connected components in an UNDIRECTED graph
* "Are these two things in the same group"
* Dynamic connectivity (edges arrive over time)
* Merge accounts / emails / equivalent items
* Kruskal's MST
* Cycle detection in an undirected graph
* Offline problems processed in reverse (adding is easy, removing is not)

## Tricks

* Two operations only: `find` (with path compression) and `union`
* Path compression: `self.id[x] = self.find(parent)` on the way back up
* Union by rank/size keeps the tree shallow; you need BOTH it and path compression for the O(α(n)) bound
* Track component COUNT: start at n, decrement on every successful union
* Track component SIZE: keep a `size` dict and add on union
* `find(u) == find(v)` before union = cycle detected
* Deletion is not supported — reverse the timeline instead

## Template

```python
class UnionFind:
    def __init__(self):
        self.id = {}

    def find(self, x):
        y = self.id.get(x, x)
        if y != x:
            self.id[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.id[self.find(x)] = self.find(y)
```

## Complexity

* **Time:** O(log n) amortized with path compression alone (as in the template above);
  near O(1) — O(α(n)), inverse Ackermann — with path compression AND union by rank/size
* **Space:** O(n)

## Problems

- [ ] DSU Introductory Problem
- [ ] Size of Connected Components
- [ ] Merge User Accounts
- [ ] Number of Connected Components
- [ ] Umbristan | Reverse Union Find
- [ ] Redundant Connection

## Mistakes

* Setting `self.id[x] = y` (pointing at the parent) instead of `self.id[find(x)] = find(y)` (pointing root at root).
* Decrementing the component count on EVERY union call, including no-op unions of already-connected nodes.
* Using Union Find on a DIRECTED graph — it has no notion of direction.
* Skipping path compression and hitting O(n) finds on a degenerate chain.
* Comparing `x == y` instead of `find(x) == find(y)`.
* Leaving `find()` as a placeholder that returns its own argument. It type-checks, it runs, and it
* makes cycle detection and MST silently meaningless — every node looks like its own component.
*(Flagged on your own submissions — see Minimum Spanning Tree | Forests.)*

## Keywords

* Union Find
* Disjoint Set Union
* DSU
* Path Compression
* Union by Rank
* Connected Components
* Dynamic Connectivity
* Cycle Detection
* Reverse Timeline
