# Trie

**Pattern:** Trie (Prefix Tree)
**Category:** Advanced Data Structures

## Recognition

* Prefix search / autocomplete
* "Words starting with ..."
* Dictionary of many words queried repeatedly
* Wildcard matching against a word set
* Word search on a board (Trie + backtracking)
* Longest common prefix, replace words
* Maximum XOR pair (binary trie)

## Tricks

* Node = a dict of `char -> Node`, plus an `is_word` flag
* `setdefault` builds the child in one line
* Store a `count` per node for prefix counting
* Insert all words once, then prune the DFS on the board when no child matches
* `.` wildcard: recurse into every child at that position
* Binary trie over 32 bits for XOR problems

## Template

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}

    def insert(self, s, idx):
        # idx: index of the current character in s
        if idx != len(s):
            self.children.setdefault(s[idx], Node(s[idx]))
            self.children.get(s[idx]).insert(s, idx + 1)
```

## Complexity

* **Time:** O(L) per insert or search, where L is the word length
* **Space:** O(total characters × alphabet) worst case

## Problems

- [ ] Trie Introduction
- [ ] Autocomplete
- [ ] Prefix Count
- [ ] Add and Search Words Data Structure
- [ ] Word Search II
- [ ] Implement Trie (Prefix Tree)

## Mistakes

* No `is_word` / end-of-word marker, so "app" matches when only "apple" was inserted.
* Confusing `search` (needs `is_word`) with `startsWith` (does not).
* Building a new Trie per query instead of once up front — the whole point is amortizing the build.
* Word Search II: not pruning dead branches, and forgetting to un-mark visited cells.
* Assuming lowercase-only input when the constraints allow more.

## Keywords

* Trie
* Prefix Tree
* Autocomplete
* Starts With
* Dictionary
* Wildcard
* End of Word Flag
* Binary Trie
* Word Search
