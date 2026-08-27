# Divide and Conquer

**Category:** Divide and Conquer

## Recognition

* The problem splits cleanly into independent halves
* Merge sort / quick sort / quickselect
* Count inversions or "smaller numbers after self"
* Skyline problem
* Build a tree from traversals
* Recurrence of the form T(n) = 2T(n/2) + O(n)

## Tricks

* Three steps: divide, conquer (recurse), combine
* The interesting work almost always lives in the COMBINE step
* Merge-sort skeleton also counts inversions during the merge
* Quickselect: recurse into ONE side only, giving O(n) average
* Master theorem: 2T(n/2)+O(n) = O(n log n); 2T(n/2)+O(1) = O(n)
* Use a Fenwick tree / merge sort instead of nested loops for "count smaller to the right"

## Template

```python
def divide_and_conquer(arr, lo, hi):
    if lo >= hi:                        # base case: 0 or 1 element
        return base_value(arr, lo)
    mid = (lo + hi) // 2
    left = divide_and_conquer(arr, lo, mid)
    right = divide_and_conquer(arr, mid + 1, hi)
    return combine(left, right)         # the real work lives here
```

## Complexity

* **Time:** usually O(n log n); O(n) average when you recurse into one half only
* **Space:** O(log n) stack, plus O(n) if the combine step allocates

## Problems

- [ ] Divide and Conquer Intro
- [ ] The Skyline Problem
- [ ] Count of Smaller Numbers After Self
- [ ] Merge Sort / Advanced Sorting
- [ ] Reconstruct Binary Tree from Preorder and Inorder
- [ ] Kth Largest Element (quickselect)

## Mistakes

* `mid` split that does not shrink the problem (`lo, mid` and `mid, hi` — infinite recursion; use `mid + 1`).
* Base case at `lo == hi` when the combine step assumes at least 2 elements.
* Allocating a fresh list at every level, turning O(n log n) space into a memory problem.
* Forgetting that quicksort's worst case is O(n^2) on sorted input without a random pivot.
* Doing the counting work outside the merge, losing the log factor advantage.

## Keywords

* Divide and Conquer
* Merge Sort
* Quickselect
* Combine Step
* Master Theorem
* Count Inversions
* Recurrence
* Skyline
