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
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Start reverse in-place
        prevNode, currNode = None, slow
        while currNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode, currNode = currNode, nextNode
        
        llHead = dummy = ListNode()
        
        leftNode, rightNode = head, prevNode

        while leftNode and rightNode:
            leftNext = leftNode.next
            rightNext = rightNode.next
            
            leftNode.next = rightNode
            rightNode.next = leftNext
            
            leftNode = leftNext
            rightNode = rightNext
        

        