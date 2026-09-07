# LeetCode 20 - Valid Parentheses

Pattern: Stack

Difficulty: Easy

## Idea

Use a stack to track open brackets seen so far.

For every opening bracket, push it onto the stack. For every closing bracket, pop the top of the stack and check if that pair (popped + current) forms a valid bracket pair; if the stack is empty or the pair is invalid, the string is not balanced.

At the end, the string is valid only if the stack is completely empty.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Had a Wrong Answer attempt before the accepted one, likely from not checking whether the stack was empty before popping (which would crash or silently mismatch), or from an incomplete set of valid bracket pairs.

## Recognition

Look for this pattern when you have:

* A string of matched/nested symbols (brackets, tags, etc.) that must be validated
* A stack naturally tracks the "most recently opened, not yet closed" symbol

## Keywords

* Stack
* Bracket Matching
* Balanced Sequences
* Bracket Sequences

## Similar Problems

* 682. Baseball Game
* 32. Longest Valid Parentheses
* 1249. Minimum Remove to Make Valid Parentheses