# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        waitfor = 1
        dummy = ListNode(next = head)
        prev = None
        while head:
            if waitfor == 1:
                prev = head
            elif waitfor == 0:
                prevval = prev.val
                prev.val = head.val
                head.val = prevval
                waitfor = 2
            head = head.next
            waitfor -= 1
        return dummy.next