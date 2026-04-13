# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inOrder(root):
            if not root:
                return []

            tree = []
            if root.left:
                tree += inOrder(root.left)
            tree.append(root.val)
            if root.right:
                tree += inOrder(root.right)

            return tree

        inorder = inOrder(root)
        return inorder[k-1]