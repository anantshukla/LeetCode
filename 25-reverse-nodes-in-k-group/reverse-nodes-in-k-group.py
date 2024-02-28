# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = prevGroupLastNode = ListNode(0, head)
        
        while True:
            currNode, ctr = prevGroupLastNode, k
            while currNode and ctr > 0:
                currNode = currNode.next
                ctr -= 1
            if not currNode:
                break

            lastNodeThisGroup, nextGroupStartNode = currNode, currNode.next

            prevNode, currNode = lastNodeThisGroup.next, prevGroupLastNode.next
            while currNode != nextGroupStartNode:
                nextNode = currNode.next
                currNode.next = prevNode
                prevNode = currNode
                currNode = nextNode
            
            thisGroupLastNode = prevGroupLastNode.next
            prevGroupLastNode.next = lastNodeThisGroup
            prevGroupLastNode = thisGroupLastNode
            
        return dummy.next
        