class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        
        for char in s:
            # Check for "AB" or "CD" by comparing with the top of the stack
            if stack and ((stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D')):
                stack.pop()  # Remove the matched pair
            else:
                stack.append(char)
        
        # The length of the stack is the minimum possible length
        return len(stack)
