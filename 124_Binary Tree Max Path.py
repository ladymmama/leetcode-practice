# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float("-inf")  # initialize the res to make sure sum > res, res = sum
        self.dfs(root)  # start dfs
        return self.res

    def dfs(self, node):
        if not node:  # corner case
            return 0

        left = max(0, self.dfs(node.left))  # if there is negative return, we should change it to 0
        right = max(0, self.dfs(node.right))  # to make sure we always get the max num

        self.res = max(self.res, node.val + left + right)  # root must be used, and at least use one child

        return max(left, right) + node.val  # return max path
