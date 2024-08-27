class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        isPrime = {2: True, 3: True, 5: True, 7: True, 11: True, 13: True, 17: True, 19: True, 23: True, 29: True, 31: True}
        
        result = 0
        for i in range(left, right + 1):
            number = i
            bitCount = 0
            while number:
                number &= (number - 1)
                bitCount += 1
            
            result += isPrime.get(bitCount, False)
        
        return result
        