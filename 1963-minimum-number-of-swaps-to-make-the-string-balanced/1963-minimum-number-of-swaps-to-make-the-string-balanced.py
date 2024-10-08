class Solution(object):
    def minSwaps(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        max_imbalance = 0
        
        # Calculate the maximum imbalance at any point
        for char in s:
            if char == '[':
                balance += 1
            else:
                balance -= 1
            
            # Track the minimum balance (most negative point)
            max_imbalance = min(max_imbalance, balance)
        
        # Calculate the minimum number of swaps needed
        # Since max_imbalance is negative, take its absolute value
        return (-max_imbalance + 1) // 2
