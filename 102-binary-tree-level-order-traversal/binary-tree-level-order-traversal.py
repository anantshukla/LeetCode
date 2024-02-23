# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deque, ans = collections.deque([[root]]), []
        while deque:
            popped = deque.popleft()
            nodes_below, level_vals = [], []
            for node in popped:
                level_vals.append(node.val)
                if node.left:
                    nodes_below.append(node.left)
                if node.right:
                    nodes_below.append(node.right)
            if len(level_vals) > 0:
                ans.append(level_vals)
            if len(nodes_below) > 0:
                deque.append(nodes_below)
        print(ans)
        return ans
