from typing import List

class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        cover = 0
        add = 0
        i = 0
        
        while cover < target:
            if i < len(coins) and coins[i] <= cover + 1:
                cover += coins[i]
                i += 1
            else:
                cover += cover + 1
                add += 1
        
        return add

        
