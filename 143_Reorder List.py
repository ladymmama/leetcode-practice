# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # TC:O(n/2 + n/2 + n) = O(n) SC:O(1)
        if head and head.next and head.next.next:
            # find mid
            slow = head
            fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            head1 = head
            head2 = slow.next
            slow.next = None

            # reverse head2
            dummy = ListNode(0)
            dummy.next = head2
            curr = head2.next
            head2.next = None  # first node point to null since it becomes the tail
            while curr:
                temp = curr.next
                curr.next = dummy.next
                dummy.next = curr
                curr = temp

            head2 = dummy.next

            # merge 2 list
            p1 = head1
            p2 = head2
            while p2:
                temp1 = p1.next
                temp2 = p2.next
                p1.next = p2
                p2.next = temp1
                p1 = temp1
                p2 = temp2