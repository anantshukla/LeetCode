# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, maxInRoute):
            nonlocal count
            if not node:
                return
            if node.val >= maxInRoute:
                maxInRoute = node.val
                count += 1
            
            dfs(node.left, maxInRoute)
            dfs(node.right, maxInRoute)
            
        dfs(root, root.val)
        return count

        