# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = []
        toVisit = [root]
        while toVisit:
            current = toVisit.pop(0)
            if current:
                tree.append(current.val)
                toVisit.append(current.left)
                toVisit.append(current.right)
            else:
                tree.append(None)
        return str(tree)

            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def parse(text):
            if text == "None":
                return None
            else:
                return TreeNode(int(text))
        print(data.replace('[', '').replace(']', '').replace(' ', ''))
        tree = data.replace('[', '').replace(']', '').replace(' ', '').split(",")
        if not tree:
            return None
        root = parse(tree.pop(0))
        if not root:
            return root
        currentLevel = [root]
        while tree:
            newLevel = []
            for node in currentLevel:
                if node:
                    node.left = parse(tree.pop(0))
                    node.right = parse(tree.pop(0))
                    newLevel.append(node.left)
                    newLevel.append(node.right)
            currentLevel = newLevel

        return root
        

