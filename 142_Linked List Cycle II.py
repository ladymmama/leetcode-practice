# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # TC:O(n), SC:O(1)
        curr = head
        d = {}
        while curr:
            if curr in d:
                return curr
            d[curr] = 1
            curr = curr.next
        return None
