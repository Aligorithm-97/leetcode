# O(nlogn + mlogm)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
            
#         return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True

s = "racecar"
t = "carrace"

sol = Solution()
print(sol.isAnagram(s,t))
s = "jar" 
t = "jam"
print(sol.isAnagram(s,t))
