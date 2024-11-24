
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        dummy = Node(0)

        cur1 = head  # original list
        cur2 = dummy  # the copied list

        hashMap = {None: None}

        while cur1:
            temp = Node(cur1.val)
            hashMap[cur1] = temp
            cur2.next = temp
            cur2 = cur2.next
            cur1 = cur1.next

        cur1 = head  # original list
        cur2 = dummy.next  # the copied list

        while cur1:
            cur2.random = hashMap[cur1.random]
            cur2 = cur2.next
            cur1 = cur1.next

        return dummy.next