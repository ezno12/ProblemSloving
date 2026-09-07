# LeetCode 496 - Next Greater Element I

Pattern: Monotonic Stack

Difficulty: Easy

## Idea

Process nums2 with a monotonic decreasing stack. For each number, pop every smaller element off the stack, since the current number IS their "next greater element"; record that mapping in a hash table.

Push the current number onto the stack, then continue.

After processing nums2, look up each value of nums1 in the hash table (defaulting to -1 if no greater element was ever found).

## Complexity

* Time: O(n + m)
* Space: O(n)

## Mistakes

* Solved cleanly on the first accepted attempt. The core insight is that a monotonic stack lets each element find its "next greater" in amortized O(1) per element, rather than an O(n^2) brute-force scan.

## Recognition

Look for this pattern when you have:

* Need to find, for each element, the next element to its right that is greater (or smaller)
* A decreasing (or increasing) monotonic stack processes this in a single linear pass

## Keywords

* Monotonic Stack
* Hash Table
* Next Greater Element

## Similar Problems

* 503. Next Greater Element II
* 84. Largest Rectangle in Histogram
* 739. Daily Temperatures