# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # TC:O(N*log k) k is the number of linked list
        # SC: O(n)
        head = ListNode(0)  # create a New linked list with head
        curr = head  # make the curr point position at head
        heap = []  # create a heap list
        heapq.heapify(heap)

        for l in lists:
            while l:
                heapq.heappush(heap, l.val)  # each time we put the each node's value into heap
                l = l.next

        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next

        return head.next