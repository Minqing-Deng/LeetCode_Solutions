# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None

        q = deque()
        q.append(root)
        switch = 1
        res = []

        while q:
            temp = []
            for _ in range(len(q)):
                if switch:
                    node = q.popleft()
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                else:
                    node = q.pop()
                    temp.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)

            res.append(temp)
            switch = 1 - switch

        return res