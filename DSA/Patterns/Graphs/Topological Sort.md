# Topological Sort

**Pattern:** Topological Sort (Kahn's Algorithm)
**Category:** Graphs

## Recognition

* Directed Acyclic Graph (DAG)
* Dependency / prerequisite ordering
* Task or course scheduling
* Build order, compilation order
* "Is there a valid order" / cycle detection in a directed graph
* Reconstruct a sequence from pairwise constraints

## Tricks

* Compute in-degrees, start the queue with every zero in-degree node
* Decrement neighbours; enqueue when a neighbour reaches in-degree 0
* `len(result) != len(graph)` means a cycle exists — return None / False
* Level-by-level processing gives the minimum number of rounds (task scheduling with parallelism)
* Unique order iff the queue never holds more than one node at a time
* Lexicographically smallest order: use a heap instead of a deque

## Template

```python
from collections import deque

def find_indegree(graph):
    indegree = { node: 0 for node in graph }  # dict
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1
    return indegree

def topo_sort(graph):
    res = []
    q = deque()
    indegree = find_indegree(graph)
    for node in indegree:
        if indegree[node] == 0:
            q.append(node)
    while len(q) > 0:
        node = q.popleft()
        res.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return res if len(graph) == len(res) else None
```

## Complexity

* **Time:** O(V + E)
* **Space:** O(V + E)

## Problems

- [ ] Topological Sort Intro
- [ ] Task Scheduling
- [ ] Task Scheduling 2
- [ ] Reconstructing Sequence
- [ ] Alien Dictionary
- [ ] Course Schedule

## Mistakes

* Forgetting the final `len(graph) == len(res)` cycle check.
* Building in-degrees only for nodes that appear as keys, missing sink nodes that only appear as neighbours.
* Decrementing in-degree at enqueue time instead of when the parent is processed.
* Getting the edge direction backwards — "A before B" means edge A -> B, so B's in-degree increases.
* Build the adjacency list and count in-degrees in the SAME direction. Reversed edges make cycles
* go undetected and acyclic graphs fail. *(Flagged on your own submissions — see Course Schedule.)*
* Alien Dictionary: only the FIRST differing character between adjacent words gives an edge, and a longer word before its own prefix is invalid.

## Keywords

* Topological Sort
* Kahn
* In-degree
* DAG
* Dependencies
* Prerequisites
* Cycle Detection
* Build Order
* Lexicographic Order
