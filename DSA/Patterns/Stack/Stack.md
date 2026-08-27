# Stack

**Pattern:** Stack (LIFO)
**Category:** Stack

## Recognition

* Parentheses / brackets matching
* "Last opened, first closed" — anything nested
* Expression evaluation, basic calculator
* Undo history, backtracking a path
* Simplify a file path, remove adjacent duplicates
* Iterative tree/graph traversal (replacing recursion)
* Track a minimum alongside the stack (Min Stack)

## Tricks

* Brackets close in reverse order, so LIFO is the natural structure
* Push the EXPECTED closing bracket instead of the opening one — then compare directly
* Min Stack: store `(value, min_so_far)` pairs, or keep a second stack of minima
* Calculator: push the running result and the sign when you hit `(`, restore on `)`
* A Python `list` is the stack — `append` / `pop`; never `pop(0)`
* Empty-stack guard before every `pop` or `[-1]`
* If you also need the largest/smallest *ordered* candidate, you want a monotonic stack (22)

## Template

```python
def valid_parentheses(s):
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:   # guard THEN pop
                return False
    return not stack                                    # nothing left unclosed

class MinStack:
    def __init__(self):
        self.stack = []          # (value, min_so_far)

    def push(self, x):
        cur_min = x if not self.stack else min(x, self.stack[-1][1])
        self.stack.append((x, cur_min))

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def get_min(self):
        return self.stack[-1][1]
```

## Complexity

* **Time:** O(n) for a single pass; O(1) per push/pop/get_min
* **Space:** O(n)

## Problems

- [ ] Valid Parentheses
- [ ] Min Stack
- [ ] Basic Calculator
- [ ] Simplify Path
- [ ] Closest BST Values II (traversal without recursion)

## Mistakes

* Popping an empty stack — check `if not stack` before every `pop()` or `stack[-1]`.
* Returning `True` at the end without checking the stack is empty (`"(("` would pass).
* Using `pop(0)` and turning O(n) into O(n^2) — that is a queue operation.
* Calculator: forgetting that a sign applies to the whole parenthesised group, not just the next number.
* Reaching for a plain stack when the problem says "next greater" — that needs the monotonic variant.

## Keywords

* Stack
* LIFO
* Parentheses
* Brackets
* Nested
* Min Stack
* Expression Evaluation
* Iterative Traversal
* Empty Guard
