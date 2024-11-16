class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []
        def isConsecutiveAndSorted(arr):
            if arr != sorted(arr):
                return False
            
            for i in range(1, len(arr)):
                if arr[i] != arr[i-1] + 1:
                    return False
            return True
        
        for i in range(n - k + 1):
            subarray = nums[i:i+k]
            
            if isConsecutiveAndSorted(subarray):
                results.append(max(subarray))
            else:
                results.append(-1)
        
        return results