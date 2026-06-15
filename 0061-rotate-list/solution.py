class Solution:
    def rotateRight(self, head, k):
        if not head:
            return head

        vals = []
        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next

        k = k % len(vals)
        vals = vals[-k:] + vals[:-k]

        curr = head
        for val in vals:
            curr.val = val
            curr = curr.next

        return head
        
