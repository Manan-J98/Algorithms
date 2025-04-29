# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftprev, p = dummy, head
        for i in range(left-1):
            p = p.next
            leftprev = leftprev.next
        
        prev = None
        for i in range(right-left+1):
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        leftprev.next.next = p
        leftprev.next = prev
        return dummy.next
