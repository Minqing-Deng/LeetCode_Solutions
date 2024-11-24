# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()
        res = []

        if root:
            q.append(root)

        while q:
            temp = 0
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                temp += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(temp / length)

        return res