# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxSum(root):
            if not root:
                return -math.inf, -math.inf
            leftMaxFound, leftMaxUsing = maxSum(root.left)
            rightMaxFound, rightMaxUsing = maxSum(root.right)
            val = root.val
            maxFound, maxUsing = max(val, val + rightMaxUsing, val + leftMaxUsing, val + leftMaxUsing + rightMaxUsing, leftMaxFound, rightMaxFound), max(val, val + rightMaxUsing, val + leftMaxUsing)
            print("At node " + str(root.val) + " Max found " + str(maxFound) + " Max using " + str(maxUsing))
            return maxFound, maxUsing
        
        print(maxSum(root))
        return maxSum(root)[0]