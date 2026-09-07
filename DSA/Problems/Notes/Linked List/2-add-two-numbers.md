# LeetCode 2 - Add Two Numbers

Pattern: Linked List + Math + Recursion

Difficulty: Medium

## Idea

Simulate elementary school addition digit by digit, using a dummy head to build the result list.

At each step, take the current digit from l1 and l2 (0 if that list has ended), add them plus any carry from the previous step, and create a new node with total % 10 while carrying total // 10 forward.

Continue while either list still has nodes or there is a carry left over.

## Complexity

* Time: O(max(n, m))
* Space: O(max(n, m)) for the result list

## Mistakes

* Solved cleanly on the first accepted attempt. Key detail to remember: keep looping as long as l1, l2, OR carry is truthy, so a trailing carry (e.g. 9 + 9) still produces an extra node.

## Recognition

Look for this pattern when you have:

* Two linked lists representing numbers in reverse digit order
* Need to simulate arithmetic with carrying
* A dummy head simplifies building the result list

## Keywords

* Linked List
* Math
* Carry Propagation
* Dummy Node
* Simulation

## Similar Problems

* 445. Add Two Numbers II
* 67. Add Binary
* 43. Multiply Strings