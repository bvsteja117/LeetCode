class Solution:
    def hammingWeight(self, n: int) -> int:
        r=0
        a=format(n,'b')
        for i in a:
            if i=='1':
                r=r+1
        return r
        