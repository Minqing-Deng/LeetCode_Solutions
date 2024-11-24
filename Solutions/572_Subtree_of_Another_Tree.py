# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    #     # DFS solution
    #     if not subRoot:
    #         return True
    #     if not root:
    #         return False

    #     if self.isSameTree(root, subRoot):
    #         return True
    #     return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #     if p and q and p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     else:
    #         return False

        # BFS solution:
        q = deque()
        q.append(root)

        def is_same_tree(tree1, tree2):
            # Both are None
            if not tree1 and not tree2:
                return True
            # One is None but the other isn't
            if not tree1 or not tree2:
                return False
            # Compare values and recurse on both children
            return (tree1.val == tree2.val and
                    is_same_tree(tree1.left, tree2.left) and
                    is_same_tree(tree1.right, tree2.right))

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if is_same_tree(node, subRoot):
                    return True

        return False