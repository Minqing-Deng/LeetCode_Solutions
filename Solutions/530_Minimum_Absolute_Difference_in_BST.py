# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        stack = []
        cur = root
        pre = None
        res = float("inf")

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre:
                res = min(res, cur.val - pre.val)
            pre = cur
            cur = cur.right

        return res