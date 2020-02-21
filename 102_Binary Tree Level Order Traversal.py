# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res

        queue = []
        queue.append(root)  # add root into queue

        while queue:  # when queue is not empty
            res.append([node.val for node in queue])  # put all node.val in the current level
            nqueue = []  # create a new queue to store the sub tree node

            for node in queue:  # find all node at the next level, add them to the queue
                if node.left:
                    nqueue.append(node.left)
                if node.right:
                    nqueue.append(node.right)

            queue = nqueue  # since we dont pop the result, we just simply raplace the current queue to next_level queue and loop

        return res