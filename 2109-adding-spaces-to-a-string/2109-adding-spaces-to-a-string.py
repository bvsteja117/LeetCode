class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        j = 0
        m = len(spaces)
        
        for i in range(len(s)):
            if j < m and i == spaces[j]:
                ans += " "
                j += 1
            ans += s[i]
        
        return ans