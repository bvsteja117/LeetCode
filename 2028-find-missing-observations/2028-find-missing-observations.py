class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean * (m + n)
        given_sum = sum(rolls)
        missing_sum = total_sum - given_sum
        
        if n == 0 or missing_sum < n or missing_sum > 6*n:
            return []
        
        result = [missing_sum // n] * n
        remainder = missing_sum % n
        
        for i in range(remainder):
            result[i] += 1
        
        return result if all(1 <= x <= 6 for x in result) else []