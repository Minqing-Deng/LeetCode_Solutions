# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow, fast = head, head
        count = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1

        length = count * 2 + 1 if fast else count * 2

        remove = length - n + 1  # the index need to remove

        dummy = ListNode(0, head)
        pre, cur = dummy, head

        for _ in range(remove - 1):
            pre = pre.next
            cur = cur.next

        # cur is at remove, pre is at the node before remove
        pre.next = cur.next

        return dummy.next