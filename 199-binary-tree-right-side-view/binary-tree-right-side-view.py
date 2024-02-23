# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deque, result = collections.deque([root]), []

        # BFS and add append all children to the right
        while deque:
            n, rightMost = len(deque), None
            for _ in range(n):
                node = deque.popleft()
                if node:
                    rightMost = node
                    deque.append(node.left)
                    deque.append(node.right)
            if rightMost:
                result.append(rightMost.val)
        return result
                