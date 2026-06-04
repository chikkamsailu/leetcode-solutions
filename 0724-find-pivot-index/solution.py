class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tsum=sum(nums)
        lsum=0
        rsum=0
        for i, num in enumerate(nums):
            rsum=tsum-lsum-num
            if lsum==rsum:
                return i
            lsum+=num
        return -1
        
