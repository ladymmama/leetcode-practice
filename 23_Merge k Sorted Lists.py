# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        curr = head

        heap = []
        heapq.heapify(heap)
        for l in lists:
            while l:
                heapq.heappush(heap, l.val)
                l = l.next

        while heap:
            curr.next = ListNode(heapq.heappop(heap))  # curr is head, so head next is heappop value.
            curr = curr.next  # and we move the curr to curr. next

        return head.next