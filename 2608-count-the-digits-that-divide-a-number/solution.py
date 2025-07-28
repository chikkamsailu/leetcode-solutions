class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for d in str(num):
            if num % int(d) == 0:
                count += 1
        return count

