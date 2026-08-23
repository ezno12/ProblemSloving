# LeetCode 167 - Two Sum II - Input Array Is Sorted

**Pattern:** Two Pointers
**Difficulty:** Medium

## Idea

Use two pointers because the array is **sorted**.

Start one pointer at the left (`left = 0`) and one at the right (`right = len(numbers) - 1`).

* If `numbers[left] + numbers[right] == target`, we found the answer.
* If the sum is **too small**, move `left` to the right to increase the sum.
* If the sum is **too large**, move `right` to the left to decrease the sum.

Because the array is sorted, every pointer movement eliminates impossible pairs.

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

## Mistakes

* Initially tried using a HashMap like the original Two Sum problem.
* Forgot that the array is already sorted, which makes the **two-pointer approach** possible.
* Used values instead of the required **1-based indices** in the final answer.

## Recognition

Look for this pattern when you have:

* A **sorted array**
* Need to find a pair satisfying a condition
* The condition involves the sum of two elements
* Need an efficient `O(n)` solution
* Can adjust the pair by moving from both ends

## Keywords

* Two Pointers
* Sorted Array
* Left Pointer
* Right Pointer
* Pair Sum
* Greedy Movement
* 1-Based Indexing
* Constant Space
* Monotonic Property

## Similar Problems

* **1.** Two Sum
* **15.** 3Sum
* **11.** Container With Most Water
* **125.** Valid Palindrome
* **344.** Reverse String
* **977.** Squares of a Sorted Array
