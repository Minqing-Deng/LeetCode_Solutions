# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':

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
        # Iterate the tree level by level
        if not root:
            return None

        cur = root

        # Process level by level
        while cur:

            # A dummy node to keep track of the head of the next level
            dummy = Node()
            # 'tail' helps to connect the next level's nodes
            tail = dummy

            # Iterate over the current level
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                # Move to the next node in the current level
                cur = cur.next

            # Move to the first node of the next level
            # if it is a null node, that means no nodes in the next level
            cur = dummy.next

        return root