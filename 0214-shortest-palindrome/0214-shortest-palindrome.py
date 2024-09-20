class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def compute_lps(s):
            n = len(s)
            lps = [0] * n
            length = 0  # Length of the previous longest prefix suffix
            i = 1
            while i < n:
                if s[i] == s[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # Reverse the string and create the combined string
        rev_s = s[::-1]
        combined = s + "#" + rev_s

        # Compute the longest prefix suffix (LPS) array for the combined string
        lps = compute_lps(combined)

        # The last value in the LPS array tells us the longest palindromic prefix
        longest_palindromic_prefix_length = lps[-1]

        # Add the remaining characters of the reversed suffix to the front of the string
        to_add = rev_s[:len(s) - longest_palindromic_prefix_length]
        return to_add + s