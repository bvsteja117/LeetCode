class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=date.split('-')
        
        r=""
        for i in range(len(l)):
            t=(bin(int(l[i]))[2:])
            if i==0:
                r=t
            else:
                r=r+"-"+t
        return r
        