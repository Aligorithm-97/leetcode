import heapq
from typing import List
"""

Solution with Sorting
time : O(nlogn)
space : o(n)

"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:    
            res[num] = 1 + res.get(num,0) # get if there is a value otherwise return 0. At this step we create frequency table

        arr = []
        for num ,cnt in res.items():
            arr.append([cnt,num]) # create frequency and number couples
        arr.sort() # sort them
        result = []
        while len(result) < k:
            result.append(arr.pop()[1]) # pop k times
        return res

 

sol = Solution()    

print(sol.topKFrequent([1,2,2,3,3,3],2))

"""

Solution with Heap
time : O(nlogk)
space : o(n+k)

Where n is the length of the array and k is the number of top frequent elements.

"""

class SolutionTwo:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        heap = []
        for num in count.keys():
            heapq.heappush(heap,(count[num],num)) # for this solution we use heap to get rid of sorting phase.
            if len(heap) > k:
                heapq.heappop(heap) # pop until k elements remains.
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # append remainings to res.
        return res

soltwo = SolutionTwo()
print(soltwo.topKFrequent([1,2,2,3,3,3],2))


"""

Solution with Bucket Sort
time : O(n)
space : o(n)

"""
class SolutionThree:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)] # Create a bucket 
        for num in nums:
            count[num] = 1 + count.get(num,0)
        print(count)
        for num,cnt in count.items(): # Use bucket sorting to avoid other types of sorting. With bucket sort we achieve o(n) instead of o(nlog(n))
            freq[cnt].append(num)
        print(freq)
        res = []
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                


solThree = SolutionThree()
print(solThree.topKFrequent([1,2,2,3,3,3],2))