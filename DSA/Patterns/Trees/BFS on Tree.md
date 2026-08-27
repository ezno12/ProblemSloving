# BFS on Tree

**Category:** Trees

## Recognition

* Level order traversal
* "Level by level" / "per row" output
* Shortest path in an unweighted tree
* Minimum depth
* Right / left side view
* Anything where DEPTH is the thing being measured

## Tricks

* `deque` + `while queue`; pop from the left, append children on the right
* Snapshot `len(queue)` at the top of the loop to process exactly one level
* Zigzag: reverse alternate levels (or `appendleft`)
* Right side view: take the last node of each level
* Minimum depth: return as soon as you hit the first leaf

## Template

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        for child in node.children:
            if is_goal(child):
                return FOUND(child)
            queue.append(child)
    return NOT_FOUND
```

## Complexity

* **Time:** O(n)
* **Space:** O(w) where w is the maximum level width — O(n) worst case

## Problems

- [ ] Binary Tree Level Order Traversal
- [ ] Binary Tree ZigZag Level Order Traversal
- [ ] Binary Tree Right Side View
- [ ] Binary Tree Min Depth

## Mistakes

* Reading `len(queue)` inside the level loop after you have already appended children — capture it first.
* Appending `None` children and then dereferencing them.
* Using a list with `pop(0)` instead of `deque.popleft()` — that turns O(n) into O(n^2).
* Not handling `root is None` before the first `deque([root])`.
* Using BFS for max depth where DFS is simpler, or DFS for min depth where BFS short-circuits.

## Keywords

* BFS
* Level Order
* Queue
* Deque
* Level Snapshot
* Minimum Depth
* Side View
* Zigzag
