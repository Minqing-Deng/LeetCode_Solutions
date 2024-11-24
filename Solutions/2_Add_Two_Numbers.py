# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2
        res = ListNode(-1)
        cur3 = res
        carry = 0

        while cur1 or cur2:

            if not cur1:
                num = 0 + cur2.val
                cur2 = cur2.next
            elif not cur2:
                num = cur1.val + 0
                cur1 = cur1.next
            else:
                num = cur1.val + cur2.val
                cur1 = cur1.next
                cur2 = cur2.next

            num += carry
            digit = num % 10
            carry = num // 10

            temp = ListNode(digit)
            cur3.next = temp
            cur3 = cur3.next

        if carry != 0:
            temp = ListNode(carry)
            cur3.next = temp

        return res.next