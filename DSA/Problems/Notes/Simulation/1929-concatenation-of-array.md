# LeetCode 1929 - Concatenation of Array

Pattern: Simulation

Difficulty: Easy

## Idea

The result array is simply the original array followed immediately by another copy of itself.

Return nums[:] + nums[:] (or equivalently nums + nums), which directly builds the concatenated result.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Solved cleanly on the first accepted attempt. This is a very direct problem once you notice the definition literally describes list concatenation.

## Recognition

Look for this pattern when you have:

* A problem statement that literally describes a direct construction (concatenation, repetition, etc.)
* No hidden algorithmic trick is needed, just building the described structure directly

## Keywords

* Simulation
* Array Concatenation
* Direct Construction

## Similar Problems

* 1470. Shuffle the Array
* 1662. Check If Two String Arrays are Equivalent