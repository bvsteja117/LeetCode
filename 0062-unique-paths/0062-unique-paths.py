class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        numerator = m + n - 2


        denominator = min(m, n) - 1
        result = 1

        for i in range(denominator):
            result = result * (numerator - i) // (i + 1)

        return result
