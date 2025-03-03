import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k-1
            else:
                l = k+1
        return res
    

sol = Solution()
piles = [1,4,3,2]
piles2 = [24,10,23,4]
h2 = 4
h = 9
print(sol.minEatingSpeed(piles,h))
print(sol.minEatingSpeed(piles2,h2))