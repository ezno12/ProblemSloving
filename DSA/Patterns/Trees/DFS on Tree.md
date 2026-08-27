# DFS on Tree

**Category:** Trees

## Recognition

* Tree traversal
* "Divide and conquer on a tree": answer for a node from answers of children
* Depth / height / diameter
* Path from root to leaf
* Search for a value
* Validate a structural property (balanced, BST, symmetric)

## Tricks

* Three questions: base case, what to return, what to do with children's returns
* Return a tuple / dataclass when you need more than one value up the tree
* Pass state DOWN as arguments (depth, parent, running path)
* Bubble state UP as the return value (height, count, subtree sum)
* Nonlocal / self.ans for a global best (diameter, max path sum)
* Preorder = act before recursing, postorder = act after

## Template

```python
def dfs(root, target):
    if root is None:
        return None
    if root.val == target:
        return root
    left = dfs(root.left, target)
    if left is not None:
        return left
    return dfs(root.right, target)
```

## Complexity

* **Time:** O(n)
* **Space:** O(h) recursion stack — O(log n) balanced, O(n) worst case

## Problems

- [ ] Max Depth of A Tree
- [ ] Visible Tree Node
- [ ] Balanced Binary Tree
- [ ] Subtree of Another Tree
- [ ] Invert Binary Tree
- [ ] Valid Binary Search Tree
- [ ] Lowest Common Ancestor

## Mistakes

* Missing the `root is None` base case.
* Returning early on the left branch without checking the right (or the reverse).
* Validating a BST with only `left.val < root.val < right.val` — you need a (min, max) range passed down.
* Mutating a shared path list without popping on the way out.
* Recursion depth on a degenerate (linked-list shaped) tree.

## Keywords

* DFS
* Recursion
* Post-order
* Pre-order
* Divide and Conquer on Tree
* Height
* Path
* Subtree
* Return Value vs Global
