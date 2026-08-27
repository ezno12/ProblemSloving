# Dijkstra

**Pattern:** Dijkstra (Shortest Path, Weighted Graph)
**Category:** Graphs

## Recognition

* Weighted graph, NON-negative weights
* Single-source shortest path
* "Minimum cost / time / effort to reach"
* Cheapest flights, network delay time
* Path with minimum maximum edge (swim in rising water) — same skeleton, different relax rule

## Tricks

* Priority queue of `(distance, node)` — a BFS where the queue is sorted by cost
* Lazy deletion: pop, and skip if `d > dist[node]` (no decrease-key needed)
* `dist` dict defaults to infinity
* Non-negative weights only — a negative edge breaks the "first pop is final" invariant
* Zero/one weights: use a deque (0-1 BFS) instead, it is O(V+E)
* Same skeleton with `max` instead of `+` solves bottleneck-path problems

## Template

```python
import heapq

def dijkstra(graph, source):
    dist = {source: 0}
    heap = [(0, source)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist.get(node, float('inf')):
            continue                      # stale entry
        for neighbor, weight in graph[node]:
            nd = d + weight
            if nd < dist.get(neighbor, float('inf')):
                dist[neighbor] = nd
                heapq.heappush(heap, (nd, neighbor))
    return dist
```

## Complexity

* **Time:** O((V + E) log V)
* **Space:** O(V + E)

## Problems

- [ ] Dijkstra's Algorithm | Shortest Path in a Weighted Graph
- [ ] Network Delay Time
- [ ] Cheapest Flights Within K Stops
- [ ] Path With Minimum Effort
- [ ] Swim in Rising Water

## Mistakes

* Using Dijkstra with negative edges (use Bellman-Ford).
* Using BFS on a weighted graph, or Dijkstra on an unweighted one (wasteful).
* Forgetting the stale-entry skip, which is correct but degrades performance badly.
* Pushing `(node, dist)` instead of `(dist, node)` — the heap then orders by node id.
* A "K stops" constraint makes the state `(node, stops)`, not just `node`.

## Keywords

* Dijkstra
* Weighted Graph
* Shortest Path
* Priority Queue
* Non-negative Weights
* Lazy Deletion
* Relaxation
* Bottleneck Path
* 0-1 BFS
