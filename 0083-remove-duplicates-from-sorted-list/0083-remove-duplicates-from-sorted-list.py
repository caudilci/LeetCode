# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        previous = None
        while head:
            if previous and previous.val == head.val:
                previous.next = head.next
            else:
                previous = head
            head = head.next
        return dummy.next

        