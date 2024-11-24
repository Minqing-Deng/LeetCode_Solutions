# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Recursive DFS solution:
        def dfs(root, leftBound, rightBound):
            if not root:
                return True
            if not (leftBound < root.val < rightBound):
                return False

            return dfs(root.left, leftBound, root.val) and dfs(root.right, root.val, rightBound)

        return dfs(root, float('-inf'), float('inf'))

        # # Iterative solution using inorder traversal
        # stack = []
        # cur = root
        # pre = TreeNode(float('-inf'))

        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
        #     cur = stack.pop()
        #     if pre.val >= cur.val:
        #         return False
        #     pre = cur
        #     cur = cur.right

        # return True