from collections import defaultdict
from typing import List


"""

Solution with Sorting
time : o(m * nlogn)
space : o(m * n)

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
    
strs = ["act","pots","tops","cat","stop","hat"]
sol = Solution()
print(sol.groupAnagrams(strs))
    


"""

Solution with Hash Table
time : o(m * n)
space : o(m)

"""

class SolutionTwo:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s :
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    

strs = ["act","pots","tops","cat","stop","hat"]
solTwo = SolutionTwo()
print(solTwo.groupAnagrams(strs))