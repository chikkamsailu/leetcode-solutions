from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        result = []
        n = len(nums)

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, value in count.items():
            if value > n // 3:
                result.append(key)

        return result
        
        
