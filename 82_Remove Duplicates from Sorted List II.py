# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # TC:O(n), SC:O(n)
        if not head:
            return None
        curr = head
        val_list = []
        while curr:
            val_list.append(curr.val)
            curr = curr.next
        d = collections.Counter(val_list)

        cur = head
        prev = None
        while cur:
            if d[cur.val] > 1:
                if not prev:
                    head = cur.next
                    cur = cur.next
                else:
                    prev.next = cur.next
                    cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return head