"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hashmap = defaultdict(lambda: None)  # create a default dic to store the new linked list
        curr = head  # move the curr to the head (starting position)
        while (curr):  # when curr is not None
            if curr not in hashmap:  # if current node is not in the hashmap
                hashmap[curr] = Node(curr.val, None, None)  # we update this node in our hash map
            if curr.next != None:  # if the curr.next exist, we update the curr.next node in our hashmap
                if curr.next not in hashmap:
                    hashmap[curr.next] = Node(curr.next.val, None, None)
                hashmap[curr].next = hashmap[
                    curr.next]  # remember to make the current node point to the curr.next node in hashmap

            if curr.random != None:  # we do the exactly the same operation for random.
                if curr.random not in hashmap:
                    hashmap[curr.random] = Node(curr.random.val, None, None)
                hashmap[curr].random = hashmap[curr.random]

            curr = curr.next  # everytime we loop, we move the current to current.next

        return hashmap[head]  # return the final result in hashmap which is exatly the deep copy