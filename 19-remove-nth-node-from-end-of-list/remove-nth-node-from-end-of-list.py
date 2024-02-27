# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        frontPtr = dummy = ListNode()
        frontPtr.next = head
        ctr = n
        while ctr > 0:
            frontPtr = frontPtr.next
            ctr -= 1
        backPtr = dummy

        while frontPtr and frontPtr.next:
            frontPtr, backPtr = frontPtr.next, backPtr.next
        
        backPtr.next = backPtr.next.next

        return dummy.next


        