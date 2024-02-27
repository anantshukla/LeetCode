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
            newPtr = oldToNewNodeMap[oldPtr]
            newPtr.next = oldToNewNodeMap[oldPtr.next]
            newPtr.random = oldToNewNodeMap[oldPtr.random]
            oldPtr = oldPtr.next
        return oldToNewNodeMap[head]