# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:  # if root is not exist, return []
            return res
        queue = []  # create a queue
        queue.append(root)  # we append the root

        while queue:  # while the queue is not empty

            res.append(queue[-1].val)  # append the last node which is the rightmost node
            nqueue = []

            for node in queue:  # if node.left, we add it to a new queue
                if node.left:
                    nqueue.append(node.left)
                if node.right:  # if node.right, we add it to a new queue
                    nqueue.append(node.right)

            queue = nqueue  # make the new queue becomes queue

        return res
