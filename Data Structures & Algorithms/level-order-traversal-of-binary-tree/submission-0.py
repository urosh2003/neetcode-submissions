# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tree = []
        current = root
        level = [root]
        while level:
            newLevel = []
            thisLevel = []
            for node in level:
                if node:
                    thisLevel.append(node.val)
                    newLevel.append(node.left)
                    newLevel.append(node.right)
            if thisLevel:
                tree.append(thisLevel)
            level = newLevel
        return tree