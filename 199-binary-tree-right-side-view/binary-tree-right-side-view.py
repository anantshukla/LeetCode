# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deque, res = collections.deque([root]), []
        while deque:
            n = len(deque)
            rightMost = None
            for _ in range(n):
                node = deque.popleft()
                if node:
                    rightMost = node.val
                    deque.append(node.left)
                    deque.append(node.right)
            if rightMost != None:
                res.append(rightMost)
        return res
                