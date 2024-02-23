# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def getGoodCount(node, maxInRoute):
            if not node:
                return 0
            
            curMax = max(maxInRoute, node.val)
            goodCount = getGoodCount(node.left, curMax) + getGoodCount(node.right, curMax)

            if node.val >= maxInRoute:
                goodCount += 1
            return goodCount

        return getGoodCount(root, root.val)
        

        