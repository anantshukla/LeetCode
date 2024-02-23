# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def getMaxSum(node, curSum):
            if node:
                curSum += node.val
                lSum = getMaxSum(node.left, curSum)
                rSum = getMaxSum(node.right, curSum)
                
                if not node.left and not node.right:
                    return curSum == targetSum
                return lSum or rSum
            return False
        return getMaxSum(root, 0)