# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        less = ListNode(0)
        greater = ListNode(0)

        cur = head
        curL = less
        curG = greater

        while cur:
            if cur.val < x:
                curL.next = cur
                curL = curL.next
            else:
                curG.next = cur
                curG = curG.next

            cur = cur.next

        curL.next = greater.next
        curG.next = None

        return less.next