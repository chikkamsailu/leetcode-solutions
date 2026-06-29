class Solution:
    def minOperations(self, nums):
        for num in nums:
            if num != nums[0]:
                return 1
        return 0
        
