# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Solution 2
        # iteration: time: O(n), space: O(1)
        prev = None
        curr = head
        while (curr != None):  # use iteration, if current node is not None
            nextNode = curr.next  # define a nextNode = current.next
            curr.next = prev  # make the curr.next point to the previous one
            prev = curr  # assign current value to previous, thus curr.next point to curr
            curr = nextNode  # curr move to the next node.
        return prev  # return the tail which should be head for reversed list

        """
        #Solution 2 
        # recuesion: time: O(n), space: O(n)
        if not head or not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
        """