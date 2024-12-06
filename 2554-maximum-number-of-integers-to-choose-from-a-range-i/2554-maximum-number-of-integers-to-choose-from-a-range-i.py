class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
    
        banned_set = set(banned)
        
        selected = []
        current_sum = 0
        
        for num in range(1, n + 1):
            if num in banned_set:
                continue
            
            if current_sum + num <= maxSum:
                selected.append(num)
                current_sum += num
            else:
                break
        
        return len(selected)
            