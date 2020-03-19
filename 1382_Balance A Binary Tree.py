# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        l = []
        self.getNode(root, l)
        return self.bst(l)

    def getNode(self, root, l):
        if not root:
            return None

        self.getNode(root.left, l)
        l.append(root.val)
        self.getNode(root.right, l)

    def bst(self, l):
        if not l:
            return
        _len = len(l)
        mid = _len // 2
        root = TreeNode(l[mid])
        root.left = self.bst(l[:mid])
        root.right = self.bst(l[mid + 1:])
        return root