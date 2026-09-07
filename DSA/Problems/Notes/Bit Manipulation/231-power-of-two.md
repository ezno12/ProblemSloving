# LeetCode 231 - Power of Two

Pattern: Bit Manipulation

Difficulty: Easy

## Idea

A power of two has exactly one bit set in its binary representation.

Use the trick n & (n - 1): for a power of two, this clears the single set bit, resulting in 0. Combined with checking n > 0 (to exclude zero and negatives), this confirms n is a power of two.

## Complexity

* Time: O(1)
* Space: O(1)

## Mistakes

* Solved cleanly on the first accepted attempt. The n & (n-1) == 0 trick is a fundamental bit manipulation identity worth memorizing; it also underlies counting set bits efficiently (see 338. Counting Bits).

## Recognition

Look for this pattern when you have:

* Need to check if a number is a power of two (or count/manipulate set bits)
* The n & (n-1) trick removes the lowest set bit in O(1)

## Keywords

* Bit Manipulation
* Power of Two
* Bitwise AND Trick

## Similar Problems

* 338. Counting Bits
* 191. Number of 1 Bits
* 342. Power of Four