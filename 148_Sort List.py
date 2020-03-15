# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        # TC: O(nlongn + n + n) = O(nlong) , SC: O(n)
        if not head or not head.next:
            return head

        curr = head
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next

        l.sort()
        ans_head = ListNode(0)
        ans = ans_head

        for i in l:
            ans.next = ListNode(i)
            ans = ans.next

        return ans_head.next
