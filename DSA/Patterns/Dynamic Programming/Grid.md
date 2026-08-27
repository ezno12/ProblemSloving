# Grid

**Pattern:** DP - Grid
**Category:** Dynamic Programming

## Recognition

* 2D grid / matrix
* Count paths from corner to corner
* Minimum path sum / cost
* Obstacles blocking cells
* Movement restricted to right/down (no revisiting)
* Maximal square / rectangle of 1s

## Tricks

* `dp[r][c]` = best/count for reaching cell (r, c)
* `dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])`
* Pad with an extra row and column of sentinels to avoid boundary `if`s
* Obstacles: set `dp[r][c] = 0` (counting) or `inf` (minimizing) and move on
* Only the previous row is needed -> O(cols) space
* If movement is in ALL four directions, it is BFS/Dijkstra, not grid DP
* Maximal square: `dp[r][c] = 1 + min(up, left, up-left)` when `grid[r][c] == 1`

## Template

```python
def grid_dp(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                continue
            best = inf_or_zero
            if r > 0:
                best = combine(best, dp[r - 1][c])
            if c > 0:
                best = combine(best, dp[r][c - 1])
            dp[r][c] = best + grid[r][c]
    return dp[rows - 1][cols - 1]
```

## Complexity

* **Time:** O(rows × cols)
* **Space:** O(rows × cols), reducible to O(cols)

## Problems

- [ ] Unique Paths
- [ ] Unique Paths with Obstacles
- [ ] Minimum Path Sum
- [ ] Maximal Square
- [ ] Triangle
- [ ] Dungeon Game

## Mistakes

* Filling the first row/column inside the main loop and reading an out-of-range index.
* Using grid DP when movement allows going up or left — that breaks the acyclic order.
* Dungeon Game: iterating forward instead of BACKWARD from the princess.
* Sharing one row object across the DP table (`[[0] * cols] * rows` aliases every row).
* Adding `grid[r][c]` twice for the start cell.

## Keywords

* Dynamic Programming
* Grid DP
* 2D DP
* Unique Paths
* Minimum Path Sum
* Obstacles
* Padding
* Row Rolling
* Maximal Square
