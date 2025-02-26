"""

Solution with Reverse String
time : O(n)
space : o(n)

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
s = "Was it a car or a cat I saw?"
s2 = "tab a cat"
sol = Solution()
print(sol.isPalindrome(s))
print(sol.isPalindrome(s2))


"""

Solution with Two Pointers
time : O(n)
space : o(n)

"""

class SolutionTwo:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l+=1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True


    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    

s = "Was it a car or a cat I saw?"
s2 = "tab a cat"
solTwo = SolutionTwo()
print(solTwo.isPalindrome(s))
print(solTwo.isPalindrome(s2))