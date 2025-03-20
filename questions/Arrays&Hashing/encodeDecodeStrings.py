from typing import List

"""

Solution Optimal
time : o(n)
space : o(1)

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" # ex/ hello : 5#hello
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
    

sol = Solution()
print(sol.encode(["a","code","b","you"]))
print(sol.decode(sol.encode(["a","code","b","you"])))