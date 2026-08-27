# Tree

**Pattern:** DP - Tree
**Category:** Dynamic Programming

## Recognition

* DP where the "sequence" is a tree, not an array
* Each node's answer built from its children's answers
* "Cannot pick a node and its child" (House Robber III)
* Diameter / longest path through a node
* Maximum path sum in a binary tree
* Counting subtrees with a property

## Tricks

* Post-order DFS: compute children first, then combine at the parent
* Return a TUPLE of the states you need, e.g. `(best_if_taken, best_if_skipped)`
* Two distinct quantities: what you RETURN upward vs the GLOBAL answer you record
* Diameter: return the height; record `left_height + right_height` in a nonlocal
* Topological-order DP is the general-graph version of this
* Memoization on node identity when the tree is a DAG

## Template

```python
def tree_dp(root):
    # returns (best_including_node, best_excluding_node)
    def dfs(node):
        if not node:
            return (0, 0)
        l_take, l_skip = dfs(node.left)
        r_take, r_skip = dfs(node.right)
        take = node.val + l_skip + r_skip          # cannot take children
        skip = max(l_take, l_skip) + max(r_take, r_skip)
        return (take, skip)

    return max(dfs(root))
```

## Complexity

* **Time:** O(n)
* **Space:** O(h) recursion stack

## Problems

- [ ] Tree DP Introduction
- [ ] House Robber III
- [ ] Binary Tree Maximum Path Sum
- [ ] Diameter of Binary Tree
- [ ] Longest Increasing Path in a Matrix (topological DP)
- [ ] Longest String Chain

## Mistakes

* Returning the global answer from the recursion instead of the per-node state (path-sum problems break here).
* Allowing a negative child contribution — clamp with `max(0, child)` for max-path-sum.
* Recomputing children (calling `dfs(node.left)` twice) and turning O(n) into O(2^n).
* Forgetting the `None` base case, or returning `(0, 0)` where `(-inf, 0)` is needed.
* Confusing "path through a node" (both children) with "path down from a node" (one child).

## Keywords

* Dynamic Programming
* Tree DP
* Post-order
* Take or Skip
* Tuple Return
* House Robber III
* Diameter
* Global vs Returned
