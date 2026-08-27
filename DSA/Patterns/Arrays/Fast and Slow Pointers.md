# Fast and Slow Pointers

**Pattern:** Fast and Slow Pointers (Cycle Finding)
**Category:** Arrays

## Recognition

* Linked list cycle detection
* Find the cycle entrance
* Middle of a linked list in one pass
* Happy number / functional graph iteration
* Duplicate number in `[1..n]` treated as a pointer chain
* No extra memory allowed

## Tricks

* `slow` moves 1 step, `fast` moves 2 — they meet iff there is a cycle
* Floyd phase 2: reset one pointer to head, advance both by 1, they meet at the cycle entrance
* Middle of list: when `fast` hits the end, `slow` is the middle
* Treat `i -> nums[i]` as an implicit linked list (the successor of index i is the value at i)

## Template

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def cycle_start(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:              # cycle confirmed
            slow = head
            while slow is not fast:   # both move 1 step now
                slow, fast = slow.next, fast.next
            return slow
    return None
```

## Complexity

* **Time:** O(n)
* **Space:** O(1)

## Problems

- [ ] Linked List Cycle
- [ ] Linked List Cycle II (entrance)
- [ ] Middle of a Linked List
- [ ] Happy Number
- [ ] Find the Duplicate Number

## Mistakes

* Checking `fast.next` before `fast` — order matters or you get an AttributeError.
* Comparing values (`slow.val == fast.val`) instead of identity (`slow is fast`).
* Starting `fast` at `head.next` and then using the phase-2 reset — the two conventions are not interchangeable.
* Assuming "meeting point == cycle start". It is not; phase 2 is required.

## Keywords

* Fast and Slow
* Floyd Cycle Detection
* Linked List Cycle
* Cycle Entrance
* Middle of List
* Functional Graph
* Constant Space
* Tortoise and Hare
