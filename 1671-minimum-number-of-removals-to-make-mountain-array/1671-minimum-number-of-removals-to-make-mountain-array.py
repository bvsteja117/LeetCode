class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        def LIS(A):
            d = []
            for a in A:
                i = bisect.bisect_left(d, a)
                if i < len(d):
                    d[i] = a
                elif not d or d[-1] < a:
                    d.append(a)
            return d.index(A[-1])

        for i in range(1, n-1):
            l, r = LIS(nums[:i+1]), LIS(nums[i:][::-1])
            if not l or not r: continue
            ans = min(ans, n - 1 - l - r)
        return ans
        