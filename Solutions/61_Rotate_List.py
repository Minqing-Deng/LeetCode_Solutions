# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next or k == 0:
            return head

        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1

        if k % size == 0:
            return head

        k = k % size

        left, right = head, head
        for _ in range(k):
            right = right.next
        # right is k space far from left(head)

        while right and right.next:
            left = left.next
            right = right.next
        # left is at the node before the node shuld be the new head
        # right is at the tail

        new_head = left.next
        left.next = None
        right.next = head

        return new_head