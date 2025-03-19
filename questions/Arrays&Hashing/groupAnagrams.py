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
            sortedS = ''.join(sorted(s)) # All strings must be sorted so we can detect the same ones like eat and tea they both will be "aet" . Cant use directly sorted(s) because it returns array.
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
            count = [0] * 26 # Create an array for 26 letters
            for c in s :
                count[ord(c) - ord('a')] += 1 # Increase by their count according to their occurence
            res[tuple(count)].append(s) # Tuple for using array as key.
        return list(res.values())
    

strs = ["act","pots","tops","cat","stop","hat"]
solTwo = SolutionTwo()
print(solTwo.groupAnagrams(strs))