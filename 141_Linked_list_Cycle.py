# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        # first solution: Hashtable  TC: O(n), Space: O(n)
        # go through each node one by one and record each node in hashtable.
        # if curr is none, we have reach the end so there is no cycle
        # if its in hash table, there is a cycle.

        d = {}
        curr = head
        while curr:
            if curr in d:
                return True
            else:
                d[curr] = 1
            curr =  curr. next   # curr point to the next node.
        return False

        """
        # second solution: 2 pointer with differnt speed.  Tc: O(n) worst should be O(n+k),  Space: O(1)
        if not head or not head.next:  # if head is null or head.next is null, no cycle
            return False

        slow = head  # since head,head.next is not null
        fast = head.next  # we assign this head,head.next to slow and fast.

        while slow != fast:  # when they are not meet each other
            if not fast or not fast.next:  # if fast reach the end, there is no cycle
                return False
            slow = slow.next  # slow move one step
            fast = fast.next.next  # fast move 2 step
        return True  # when the loops breaks, it means fast meet slow, it means there is a cycle.