from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]  # Mark as visited
        
        result = []
        for i, num in enumerate(nums):
            if num > 0:  # Indexes not visited
                result.append(i + 1)
        return result

