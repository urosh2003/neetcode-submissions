# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def areTreesSame(root, subroot):
            if not root and not subroot:
                return True
            if not root:
                return False
            if not subroot:
                return False
            if root.val == subroot.val:
                return areTreesSame(root.left, subroot.left) and areTreesSame(root.right, subroot.right)
            else:
                return False

        if not subRoot and not root:
            return True
        if not root or not subRoot:
            return False

        if root.val == subRoot.val:
            if areTreesSame(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)