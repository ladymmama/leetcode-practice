# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.diameter = 0
        self.helper(root)
        return self.diameter

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        self.diameter = max(self.diameter, left + right)  # update the results

        return 1 + max(left, right)  # we want to return the max length from each point
