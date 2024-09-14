class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)

        ans = 0
        cnt = 0

        for x in nums:
            if x == mx:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)

        return ans