# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        mid = ListNode(0)  # dummy node to create a valid mid
        mid.next, tail = head, head

        while tail and tail.next:
            mid = mid.next
            tail = tail.next.next

        # cut the list to half
        temp = mid.next
        mid.next = None
        mid = temp

        # mid = self.get_mid(head)

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, left, right):

        if not left:
            return right
        if not right:
            return left

        dommy = ListNode(0)

        cur = dommy
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left
        else:
            cur.next = right

        return dommy.next

    # def get_mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     mid_prev = None
    #     while head and head.next:
    #         mid_prev = mid_prev.next if mid_prev else head
    #         head = head.next.next

    #     mid = mid_prev.next
    #     mid_prev.next = None

    #     return mid