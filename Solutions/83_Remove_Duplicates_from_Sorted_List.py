# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        cur = head

        # Time: O(n), space: O(1)
        while cur:

            while cur.next and cur.val == cur.next.val:
                cur.next = cur.next.next

            cur = cur.next

        return head