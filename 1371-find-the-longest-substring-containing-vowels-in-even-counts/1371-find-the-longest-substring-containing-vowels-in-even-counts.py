class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        index = [-float('inf')] * 32  # Initialize the index array with negative infinity
        state = 0
        index[state] = -1  # Initial state

        for i in range(len(s)):
            ch = s[i]

            # Update the state if the character is a vowel
            for j in range(len(vowels)):
                if ch == vowels[j]:
                    state ^= 1 << j

            if index[state] == -float('inf'):
                index[state] = i

            max_length = max(max_length, i - index[state])

        return max_length