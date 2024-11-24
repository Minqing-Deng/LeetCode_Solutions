# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        def height(root):
            count = 0
            while root:
                root = root.left
                count += 1
            return count

        left_height = height(root.left)
        right_height = height(root.right)

        if left_height == right_height:
            # the left tree is a perfect tree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # the right tree is a perfect tree
            return (1 << right_height) + self.countNodes(root.left)