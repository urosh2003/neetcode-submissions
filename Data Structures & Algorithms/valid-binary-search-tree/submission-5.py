# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """def isValid(root):
            if root.left and not root.left.val < root.val:
                return False, 0, 0
            if root.right and not root.right.val > root.val:
                return False, 0, 0
            if not root.left and not root.right:
                return True

            if root.left:
                leftChild, minLeft, maxLeft = isValid(root.left)
            else:
                leftChild = True
                maxLeft = -math.inf
            if root.right:
                rightChild, minRight, maxRight = isValid(root.right)
            else:
                rightChild = True
                minRight = math.inf"""

        if not root:
            return True
        if root.left and not root.left.val < root.val:
            return False
        if root.right and not root.right.val > root.val:
            return False
        if not root.left and not root.right:
            return True

        if root.left:
            curr = root.left
            while curr.right:
                curr = curr.right
            if root.val <= curr.val:
                return False
        if root.right:
            curr = root.right
            while curr.left:
                curr = curr.left
            if root.val >= curr.val:
                return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)




        