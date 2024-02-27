# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Reverse the second half of the linkedList
        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        # Start reverse in-place
        prevNode, currNode = None, slow
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode, currNode = currNode, nextNode
        
        leftNode, rightNode = head, prevNode
        
        # Merge
        while leftNode and rightNode:
            leftNext, rightNext = leftNode.next, rightNode.next
            leftNode.next, rightNode.next = rightNode, leftNext
            leftNode, rightNode = leftNext, rightNext
        