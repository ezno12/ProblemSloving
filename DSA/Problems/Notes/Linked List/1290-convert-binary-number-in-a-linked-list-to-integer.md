# LeetCode 1290 - Convert Binary Number in a Linked List to Integer

Pattern: Linked List + Math

Difficulty: Easy

## Idea

Walk through the linked list from head to tail, appending each node's value (0 or 1) to a binary string.

Once the full string of bits is built, convert it to an integer using base 2 (int(bin_str, 2)).

## Complexity

* Time: O(n)
* Space: O(n) for the string (could be O(1) by accumulating value*2 + bit instead)

## Mistakes

* Solved cleanly on the first accepted attempt. A more space-efficient version would accumulate num = num * 2 + node.val while traversing, avoiding the intermediate string entirely.

## Recognition

Look for this pattern when you have:

* A linked list where each node represents a single bit
* Need to interpret the list as a single binary number

## Keywords

* Linked List
* Math
* Base Conversion
* Bit Accumulation

## Similar Problems

* 206. Reverse Linked List
* 67. Add Binary
* 191. Number of 1 Bits