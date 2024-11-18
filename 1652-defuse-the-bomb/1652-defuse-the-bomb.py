class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if n == 0:
            return []
        if k == 0:
            return [0] * n
            
        result = [0] * n
        
        for i in range(n):
            if k > 0:
                sum_val = 0
                for j in range(1, k + 1):
                    idx = (i + j) % n
                    sum_val += code[idx]
                result[i] = sum_val
            else:
                sum_val = 0
                for j in range(1, abs(k) + 1):
                    idx = (i - j + n) % n
                    sum_val += code[idx]
                result[i] = sum_val
                
        return result