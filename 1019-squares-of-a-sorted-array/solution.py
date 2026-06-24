class Solution:
    def sortedSquares(self, nums):
        result = []

        for num in nums:
            result.append(num * num)

        result.sort()

        return result
