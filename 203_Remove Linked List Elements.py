# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # TC:O(n),SC:O(1)
        curr = head
        prev = None
        while curr:
            if curr.val == val:
                if not prev:
                    head = curr.next
                    curr = curr.next
                else:
                    prev.next = curr.next
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return head