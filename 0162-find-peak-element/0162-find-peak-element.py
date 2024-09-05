class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        m=0
        for j in range(len(nums)):
            if nums[m]<=nums[j]:
                m=j
        return m
        