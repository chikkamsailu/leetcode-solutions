class Solution:
    def alternatingSum(self, nums):
        ans = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                ans += nums[i]
            else:
                ans -= nums[i]

        return ans
        
