# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        self.helper(root, sum, res, [root.val])
        return res

    def helper(self, root, target, res, path):
        if not root:
            return

        if not root.left and not root.right and sum(path) == target:
            res.append(path)
            return
        if root.left:
            self.helper(root.left, target, res, path + [root.left.val])
        if root.right:
            self.helper(root.right, target, res, path + [root.right.val])