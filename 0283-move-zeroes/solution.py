from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                if r != write:  # only swap when needed
                    nums[write], nums[r] = nums[r], nums[write]
                write += 1

