# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # # recursive DFS
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # iterative BFS
        # q = deque()

        # if root:
        #     q.append(root)

        # level = 0

        # while q:
        #     for _ in range(len(q)): # the len(q) would calculate before the loop starts
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     level += 1

        # return level

        # iterative DFS (preorder)
        if not root:
            return 0

        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            res = max(res, depth)

            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])

        return res