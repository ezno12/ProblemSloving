# BFS on Graph

**Category:** Graphs

## Recognition

* Shortest path in an UNWEIGHTED graph
* Fewest steps / minimum moves
* Level-by-level expansion
* Connected components (BFS flavour)
* Multi-source spread (rotting oranges, walls and gates)
* Implicit graph: states as nodes, transitions as edges

## Tricks

* `visited` must be marked when you ENQUEUE, not when you dequeue
* Multi-source: seed the queue with every source before the loop
* Count levels with the `len(queue)` snapshot to get the distance
* Bidirectional BFS halves the frontier for Word Ladder-style problems
* For implicit graphs, encode state as a tuple/string and write `get_neighbors(state)`

## Template

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    visited = set([root])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
```

## Complexity

* **Time:** O(V + E)
* **Space:** O(V)

## Problems

- [ ] Shortest Path
- [ ] Clone Graph
- [ ] Word Ladder
- [ ] Open the Lock
- [ ] Sliding Puzzle
- [ ] Walls and Gates / Zombie in Matrix

## Mistakes

* Marking `visited` on dequeue — the same node gets enqueued many times and the queue explodes.
* Using BFS on a WEIGHTED graph and expecting the shortest path. That is Dijkstra.
* Forgetting to add the start node to `visited`.
* `list.pop(0)` instead of `deque.popleft()`.
* Not deduplicating implicit states, so an infinite state space never terminates.

## Keywords

* BFS
* Shortest Path
* Unweighted Graph
* Visited Set
* Multi-source
* Implicit Graph
* State Space
* Level Counting
* Bidirectional BFS
