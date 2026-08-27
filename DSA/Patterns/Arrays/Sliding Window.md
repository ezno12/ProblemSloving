# Sliding Window

**Category:** Arrays
**Variants:** Fixed Size, Flexible - Longest, Flexible - Shortest

A contiguous window that extends on the right and shrinks on the left. All three variants
share that skeleton; what differs is **when** you shrink and **when** you record the answer.
Get that pair right and the rest is bookkeeping.

| Variant | Inner loop | Record the answer |
|---------|-----------|-------------------|
| Fixed size k | none — remove left, add right each step | every step |
| Flexible, longest | `while invalid(window)` | **after** the loop |
| Flexible, shortest | `while valid(window)` | **inside** the loop, before removing |

## Recognition

* Contiguous / "subarray" / "substring"
* **Fixed:** window size k is given, max/min/average of every k-length slice, anagram of a fixed pattern
* **Longest:** "longest", "at most K distinct", "at most K replacements", "without repeating characters"
* **Shortest:** "shortest", "minimum length", "sum at least S", "contains all characters of T"

## Tricks

* Window length is `right - left + 1`
* Frequency map (`Counter`) for character windows; delete keys that drop to zero
* Fixed size: `left = right - window_size`, no separate left pointer needed
* Fixed size: keep a running sum instead of recomputing the window
* "At most K" is the natural fit; "exactly K" = `atMost(K) - atMost(K-1)`
* Shortest: need-map + a `missing` counter for "covers all of T"
* Shortest: initialize `ans = inf` and translate it back to 0 / "" at the end
* Monotonic deque when you need the window's max or min
* Negative numbers break the "sum at least S" monotonicity — use prefix sum + deque instead

## Template

```python
def sliding_window_fixed(input, window_size):
    ans = window = input[0:window_size]
    for right in range(window_size, len(input)):
        left = right - window_size
        remove input[left] from window
        append input[right] to window
        ans = optimal(ans, window)
    return ans


def sliding_window_flexible_longest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while invalid(window):        # update left until window is valid again
            remove input[left] from window
            left += 1
        ans = max(ans, window)        # window is guaranteed to be valid here
    return ans


def sliding_window_flexible_shortest(input):
    initialize window, ans
    left = 0
    for right in range(len(input)):
        append input[right] to window
        while valid(window):
            ans = min(ans, window)      # window is guaranteed to be valid here
            remove input[left] from window
            left += 1
    return ans
```

The three templates above are AlgoMonster's, kept verbatim — the natural-language lines
(`remove input[left] from window`) are pseudocode on purpose, so you fill in the window
state that the problem needs.

## Complexity

* **Time:** O(n) — each index enters and leaves the window at most once
* **Space:** O(k) for the window state, O(1) for a running sum

## Problems

- [ ] Subarray Sum - Fixed
- [ ] Maximum Average Subarray
- [ ] Find All Anagrams in a String
- [ ] Sliding Window Maximum (with monotonic deque)
- [ ] Sliding Window - Longest
- [ ] Longest Substring without Repeating Characters
- [ ] Longest Substring with At Most K Distinct Characters
- [ ] Fruits Into Baskets
- [ ] Longest Repeating Character Replacement
- [ ] Sliding Window - Shortest
- [ ] Least Consecutive Cards to Match
- [ ] Minimum Size Subarray Sum
- [ ] Minimum Window Substring

## Mistakes

* Don't forget to shrink.
* Shrinking on the wrong condition. For LONGEST you shrink while INVALID; for SHORTEST you shrink while VALID. Swapping them silently gives wrong answers.
* Updating the answer inside the shrink loop for the longest variant, or after it for the shortest variant.
* Using `if invalid(...)` instead of `while invalid(...)` — one shrink is not always enough.
* Computing length as `right - left` instead of `right - left + 1`.
* Not removing keys that drop to zero, so the distinct count stays too high.
* Fixed size: recomputing the whole window each step, which is O(nk) instead of O(n).
* Fixed size: forgetting to seed `ans` with the first window.
* Shortest: returning `inf` when no valid window exists instead of `0` / `""`.

## Keywords

* Sliding Window
* Fixed Window
* Flexible Window
* Contiguous
* Substring
* Subarray
* At Most K
* Frequency Map
* Shrink Condition
* Monotonic Deque
