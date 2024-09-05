from collections import Counter

class Solution:
    
    def areOccurrencesEqual(self, s: str) -> bool:
        l=list(s)
        d=dict(Counter(l))
        l=[]
        for x in d.values():
            l.append(x)
        ir=l[0]
        for i in range(1,len(l)):
            if ir!=l[i]:
                return False
        return True

        