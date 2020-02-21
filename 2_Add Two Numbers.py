# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        answer = head
        
        while l1 and l2:
            add = l1.val + l2.val + carry   # the first digit in the result.
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10) #the second one 
            head = head.next                #move to the next head
            l1, l2 = l1.next, l2.next
        l = l1 if l1 else l2
        while l:                            #if l1 and l2 length is not match
            add = l.val + carry             # fo the same operation. 
            carry = 1 if add >= 10 else 0
            head.next = ListNode(add % 10)
            head = head.next
            l = l.next
        if carry:
            head.next = ListNode(1)         #if there is a carry after all the opreration, we should add one digit to our result
        return answer.next                  