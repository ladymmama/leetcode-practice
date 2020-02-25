# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        res = []

        def preOrder(root):  # creat a helperfunction to help us do recursion
            if not root:  # if the root is empty, we return a "null"
                res.append('null')
                return
            else:
                res.append(str(root.val))  # each time we recurse, we add the curr root.val
                preOrder(root.left)  # first do the left part
                preOrder(root.right)  # then do the right part

        preOrder(root)  # start recursion with root
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:  # if its empty string, nothing to return
            return

        lst = data.split(',')  # first we need to split the input data
        return self.helper(lst)  # then we need to have a helper function to deseiralize

    def helper(self, l):
        while l:  # when list is not empty
            if l[0] == "null":  # if the first element is null, means there is no node
                l.pop(0)  # pop the first element
                return
            root = TreeNode(int(l.pop(0)))  # start with root node with the first element
            root.left = self.helper(l)  # after use the first element, pop it
            root.right = self.helper(l)  # do the same operation for root.left and root.right
            return root  # return the root node to show our tree

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))