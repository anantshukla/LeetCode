# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # TC: O(n), SC: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        rear, forward = head, head
        
        while rear and forward and forward.next:
            rear = rear.next
            forward = forward.next.next

            if forward == rear:
                return True
        return False



    # TC: O(n), SC: O(n)
    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     hs = set()
    #     ptr = head
    #     while ptr:
    #         if ptr in hs:
    #             return True
    #         hs.add(ptr)
    #         ptr = ptr.next
    #     return False

        