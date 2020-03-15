# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # TC: O(n), SC:O(1)
        if not head:
            return head
        curr = head
        prev = None

        while m > 1:
            m -= 1
            n -= 1
            prev = curr
            curr = curr.next
        tail = curr
        last = prev

        while n:
            n -= 1
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        if last:
            last.next = prev
        else:
            head = prev

        tail.next = curr

        return head