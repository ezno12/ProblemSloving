# LeetCode 1927 - Sum Game

Pattern: Game Theory + Greedy

Difficulty: Medium

## Idea

Split the string into left and right halves. Compute the known digit sum and the count of '?' placeholders in each half.

If the number of unknowns on both sides is equal (L == R), the second player can always mirror the first player's moves to keep the sums equal, so Alice wins only if the known sums already differ (sum_left != sum_right).

If the unknown counts differ, compute the net advantage using the formula 2 * (sum_left - sum_right) + 9 * (L - R); Alice wins whenever this value is non-zero, since it represents the guaranteed final imbalance under optimal play from both sides.

## Complexity

* Time: O(n)
* Space: O(1) extra (beyond string slicing)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from the special-case formula when L == R being mishandled, or from an error in deriving the general imbalance formula.

## Recognition

Look for this pattern when you have:

* A two-player alternating game where both players play optimally
* Need to determine a winner based on a mathematical invariant rather than simulating every possible game

## Keywords

* Game Theory
* Greedy
* Math
* Optimal Play Invariant

## Similar Problems

* 292. Nim Game
* 877. Stone Game
* 1406. Stone Game III