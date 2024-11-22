class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt=Counter()
        for r in matrix:
            t=tuple(r) if r[0]== 0 else tuple(x^1 for x in r)
            cnt[t]+=1
        return max(cnt.values()) if cnt else 0