# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ptr = head
        prev = None
        if not head:
            return None
        while ptr:
            if ptr.val == val:
                if prev:
                    prev.next = ptr.next
                else:
                    head = head.next
            else:
                prev = ptr
            ptr = ptr.next
        return head
