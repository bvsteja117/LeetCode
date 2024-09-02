class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        allSum = 0
        
        for val in chalk:
            allSum += val
        
        mod = k % allSum
        
        n = len(chalk)
        
        for i in range(n):
            if chalk[i] > mod:
                return i
            
            mod -= chalk[i]
        
        return mod


        