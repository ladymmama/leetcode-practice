# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # TC:O(n) SC:O(1)
        if not head or not head.next:
            return head
        prev = newhead = ListNode(0)

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            prev.next = tmp
            prev = head
            head = head.next
        return newhead.next