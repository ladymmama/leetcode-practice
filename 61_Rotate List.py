# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast, curr = head, head, head
        _len = 0
        while curr:
            _len += 1
            curr = curr.next

        if k % _len == 0:
            return head

        k %= _len
        while k > 0:
            if fast.next:
                fast = fast.next
            k -= 1

        while fast.next:
            slow = slow.next
            fast = fast.next

        head2 = slow.next
        slow.next = None
        fast.next = head

        return head2
