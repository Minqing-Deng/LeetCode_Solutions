# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res

        # # Only beats 5.19%
        # def tree_height(root):
        #     if not root:
        #         return 0

        #     return 1 + max(tree_height(root.left), tree_height(root.right))

        # def dfs(root):
        #     if not root:
        #         return 0

        #     includeRoot = tree_height(root.left) + tree_height(root.right)

        #     return max(includeRoot, dfs(root.left), dfs(root.right))

        # return dfs(root)