# LeetCode 1386 - Cinema Seat Allocation

**Pattern:** Bit Manipulation
**Difficulty:** Medium

## Idea

Store the reserved seats of each row as a **bitmask**. Then check the three possible 4-seat blocks (left, middle, and right) using bitwise `AND` to determine how many groups can fit in each affected row.

Rows with no reservations can always fit **2 groups**.

## Complexity

* **Time:** `O(m)`, where `m = len(reservedSeats)`
* **Space:** `O(m)`

## Mistakes

* Initially tried using a HashMap.
* Forgot that a sorted array can allow the use of two pointers.

## Recognition

Look for this pattern when you have:

* Fixed-size groups of seats
* Only a few valid seat blocks
* A need to check whether seats are reserved
* Very large `n`, but relatively few reserved seats

## Keywords

* Bitmask
* Bit Manipulation
* Hash Map
* Sparse Data
* State Representation
* Constant-Size Cases
* Efficient Lookup
* Set of Possibilities

## Similar Problems

* **1876.** Substrings of Size Three with Distinct Characters
* **89.** Gray Code
* **78.** Subsets
* **318.** Maximum Product of Word Lengths
