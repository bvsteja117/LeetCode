class Solution(object):
    def minSubarray(self, nums, p):
        total_sum = sum(nums)
        remainder = total_sum % p
        
        if remainder == 0:
            return 0  # No need to remove anything
        
        prefix_sums = {0: -1}  # Maps prefix sum mod p to the index where it was first seen
        current_sum = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            current_sum += num
            current_sum %= p
            # We want (current_sum - target) % p == 0, or equivalently:
            target_sum = (current_sum - remainder) % p
            
            if target_sum in prefix_sums:
                # Calculate the length of the subarray
                min_length = min(min_length, i - prefix_sums[target_sum])
            
            # Store the current prefix sum modulo p
            prefix_sums[current_sum] = i
        
        return min_length if min_length < len(nums) else -1
