class Solution(object):
    def canArrange(self, arr, k):
        # Create a remainder frequency array to count occurrences of (arr[i] % k)
        remainder_count = [0] * k
        
        # Count the frequency of each remainder when dividing the array elements by k
        for num in arr:
            remainder = num % k
            # Handle negative remainders by making them positive
            remainder_count[remainder % k] += 1
        
        # Check for divisibility of pairs
        for i in range(1, k // 2 + 1):
            # Check if the count of remainders i and k-i are the same
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        # For the case where the remainder is exactly 0, the count must be even
        if remainder_count[0] % 2 != 0:
            return False
        
        return True

        