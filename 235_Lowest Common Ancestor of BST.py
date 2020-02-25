# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode


        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val: # if all on the right
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val: # if all on the left
                curr = curr.right
            else:
                return curr
        """
        # same approch with recursion:

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root