# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque([root])
        output = []

        while q:
            levelValues = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                if node:
                    levelValues.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if len(levelValues):
                output.append(levelValues)

        return output