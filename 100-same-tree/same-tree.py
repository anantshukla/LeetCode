# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1, q2 = [p], [q]
        while q1 and q2:
            t1, t2 = q1.pop(0), q2.pop(0)

            if not t1 and not t2:
                continue
            
            if (not t1 and t2) or (t1 and not t2) or t1.val != t2.val:
                return False
            
            q1.append(t1.left)
            q1.append(t1.right)
            q2.append(t2.left)
            q2.append(t2.right)
        
        return not q1 and not q2



        