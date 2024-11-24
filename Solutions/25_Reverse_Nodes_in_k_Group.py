# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        def find_Kth(cur, k):
            while cur and k > 0:
                cur = cur.next
                k -= 1
            return cur

        groupPrev = dummy

        while True:
            kth = find_Kth(groupPrev, k)
            if not kth:
                break

            cur = groupPrev.next
            prev = kth.next
            groupNext = kth.next

            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next