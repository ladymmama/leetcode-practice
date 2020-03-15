# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        # TC: O(m+n) SC:O(1)
        p1 = headA
        p2 = headB
        while p1 != p2:
            if not p1:
                p1 = headB
            else:
                p1 = p1.next
            if not p2:
                p2 = headA
            else:
                p2 = p2.next
        return p1

        """
        curr = headA
        d = {}
        while curr:
            d[curr] = 1
            curr = curr.next
        now = headB
        while now:
            if now in d:
                return now
            now = now.next
        return None