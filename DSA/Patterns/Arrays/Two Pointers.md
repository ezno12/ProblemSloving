# Two Pointers

**Category:** Arrays
**Variants:** Opposite Direction, Same Direction

Two indices walking the array under a stated invariant. Which direction they walk is the
whole decision. See also [Fast and Slow Pointers](Fast%20and%20Slow%20Pointers.md) for the
cycle-finding variant and [Sliding Window](Sliding%20Window.md) for the window variant.

## Recognition

**Opposite direction** (converge inward from both ends)

* Sorted array + target sum
* Palindrome check
* Pair / triplet from both ends
* Maximize area or width between two indices
* Reverse or partition in place (Dutch national flag)

**Same direction** (a slow write index and a fast scanner)

* In-place filter / compaction
* Remove duplicates
* Move / partition elements
* Linked list: n-th node from the end
* Read-ahead vs write-behind

## Tricks

* Opposite: `left = 0`, `right = n - 1`, move the pointer that cannot possibly improve the answer
* Opposite invariant: the answer, if it exists, is always inside `[left, right]`
* Skip duplicates after a match (3Sum family)
* Sort first when order does not matter
* Same: `slow` is the boundary of the finished region, `fast` is the scanner
* Same: `slow` only advances when you commit an element
* Same invariant: `arr[0:slow]` is always the finished answer — return `slow` as the new length
* Gap of exactly k between the pointers for "n-th from the end"

## Template

```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process current elements
        current = process(arr[left], arr[right])

        # Update pointers based on condition
        if condition(arr[left], arr[right]):
            left += 1
        else:
            right -= 1


def two_pointers_same(arr):
    slow, fast = 0, 0
    while fast < len(arr):
        # Process current elements
        current = process(arr[slow], arr[fast])

        # Update pointers based on condition
        if condition(arr[slow], arr[fast]):
            slow += 1

        # Fast pointer always moves forward
        fast += 1
```

## Complexity

* **Time:** O(n), or O(n log n) if you must sort first
* **Space:** O(1)

## Problems

- [ ] Two Sum Sorted
- [ ] Valid Palindrome
- [ ] Container With Most Water
- [ ] 3Sum
- [ ] Remove Duplicates
- [ ] Middle of a Linked List
- [ ] Move Zeros
- [ ] Remove N-th Node from End of Linked List

## Mistakes

* `while left <= right` when the two pointers must not meet, double-counting the middle element.
* Moving the wrong pointer — always justify the move with the invariant, not with intuition.
* Forgetting to skip duplicates, producing repeated triplets.
* Using the opposite-direction form on an unsorted array, where the monotonic argument does not hold.
* Advancing `slow` unconditionally — it must only move when you commit an element.
* Writing before reading, clobbering a value `fast` still needs.
* Off-by-one on the gap version: advance `fast` k+1 times, not k, when you need the node *before* the target.
* Returning the array instead of the new length when the problem asks for in-place length.

## Keywords

* Two Pointers
* Opposite Direction
* Same Direction
* Sorted Array
* Pair Sum
* Palindrome
* Invariant
* In-place
* Write Index
* Constant Space
