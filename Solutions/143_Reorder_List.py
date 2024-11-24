# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second part
        cur = slow.next
        slow.next = None
        second = None # the head of the second part
        while cur:
            temp = cur.next
            cur.next = second
            second = cur
            cur = temp

        # Converge the two parts
        first = head
        while second:
            firstTemp = first.next
            secondTemp = second.next
            first.next = second
            second.next = firstTemp
            first = firstTemp
            second = secondTemp