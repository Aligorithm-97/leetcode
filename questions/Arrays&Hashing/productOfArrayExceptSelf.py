from collections import defaultdict
from typing import List

"""

Solution with Division
time : O(n)
space : o(1)

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,zero = 1,0
        for num in nums:
            if num:
                prod *= num
            else:
                zero += 1
        if zero > 1 : return [0] * len(nums)

        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zero : res[i] = 0 if c else prod
            else : res[i] = prod // c
        return res
    
sol = Solution()
print(sol.productExceptSelf([-1,0,1,2,3]))