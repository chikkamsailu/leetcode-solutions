from math import gcd

class Solution:
    def countBeautifulPairs(self, nums: list[int]) -> int:
        def first_digit(x):
            while x >= 10:
                x //= 10
            return x
        
        count = 0
        n = len(nums)
        
        for i in range(n):
            fd = first_digit(nums[i])  
            for j in range(i+1, n):
                ld = nums[j] % 10       
                if gcd(fd, ld) == 1:
                    count += 1
                    
        return count

