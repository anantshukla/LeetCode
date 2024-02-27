"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldPtr, oldToNewNodeMap = head, {None: None}

        while oldPtr:
            oldToNewNodeMap[oldPtr] = Node(oldPtr.val)
            oldPtr = oldPtr.next
        
        oldPtr = head
        while oldPtr:
            copyNode = oldToNewNodeMap[oldPtr]
            copyNode.next = oldToNewNodeMap[oldPtr.next]
            copyNode.random = oldToNewNodeMap[oldPtr.random]
            oldPtr = oldPtr.next
        
        return oldToNewNodeMap[head]