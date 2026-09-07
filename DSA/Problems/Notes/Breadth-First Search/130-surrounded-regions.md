# LeetCode 130 - Surrounded Regions

Pattern: Breadth-First Search (Multi-Source)

Difficulty: Medium

## Idea

Instead of checking every 'O' region for whether it touches the border (hard to do directly), flip the problem: start a multi-source BFS from every 'O' that is already ON the border.

Mark every 'O' reachable from the border as safe (they cannot be surrounded). After the BFS, any 'O' not marked safe is fully surrounded and should be flipped to 'X'.

## Complexity

* Time: O(rows * cols)
* Space: O(rows * cols) for the queue/visited tracking

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from trying to flood-fill from interior regions directly instead of starting from the border, which cannot correctly determine "surrounded" status in one pass.

## Recognition

Look for this pattern when you have:

* A grid problem where the "boundary" or "edge" cells behave differently from interior cells
* It is easier to mark what should NOT be changed (safe/reachable from border) than to detect what should

## Keywords

* Breadth-First Search
* Multi-Source BFS
* Grid/Matrix
* Border Flood Fill
* Union-Find (alternative)

## Similar Problems

* 200. Number of Islands
* 733. Flood Fill
* 417. Pacific Atlantic Water Flow