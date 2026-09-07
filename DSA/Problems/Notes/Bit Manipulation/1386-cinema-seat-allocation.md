# LeetCode 1386 - Cinema Seat Allocation

Pattern: Bit Manipulation + Greedy

Difficulty: Medium

## Idea

Represent each row's reserved seats as a bitmask, only tracking rows that actually have reservations (using a dictionary keyed by row number).

Precompute three bitmasks representing the "left group" (seats 2-5), "middle group" (seats 4-7), and "right group" (seats 6-9) of 4 consecutive seats.

For rows with no reservations at all, two families of 4 fit trivially. For rows with some reservations, check if the reserved bitmask overlaps with any of the three fixed 4-seat window masks; if a window is completely free (no bit overlap), a family of 4 can be seated there.

## Complexity

* Time: O(number of reserved seats)
* Space: O(number of rows with reservations)

## Mistakes

* Solved cleanly on the first accepted attempt. The key trick is using bitwise OR to combine multiple reservations into one mask per row, then bitwise AND to test overlap against the three candidate seat-window masks.

## Recognition

Look for this pattern when you have:

* A fixed small set of seats/positions per group (here, seats 2-9 in a row of 10)
* Need to check overlap between a "used" set and several fixed candidate patterns
* Bitmasks make overlap checks O(1) instead of iterating seat by seat

## Keywords

* Bit Manipulation
* Bitmask
* Greedy
* Hash Table (sparse row tracking)

## Similar Problems

* 645. Set Mismatch
* 338. Counting Bits
* 1004. Max Consecutive Ones III