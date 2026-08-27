# Monotonic Stack

**Category:** Stack

## Recognition

* "Next greater / next smaller element"
* "Previous greater / previous smaller element"
* Largest rectangle in a histogram
* Daily temperatures / waiting days
* Sliding window maximum (monotonic deque)
* Span / range where the current element dominates

## Tricks

* Decide the direction: decreasing stack -> next GREATER; increasing stack -> next SMALLER
* Store INDICES, not values, when you need distances
* Whatever you pop, the current element is its answer
* Sentinels: append a `0` (histogram) or `inf` to flush the stack at the end
* Circular arrays: iterate `2n` times with `i % n`
* Sliding window max = monotonic DEQUE (pop from both ends)

## Template

```python
def mono_stack(insert_entries):
    stack = []
    for entry in insert_entries:
        while stack and stack[-1] <= entry:
            stack.pop()
            # Do something with the popped item here
        stack.append(entry)
```

## Complexity

* **Time:** O(n) — each element is pushed and popped at most once
* **Space:** O(n)

## Problems

- [ ] Monotonic Stack Intro
- [ ] Daily Temperatures
- [ ] Next Greater Element II
- [ ] Largest Rectangle in Histogram
- [ ] Sliding Window Maximum
- [ ] Trapping Rain Water

## Mistakes

* `<` vs `<=` in the while condition — it decides how EQUAL elements are handled, which matters for histogram widths.
* Storing values when the problem needs index distance.
* Forgetting to flush the leftover stack after the loop (those elements have no next greater).
* Wrong stack direction — write down "I want next greater, so the stack is decreasing" before coding.
* Popping inside a `for` instead of a `while`, handling only one violation.

## Keywords

* Monotonic Stack
* Next Greater
* Next Smaller
* Decreasing Stack
* Histogram
* Indices not Values
* Sentinel
* Monotonic Deque
* Amortized O(n)
