# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    # Space: O(h) using stack with iterative inorder traversal
    def __init__(self, root: Optional[TreeNode]):

        self.stack = []

        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:

        res = self.stack.pop()
        cur = res.right
        while cur:
            self.stack.append(cur)
            cur = cur.left
        return res.val

    def hasNext(self) -> bool:

        return self.stack != []

    # # Space: O(n) using array with recursive inorder traversal
    # def __init__(self, root: Optional[TreeNode]):

    #     self.array = []

    #     def inorder(root):
    #         if not root:
    #             return

    #         inorder(root.left)
    #         self.array.append(root.val)
    #         inorder(root.right)

    #     inorder(root)

    #     self.index = -1

    # def next(self) -> int:

    #     self.index += 1
    #     return self.array[self.index]

    # def hasNext(self) -> bool:

    #     if self.index + 1 == len(self.array):
    #         return False
    #     else:
    #         return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()