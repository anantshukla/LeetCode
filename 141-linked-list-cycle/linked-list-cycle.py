# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1, ptr2 = head, head


    # TC: O(n), SC: O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hs = set()
        ptr = head
        while ptr:
            if ptr in hs:
                return True
            hs.add(ptr)
            ptr = ptr.next
        return False

        