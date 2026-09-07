# LeetCode 278 - First Bad Version

Pattern: Binary Search

Difficulty: Easy

## Idea

Binary search for the leftmost version that is bad, using the provided isBadVersion API as the check.

If isBadVersion(mid) is true, the first bad version is at mid or earlier, so move right to mid; otherwise, it must be later, so move left to mid + 1.

## Complexity

* Time: O(log n) API calls
* Space: O(1)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from moving right to mid - 1 instead of mid when isBadVersion(mid) is true, which can skip over the actual first bad version.

## Recognition

Look for this pattern when you have:

* A monotonic predicate (once true, stays true) over a range
* Need the boundary point (leftmost True), which is a classic "binary search on a predicate" pattern

## Keywords

* Binary Search
* Boundary Search
* Interactive
* Monotonic Predicate

## Similar Problems

* 704. Binary Search
* 744. Find Smallest Letter Greater Than Target
* 1095. Find in Mountain Array