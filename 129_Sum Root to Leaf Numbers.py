# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.total = 0
        if not root:
            return 0
        self.helper(root, root.val)
        return self.total

    def helper(self, root, path):
        if not root.left and not root.right:
            self.total += path
        if root.left:
            self.helper(root.left, path * 10 + root.left.val)
        if root.right:
            self.helper(root.right, path * 10 + root.right.val)
