# LeetCode 1 - Two Sum

Pattern: Hash Table

Difficulty: Easy

## Idea

Iterate through the array once, keeping a hash map (num_to_index) of value -> index seen so far.

For each number, compute its complement (target - num) and check if the complement already exists in the map; if it does, return the two indices immediately. Otherwise, store the current number and index.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from checking the map before it contained enough entries, or from an edge case with duplicate values where the same index gets reused incorrectly.

## Recognition

Look for this pattern when you have:

* An unsorted array
* Need to find a pair (or complement) satisfying a sum condition in O(n) time
* The array is not sorted, so a hash map lookup replaces a two-pointer approach

## Keywords

* Hash Table
* Complement Lookup
* One Pass
* Pair Sum

## Similar Problems

* 167. Two Sum II - Input Array Is Sorted
* 15. 3Sum
* 1679. Max Number of K-Sum Pairs