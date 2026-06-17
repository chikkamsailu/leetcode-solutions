class Solution:
    def modifiedList(self, nums, head):
        nums = set(nums)

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val in nums:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next
        
