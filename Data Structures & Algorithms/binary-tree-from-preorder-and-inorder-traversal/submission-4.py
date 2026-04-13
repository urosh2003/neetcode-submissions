# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder.pop(0))
        
        rootIndex = inorder.index(root.val)

        leftSubtree = self.buildTree(preorder[:rootIndex], inorder[:rootIndex])

        root.left = leftSubtree

        rightSubtree = self.buildTree(preorder[rootIndex:], inorder[rootIndex+1:])

        root.right = rightSubtree

        return root