# LeetCode 84 - Largest Rectangle in Histogram

Pattern: Monotonic Stack

Difficulty: Hard

## Idea

Maintain a stack of indices with increasing bar heights. Append a sentinel 0 to the end of the heights list to force all remaining bars to be popped at the end.

Whenever the current bar is shorter than the bar at the top of the stack, pop that taller bar and compute the rectangle it could form: its height, and its width determined by the distance to the new stack top (or to the current index if the stack is empty).

Track the maximum area found across all pops.

## Complexity

* Time: O(n)
* Space: O(n) for the stack

## Mistakes

* Solved cleanly on the first accepted attempt. The sentinel 0 appended at the end is a key trick that avoids needing special-case cleanup code after the main loop to flush the remaining stack.

## Recognition

Look for this pattern when you have:

* Need the largest rectangle/area/span defined by consecutive elements bounded by a "shorter neighbor" constraint
* A monotonic stack efficiently finds, for each element, the nearest smaller elements on both sides

## Keywords

* Monotonic Stack
* Histogram
* Area Maximization
* Sentinel Value

## Similar Problems

* 42. Trapping Rain Water
* 85. Maximal Rectangle
* 496. Next Greater Element I