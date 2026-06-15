class Solution:
    def reverseList(self, head):
        vals = []

        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        curr = head
        while curr:
            curr.val = vals.pop()
            curr = curr.next

        return head
        
