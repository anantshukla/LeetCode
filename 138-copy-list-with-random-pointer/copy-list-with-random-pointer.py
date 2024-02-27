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
        currPtr, oldToNewNodeMap = head, {None: None}

        while currPtr:
            copyNode = Node(currPtr.val)
            oldToNewNodeMap[currPtr] = copyNode
            currPtr = currPtr.next
        
        currPtr = head
        while currPtr:
            copyNode = oldToNewNodeMap[currPtr]
            copyNode.next = oldToNewNodeMap[currPtr.next]
            copyNode.random = oldToNewNodeMap[currPtr.random]
            currPtr = currPtr.next
        
        return oldToNewNodeMap[head]