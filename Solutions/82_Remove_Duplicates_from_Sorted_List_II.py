# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Since the head might be changed
        # Need a dummy head to deal with edge cases
        dummy = ListNode(0, head)

        pre = dummy  # the last node before the duplicates
        cur = head

        while cur:
            # check if the cur node is the beginning of the duplicates
            if cur.next and cur.val == cur.next.val:  # cur is the beginning of the duplicates
                # go through all the duplicates
                while cur.next and cur.val == cur.next.val:
                    cur.next = cur.next.next
                cur = cur.next
                # until here, cur is at the node after duplicates
                pre.next = cur
            else:  # cur is not the beginning of the duplicates
                pre = cur
                cur = cur.next

        return dummy.next