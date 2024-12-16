class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        arr = nums.copy()
    
        for _ in range(k):
            min_val = min(arr)
            min_index = arr.index(min_val)
            
            arr[min_index] *= multiplier
        
        return arr