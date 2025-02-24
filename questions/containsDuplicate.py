from typing import List


"""

Solution with HashSet Length
time : o(n)
space : o(n)

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
solution = Solution()
x = solution.hasDuplicate([1,2,3,4])

print(x)