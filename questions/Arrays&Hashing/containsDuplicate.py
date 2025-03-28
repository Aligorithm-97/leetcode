from typing import List


"""

Solution with HashSet Length
time : o(n)
space : o(n)

Solution explanation : Simply put the nums into a set if there is a duplicate its length will be smaller.

"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
    
solution = Solution()
x = solution.hasDuplicate([1,2,3,4])

print(x)

"""

Solution with Sorting
time : o(nlogn)
space : o(n)

Solution explanation : Simply sort the numbers and compare one by one.
"""

class SolutionTwo:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        

solutionTwo = SolutionTwo()

x = solutionTwo.hasDuplicate([1,2,1,4])

print(x)