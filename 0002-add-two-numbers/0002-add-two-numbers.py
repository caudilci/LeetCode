# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy
        current = 0
        carry = 0

        while l1 or l2 or carry:
            current = carry
            if l1:
                current += l1.val
                l1 = l1.next
            if l2:
                current += l2.val
                l2 = l2.next
            num = current % 10
            carry = current // 10
            dummy.next = ListNode(val=num)
            dummy = dummy.next

        return result.next