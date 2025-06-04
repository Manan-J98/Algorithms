# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        length = 0
        res = 0
        ptr = head 
        while ptr :
            ptr = ptr.next
            length += 1
        length = length - 1
        ptr = head
        while length >= 0:
            res += int(ptr.val * math.pow(2, length))
            ptr = ptr.next
            length -= 1
        return res