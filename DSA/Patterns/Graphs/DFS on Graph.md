# DFS on Graph

**Category:** Graphs

## Recognition

* Connected components / flood fill
* Cycle detection in a directed graph
* Reachability ("can I get from A to B")
* Path enumeration
* Topological order via post-order
* Bipartite check / 2-colouring

## Tricks

* `visited` set is mandatory — graphs have cycles, trees do not
* Directed cycle detection needs THREE colours: unvisited / in-progress / done
* Post-order push + reverse = topological sort
* Iterative version with an explicit stack when recursion depth is a risk
* Count components: loop every node, run DFS from unvisited ones, increment

## Template

```python
def dfs(root, visited):
    for neighbor in get_neighbors(root):
        if neighbor in visited:
            continue
        visited.add(neighbor)
        dfs(neighbor, visited)
```

## Complexity

* **Time:** O(V + E)
* **Space:** O(V)

## Problems

- [ ] DFS on Graph
- [ ] Number of Islands
- [ ] Flood Fill
- [ ] Course Schedule (cycle detection)
- [ ] Pacific Atlantic Water Flow
- [ ] Number of Connected Components

## Mistakes

* Omitting `visited` — infinite recursion on the first cycle.
* Adding the start node to `visited` in the caller but not in the template (or the reverse), so it gets processed twice.
* Using a plain 2-state `visited` for directed cycle detection: a node seen on a *different* branch is not a cycle.
* Recursion limit on large graphs — `sys.setrecursionlimit` or go iterative.
* Treating an undirected edge as one-directional when building the adjacency list.

## Keywords

* DFS
* Connected Components
* Cycle Detection
* Three Colours
* Reachability
* Bipartite
* Post-order
* Recursion Limit
