# LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String

Pattern: Sliding Window

Difficulty: Medium

## Idea

Use a variable-size sliding window with left and right pointers, expanding right and counting how many '1' characters (ones) are in the window.

Whenever the window contains exactly k ones, it is a candidate "beautiful" substring; compare it against the best answer found so far (shorter wins, and for equal length, lexicographically smaller wins), then shrink from the left to look for an even shorter valid window.

## Complexity

* Time: O(n) amortized (each window slice comparison can add overhead, making it closer to O(n^2) in the worst case due to string slicing)
* Space: O(n) for the candidate substrings

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail: after shrinking, the window is re-checked in the same while loop so that all valid minimal windows ending near this right pointer are considered, not just the first one found.

## Recognition

Look for this pattern when you have:

* Need the shortest substring satisfying a count-based condition (here, exactly k ones)
* A classic "shrink from the left while the condition still holds" sliding window shape

## Keywords

* Sliding Window
* Variable Size Window
* Lexicographic Comparison
* Substring Search

## Similar Problems

* 209. Minimum Size Subarray Sum
* 3. Longest Substring Without Repeating Characters
* 76. Minimum Window Substring