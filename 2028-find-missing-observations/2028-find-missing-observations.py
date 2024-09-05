class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        ts= mean * (m + n)
        gs = sum(rolls)
        ms = ts-gs
        
        if n == 0 or ms < n or ms > 6*n:
            return []
        
        r = [ms // n] * n
        rem = ms % n
        
        for i in range(rem):
            r[i] += 1
        
        return r if all(1 <= x <= 6 for x in r) else []