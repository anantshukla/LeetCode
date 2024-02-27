# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = newList = ListNode(0)
        carry = 0
        while l1 and l2:
            sumNodes = l1.val + l2.val + carry
            carry = sumNodes // 10
            newList.next = ListNode(sumNodes % 10)

            l1, l2, newList = l1.next, l2.next, newList.next
        
        while l1:
            sumNodes = l1.val + carry
            carry = sumNodes // 10
            newList.next = ListNode(sumNodes % 10)
            l1, newList = l1.next, newList.next
        while l2:
            sumNodes = l2.val + carry
            carry = sumNodes // 10
            newList.next = ListNode(sumNodes % 10)
            l2, newList = l2.next, newList.next
        if carry > 0:
             newList.next = ListNode(carry)


        return dummy.next

        