from collections import deque
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        min_length = n + 1
        
        monoq = deque()
        
        for i, curr_sum in enumerate(prefix_sums):
            while monoq and curr_sum <= prefix_sums[monoq[-1]]:
                monoq.pop()
                
            while monoq and curr_sum - prefix_sums[monoq[0]] >= k:
                min_length = min(min_length, i - monoq.popleft())
                
            monoq.append(i)
        
        return min_length if min_length <= n else -1