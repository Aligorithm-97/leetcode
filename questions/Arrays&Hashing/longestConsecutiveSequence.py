from collections import defaultdict
from typing import List

"""

Solution with Hash Set
time : O(n)
space : o(n)

"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest    

sol = Solution()
nums = [2,20,4,10,3,4,6]
print(sol.longestConsecutive(nums))


"""

Solution with Hash Set
time : O(n)
space : o(n)

"""


class SolutionTwo:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        res = 0
        for num in nums:
            if not mp[num]:
                mp[num] = mp[num-1]+ mp[num+1] + 1
                mp[num - mp[num-1]] = mp[num]
                mp[num + mp[num+1]] = mp[num]
                res = max(res, mp[num])
        return res
    
solTwo = SolutionTwo()
nums = [2,20,4,10,3,4,5]
print(solTwo.longestConsecutive(nums))