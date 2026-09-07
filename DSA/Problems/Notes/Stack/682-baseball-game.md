# LeetCode 682 - Baseball Game

Pattern: Stack

Difficulty: Easy

## Idea

Process each operation in order, using a stack (scores) to hold the running record's point values.

For "+", push the sum of the last two scores. For "D", push double the last score. For "C", pop the last score (cancel it). For any plain number, push its integer value directly.

The final answer is the sum of everything left on the stack.

## Complexity

* Time: O(n)
* Space: O(n)

## Mistakes

* Solved cleanly on the first accepted attempt. This is a very direct simulation problem; a stack naturally models "the last few scores" that operations like '+', 'D', and 'C' need to reference.

## Recognition

Look for this pattern when you have:

* A sequence of operations that reference recent history (the last one or two entries)
* Operations include "undo" (cancel) type actions
* A stack models the running history compactly

## Keywords

* Stack
* Simulation
* Running History
* Undo Operation

## Similar Problems

* 20. Valid Parentheses
* 155. Min Stack
* 71. Simplify Path