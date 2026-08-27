# Matrix as Graph

**Pattern:** BFS on a Matrix (Matrix as Graph)
**Category:** Graphs

## Recognition

* Grid / 2D board
* Shortest path through cells
* Islands, regions, flood fill
* Minimum moves on a board (knight, maze)
* Spread over time (rot, fire, water)
* 4-directional or 8-directional movement

## Tricks

* Cell = node, adjacency = the 4 (or 8) in-bounds neighbours
* Delta arrays: `delta_row = [-1, 0, 1, 0]`, `delta_col = [0, 1, 0, -1]`
* Bounds check and the wall/obstacle check both live in `get_neighbors`
* Use the grid itself as `visited` (overwrite with a sentinel) to save memory
* Multi-source: enqueue every starting cell first
* Level counting gives the step count

## Template

```python
num_rows, num_cols = len(grid), len(grid[0])
def get_neighbors(coord):
    row, col = coord
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    res = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            res.append((neighbor_row, neighbor_col))
    return res

from collections import deque

def bfs(starting_node):
    queue = deque([starting_node])
    visited = set([starting_node])
    while len(queue) > 0:
        node = queue.popleft()
        for neighbor in get_neighbors(node):
            if neighbor in visited:
                continue
            # Do stuff with the node if required
            # ...
            queue.append(neighbor)
            visited.add(neighbor)
```

## Complexity

* **Time:** O(rows × cols)
* **Space:** O(rows × cols)

## Problems

- [ ] Matrix as Graph
- [ ] Flood Fill
- [ ] Number of Islands
- [ ] Knight Minimum Moves
- [ ] Walls and Gates / Zombie in Matrix
- [ ] Pacific Atlantic Water Flow

## Mistakes

* Swapping row and column somewhere in the delta arrays.
* Bounds check with `<=` instead of `<` on the upper limit.
* Assuming `len(grid[0])` is safe — guard against an empty grid.
* Using tuples as `visited` keys but lists as queue items (or vice versa), so lookups never match.
* Marking visited late in the matrix case too — same explosion as plain BFS.
* Forgetting the diagonal neighbours when the problem says 8-directional.

## Keywords

* Matrix as Graph
* Grid
* Delta Arrays
* Four Directions
* Flood Fill
* Islands
* Bounds Check
* In-place Visited
* Multi-source Spread
