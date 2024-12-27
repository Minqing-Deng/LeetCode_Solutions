# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Inorder Iterative
        if not root:
            return None
        res, stack = [], []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


        # # Preorder Iterative
        # if not root:
        #     return None
        # res, stack = [], []
        # stack.append(root)

        # while stack:
        #     cur = stack.pop()
        #     res.append(cur.val)
        #     if cur.right:
        #         stack.append(cur.right)
        #     if cur.left:
        #         stack.append(cur.left)
        # return res


        # # Iterative approach for postorder traversal (left -> right -> root)
        # if not root:
        #     return []

        # res, stack = [], [root]
        # while stack:
        #     curr = stack.pop()
        #     res.append(curr.val)
        #     if curr.left:
        #         stack.append(curr.left)
        #     if curr.right:
        #         stack.append(curr.right)

        # # Since we visited root first, then right, then left, reverse the result to get left -> right -> root
        # return res[::-1]