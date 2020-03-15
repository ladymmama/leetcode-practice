# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # TC:O(n), SC:O(1)
        if not head:
            return None

        slow = head
        fast = head
        prev = None
        while n != 0:
            n -= 1
            fast = fast.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        if prev:
            prev.next = slow.next
        else:
            head = slow.next
        return head