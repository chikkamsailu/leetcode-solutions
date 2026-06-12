# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        dnum=0
        while head:
            dnum=dnum*2+head.val
            head=head.next
        return dnum
        
