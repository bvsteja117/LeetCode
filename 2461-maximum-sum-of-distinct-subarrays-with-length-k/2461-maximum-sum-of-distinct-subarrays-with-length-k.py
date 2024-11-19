class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
       
        if len(nums) < k:
            return 0
        
        window_sum = 0
        max_sum = 0
        left = 0
        seen = {}  # Dictionary to store element -> index mapping
        
        for right in range(len(nums)):
            while nums[right] in seen and seen[nums[right]] >= left:
                window_sum -= nums[left]
                left += 1
                
            window_sum += nums[right]
            seen[nums[right]] = right
            
            if right - left + 1 == k:
                max_sum = max(max_sum, window_sum)
                window_sum -= nums[left]
                left += 1
        
        return max_sum
