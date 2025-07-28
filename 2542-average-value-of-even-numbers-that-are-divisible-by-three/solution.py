class Solution:
    def averageValue(self, nums: list[int]) -> int:
        total = 0
        count = 0
        
        for n in nums:
            if n % 6 == 0:      # divisible by 2 and 3 (i.e., 6)
                total += n
                count += 1
        
        return total // count if count > 0 else 0






