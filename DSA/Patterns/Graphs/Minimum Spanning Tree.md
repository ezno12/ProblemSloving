# Minimum Spanning Tree

**Pattern:** Minimum Spanning Tree (Kruskal / Prim)
**Category:** Graphs

## Recognition

* Connect all nodes at minimum total cost
* "Minimum cost to connect all points / cities / wells"
* Undirected, weighted graph
* Network / cabling / road-building framing
* Count or find critical (must-use) edges

## Tricks

* Kruskal = sort all edges by weight + Union Find, skip edges that would form a cycle
* Prim = grow one tree with a heap of frontier edges (better on dense graphs)
* Stop after V-1 accepted edges
* Disconnected graph -> no spanning tree exists (a "forest" instead)
* Low ROI in interviews, but it is the classic Union Find pay-off

## Template

```python
def kruskal(n, edges):                    # edges: list of (weight, u, v)
    uf = UnionFind()
    total, used = 0, 0
    for weight, u, v in sorted(edges):
        if uf.find(u) != uf.find(v):      # no cycle
            uf.union(u, v)
            total += weight
            used += 1
            if used == n - 1:
                break
    return total if used == n - 1 else None   # None = disconnected
```

## Complexity

* **Time:** O(E log E) for Kruskal, O(E log V) for Prim with a heap
* **Space:** O(V + E)

## Problems

- [ ] Introduction to Minimum Spanning Tree
- [ ] Minimum Spanning Tree | Forests
- [ ] Min Cost to Connect All Points
- [ ] Connecting Cities With Minimum Cost

## Mistakes

* Forgetting the `find(u) != find(v)` cycle guard, producing a cheap but invalid subgraph.
* Not checking that exactly V-1 edges were used before returning a total.
* Applying MST to a DIRECTED graph (that is arborescence, a different problem).
* Building the full O(n^2) edge list for a large geometric input without noticing the memory cost.
* Confusing MST with shortest path — MST minimizes total weight, not any single path.

## Keywords

* Minimum Spanning Tree
* Kruskal
* Prim
* Union Find
* Cycle Guard
* V-1 Edges
* Connect All Nodes
* Forest
