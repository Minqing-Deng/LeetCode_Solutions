
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        # # BFS solution using queue, Time: O(n), Space: O(n)
        # if not root:
        #     return None

        # q = deque()
        # q.append(root)

        # while q:
        #     nextNode = None
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         node.next = nextNode
        #         nextNode = node
        #         if node.right:
        #             q.append(node.right)
        #         if node.left:
        #             q.append(node.left)

        # return root

        # DFS solution not using queue, Time: O(n), Space: O(1)
        if not root:
            return None

        cur = root
        next = root.left

        while next:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
            if not cur:
                cur = next
                next = cur.left

        return root