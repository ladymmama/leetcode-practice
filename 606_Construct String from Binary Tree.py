# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        return self.dfs(t)

    def dfs(self, node):
        if not node:
            return ''

        subleft = '({})'.format(self.dfs(
            node.left)) if node.left or node.right else ''  # if there is a left or right child, we should go deep for node.left.
        subright = '({})'.format(
            self.dfs(node.right)) if node.right else ''  # if there is no node.right, we dont need to go node.right
        return '{}{}{}'.format(node.val, subleft, subright)


