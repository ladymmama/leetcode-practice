# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # TC: O(n^2), SC:O(1)
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                tmp = head.next
                head.next = head.next.next
                p = dummy
                while p.next and p.next.val < tmp.val:  # if p.next.val is smaller than this node
                    p = p.next  # move to the right
                # when we end this loop, p.next.val is the first value that >= our node
                tmp.next = p.next  # our node is point to that p.next node
                p.next = tmp  # at the same time, p is smaller than our node, so p point to our node

        return dummy.next

