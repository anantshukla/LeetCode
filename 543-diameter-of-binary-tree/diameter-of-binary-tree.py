# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxHeight = 0
        def getDiameter(root):
            nonlocal maxHeight
            if not root:
                return 0
            
            lHeight = getDiameter(root.left)
            rHeight = getDiameter(root.right)
            maxHeight = max(maxHeight, lHeight + rHeight)

            return max(lHeight, rHeight) + 1
        
        getDiameter(root)
        return maxHeight