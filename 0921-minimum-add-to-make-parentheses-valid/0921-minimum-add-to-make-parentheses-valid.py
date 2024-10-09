class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance = 0
        moves = 0

        for char in s:
            if char == '(':
                balance += 1
            else:  # char == ')'
                balance -= 1

            # If balance goes negative, it means there are more ')' than '(' at this point
            if balance < 0:
                moves += 1
                balance = 0

        # Add remaining unmatched '(' to the moves count
        return moves + balance
