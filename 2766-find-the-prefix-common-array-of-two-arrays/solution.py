from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n + 1)   # values are 1..n
        res = [0] * n
        common = 0
        
        for i in range(n):
            # process A[i]
            val = A[i]
            freq[val] += 1
            if freq[val] == 2:
                common += 1
            
            # process B[i]
            val = B[i]
            freq[val] += 1
            if freq[val] == 2:
                common += 1
            
            res[i] = common
        
        return res

