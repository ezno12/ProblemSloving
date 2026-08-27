# Backtracking - Basic

**Pattern:** Backtracking - Basic (Enumerate All)
**Category:** Backtracking

## Recognition

* "Generate all" / "return all" / "list every"
* Permutations, subsets, combinations
* Partition a string / array
* Board placement (N-Queens, Sudoku)
* Combinatorial search where you must output the objects, not just count them

## Tricks

* Three decisions: state, what is a leaf, what are the edges
* `ans.append(path[:])` — append a COPY, not the live list
* Choose -> recurse -> un-choose (`path.pop()`)
* Prune early with `is_valid(edge)` instead of validating at the leaf
* `start_index` prevents re-using earlier elements (combinations vs permutations)
* Dedup: sort first, then `if i > start and arr[i] == arr[i-1]: continue`

## Template

```python
ans = []
def dfs(start_index, path, [...additional states]):
    if is_leaf(start_index):
        ans.append(path[:]) # add a copy of the path to the result
        return
    for edge in get_edges(start_index, [...additional states]):
        # prune if needed
        if not is_valid(edge):
            continue
        path.add(edge)
        if additional states:
            update(...additional states)
        dfs(start_index + len(edge), path, [...additional states])
        # revert(...additional states) if necessary e.g. permutations
        path.pop()
```

## Complexity

* **Time:** O(branching^depth × cost per leaf) — e.g. O(n · 2^n) subsets, O(n · n!) permutations
* **Space:** O(depth) for the stack + O(total output) for the answers

## Problems

- [ ] Generate All Phone Number Combinations
- [ ] Partition a String Into Palindromes
- [ ] Generate All Valid Parentheses
- [ ] Generate All Permutations
- [ ] Combination Sum
- [ ] Subsets

## Mistakes

* Appending `path` instead of `path[:]` — every entry in `ans` ends up empty or identical.
* Forgetting to revert (`path.pop()`, `used[i] = False`) after the recursive call.
* Using `start_index` for permutations (where every unused element is a valid edge) or omitting it for combinations (producing duplicates).
* Deduping with a `set` of tuples instead of pruning — works, but hides the real bug and costs memory.
* Pruning at the leaf instead of at the edge, so the search tree stays exponential.

## Keywords

* Backtracking
* Combinatorial Search
* Permutations
* Subsets
* Combinations
* Pruning
* Choose and Un-choose
* Start Index
* Deduplication
* Path Copy
