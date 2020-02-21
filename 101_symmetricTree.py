def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    else:
        return isMirror(root.left, root.right)


def isMirror(left, right):
    if not left and not right:
        return True
    elif not left or not right or left.val != right.val:
        return False
    return isMirror(left.left, right.right) and isMirror(left.right, right.left)

print(isMirror({1,2,2,3,4,4,3}))