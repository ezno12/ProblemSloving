# LeetCode 744 - Find Smallest Letter Greater Than Target

Pattern: Binary Search

Difficulty: Easy

## Idea

Use binary search for the leftmost letter that is strictly greater than target.

If letters[mid] <= target, the answer must be to the right, so move left to mid + 1; otherwise, move right to mid (it could still be the answer).

If left wraps around past the end of the array, the answer wraps to letters[0].

## Complexity

* Time: O(log n)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail: this is a "search for the boundary" binary search (find leftmost element satisfying a condition), not a search for an exact match.

## Recognition

Look for this pattern when you have:

* A sorted array (letters here can repeat, and wrap around)
* Need the smallest/largest element satisfying an inequality, not an exact match

## Keywords

* Binary Search
* Boundary Search
* Sorted Array
* Wraparound

## Similar Problems

* 704. Binary Search
* 35. Search Insert Position
* 34. Find First and Last Position of Element in Sorted Array