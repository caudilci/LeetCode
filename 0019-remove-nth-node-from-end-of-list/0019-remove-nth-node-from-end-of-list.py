# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        index = 0
        pointer = head
        while head:
            if index > n:
                pointer = pointer.next
            head = head.next
            index += 1
        if n >= index:
            return dummy.next.next
        elif pointer.next:
            pointer.next = pointer.next.next
            return dummy.next
        else:
            return dummy.next.next