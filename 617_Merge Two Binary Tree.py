# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        if t1 and t2:  # if both node are exist, we add their value
            res = TreeNode(t1.val + t2.val)
            res.left = self.mergeTrees(t1.left, t2.left)  # and do recursion for both the left and right part
            res.right = self.mergeTrees(t1.right, t2.right)
            return res
        else:  # if t1 or t2 is not exist at the same time, we return the exist node.
            return t1 or t2