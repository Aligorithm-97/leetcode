from typing import List


"""

Solution with Two Pointers
time : O(n)
space : o(1)

Solution Explanation:
    We place two pointers: one at the beginning and one at the end.
        If the sum is greater than the target, we decrease the right pointer by one.
        If the sum is less than the target, we increase the left pointer by one until we find the target.

"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r-=1
            elif curSum < target:
                l+=1
            else:
                return [l+1 , r+1]
        return []


sol = Solution()
numbers = [1,2,3,4]
target = 4
print(sol.twoSum(numbers,target))