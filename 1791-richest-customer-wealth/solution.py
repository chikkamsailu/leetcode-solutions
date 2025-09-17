from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxsum = 0
        m = len(accounts)
        for i in range(m):
            rowsum = sum(accounts[i])
            if rowsum > maxsum:
                maxsum = rowsum
        return maxsum
                  
