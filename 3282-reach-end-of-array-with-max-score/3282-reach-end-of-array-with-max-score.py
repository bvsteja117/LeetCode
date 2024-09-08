class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        res = ma = 0
        for a in nums:
            res += ma
            ma = max(ma, a)
        return res
        