# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Recursive solution
        if not head:
            return None

        if not head.next:
            return head

        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead