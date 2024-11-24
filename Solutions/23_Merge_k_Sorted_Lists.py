# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 0:
            return []
        if len(lists) == 1:
            return lists[0]

        # Time: O(nlogk)
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeLists(self, fl, sl):

        dummy = ListNode()  # Create a dummy head node
        fCurr = fl  # the current node of the first list
        sCurr = sl  # the current node of the second list
        rCurr = dummy  # the current node of the result list

        while fCurr and sCurr:
            if fCurr.val <= sCurr.val:
                rCurr.next = fCurr
                fCurr = fCurr.next
            else:
                rCurr.next = sCurr
                sCurr = sCurr.next
            rCurr = rCurr.next
        if fCurr:
            rCurr.next = fCurr
        if sCurr:
            rCurr.next = sCurr

        return dummy.next