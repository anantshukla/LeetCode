# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hs = set()
        ptr = head
        while ptr:
            if ptr in hs:
                return True
            hs.add(ptr)
            ptr = ptr.next
        return False
        # ptr1, ptr2 = head, head

        # while ptr1 and ptr2.next:
        #     ptr1 = ptr1.next
        #     ptr2 = ptr2.next.next

        #     if ptr1.val == ptr2.val:
        #         return True
        # return False

        