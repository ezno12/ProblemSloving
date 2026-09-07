# LeetCode 412 - Fizz Buzz

Pattern: Simulation

Difficulty: Easy

## Idea

Iterate from 1 to n. For each number, check divisibility by 15 first (both 3 and 5), then by 3 alone, then by 5 alone, appending "FizzBuzz", "Fizz", or "Buzz" respectively; otherwise append the number itself as a string.

## Complexity

* Time: O(n)
* Space: O(n) for the result

## Mistakes

* Solved cleanly on the first accepted attempt. The key detail is checking divisibility by 15 FIRST, before checking 3 or 5 individually, since 3 and 5 alone would each match numbers divisible by 15 too.

## Recognition

Look for this pattern when you have:

* Need to classify numbers based on several divisibility rules
* Order of checks matters when conditions overlap (checking the most specific/combined condition first)

## Keywords

* Simulation
* Math
* Divisibility Rules
* Conditional Ordering

## Similar Problems

* 3622. Check Divisibility by Digit Sum and Product
* 1360. Number of Days Between Two Dates