# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive
        if not root:
            return []
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

        # Iterative
        res = []
        stack = []
        cur = root
        while cur or stack:
            if not cur:
                cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            cur = cur.left
        return res