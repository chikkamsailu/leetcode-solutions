from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set2 = set(nums2)  # for quick lookup
        set1 = set(nums1)
        
        answer1 = sum(1 for x in nums1 if x in set2)
        answer2 = sum(1 for x in nums2 if x in set1)
        
        return [answer1, answer2]

