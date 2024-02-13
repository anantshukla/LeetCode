# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        deque = collections.deque()
        deque.append(root)
        outputList = []

        while deque:
            # BFS and add append all children to the right
            rightMostNode = None
            numOfElementsAtLevel = len(deque)
            for _ in range(numOfElementsAtLevel):
                node = deque.popleft()
                rightMostNode = node
                if node:
                    if node.left: deque.append(node.left)
                    if node.right: deque.append(node.right)
            if rightMostNode:
                outputList.append(rightMostNode.val)
        return outputList