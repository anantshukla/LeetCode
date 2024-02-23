# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        deque, res = collections.deque([root]), []
        while deque:
            n = len(deque)
            levelValues = []
            for _ in range(n):
                node = deque.popleft()
                if node:
                    deque.append(node.left)
                    deque.append(node.right)
                    levelValues.append(node.val)
            
            if len(levelValues):
                res.append(levelValues)
        return res

