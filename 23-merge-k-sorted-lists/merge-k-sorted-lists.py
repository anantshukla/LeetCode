# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mergedLists = []
        if not lists:
            return None
        ctr = 0
        while len(lists) > 1:
            print(ctr)
            ctr += 1
            head1 = lists.pop()
            head2 = lists.pop() if lists else None
            newList = self.mergeTwoLists(head1, head2)
            lists.append(newList)
            
        return lists[0] if lists else lists

    def mergeTwoLists(self, head1, head2):
        dummy = newPtr = ListNode()
        while head1 and head2:
            if head1.val > head2.val:
                newPtr.next = head2
                head2 = head2.next
            else:
                newPtr.next = head1
                head1 = head1.next
            newPtr = newPtr.next

        newPtr.next = head1 or head2
        return dummy.next

        