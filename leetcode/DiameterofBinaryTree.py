# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return -1

            right = dfs(root.right)
            left = dfs(root.left)
            res[0] = max(res[0], 2 + left + right)
