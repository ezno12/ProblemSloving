# LeetCode 1470 - Shuffle the Array

Pattern: Array (Direct Construction)

Difficulty: Easy

## Idea

The input array is structured as [x1,...,xn,y1,...,yn]. Build the result by iterating from 0 to n-1 and appending nums[i] (an x value) immediately followed by nums[n + i] (its corresponding y value).

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from an off-by-one in the index offset (n + i) used to locate the corresponding y value.

## Recognition

Look for this pattern when you have:

* An array with a known fixed structure (two concatenated halves) that must be interleaved
* Direct index arithmetic reconstructs the desired output without extra tricks

## Keywords

* Array
* Interleaving
* Direct Construction
* Index Arithmetic

## Similar Problems

* 1929. Concatenation of Array
* 1122. Relative Sort Array