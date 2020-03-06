# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.helper(root, ans)
        return ans
    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left,res)
        self.helper(root.right, res)