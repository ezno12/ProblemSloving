# LeetCode 3622 - Check Divisibility by Digit Sum and Product

Pattern: Math

Difficulty: Easy

## Idea

Convert the number to a string to iterate over its digits.

Accumulate both the sum and the product of all digits in a single pass, then check whether the original number is evenly divisible by (sum + product).

## Complexity

* Time: O(digits)
* Space: O(digits) for the string conversion

## Mistakes

* Solved cleanly on the first accepted attempt. Straightforward digit-extraction problem; the main risk is forgetting to initialize the product to 1 (not 0) since it is a running multiplication.

## Recognition

Look for this pattern when you have:

* Need to compute both the sum and product of a number's digits
* A simple single-pass digit extraction and accumulation solves it directly

## Keywords

* Math
* Digit Extraction
* Sum and Product

## Similar Problems

* 4039. Sum of Decoded Numbers
* 258. Add Digits
* 1360. Number of Days Between Two Dates