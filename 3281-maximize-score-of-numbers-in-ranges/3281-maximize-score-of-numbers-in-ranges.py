class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)
        intervals = [(s, s + d) for s in start]
        intervals.sort()
        
        def check(score):
            last = float('-inf')
            for left, right in intervals:
                current = max(last + score, left)
                if current > right:
                    return False
                last = current
            return True
        
        left, right = 0, 2*10**9
        while left < right:
            mid = (left + right + 1) // 2
            if check(mid):
                left = mid
            else:
                right = mid - 1
        
        return left