# LeetCode 11 - Container With Most Water

Pattern: Two Pointers + Greedy

Difficulty: Medium

## Idea

Start with left at 0 and right at the last index. The area is width * min(height[left], height[right]).

Always move the pointer with the smaller height inward, since keeping the taller side and moving the shorter one is the only way the area could possibly increase.

Track the maximum area seen throughout.

## Complexity

* Time: O(n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. The key greedy insight to remember is that moving the taller pointer can never improve the area, so it is always safe to move the shorter one.

## Recognition

Look for this pattern when you have:

* Need to maximize an area/product defined by two boundary elements
* A greedy argument shows one specific pointer must move at each step

## Keywords

* Two Pointers
* Greedy
* Area Maximization
* Monotonic Elimination

## Similar Problems

* 42. Trapping Rain Water
* 881. Boats to Save People
* 167. Two Sum II - Input Array Is Sorted