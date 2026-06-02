class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d=dict()
        for i in range(3):
            d[i]=0
        for num in nums:
            d[num]=d[num]+1
        nums.clear()
        for (k,v) in d.items():
            for i in range(v):
                nums.append(k)
        
