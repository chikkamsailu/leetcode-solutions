from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        missing_num = (n * (n + 1) // 2) - s  # use integer division
        return missing_num

