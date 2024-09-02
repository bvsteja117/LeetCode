class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        r=k
        l=len(chalk)
        while True:
            for i in range(l):
                r=r-chalk[i]
                if r==0:
                    return i-2
                elif r<0:
                    return i


        