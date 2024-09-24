class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        def common_prefix_len(str1, str2):
            # Compare characters of str1 and str2 to find the common prefix length
            i = 0
            while i < len(str1) and i < len(str2) and str1[i] == str2[i]:
                i += 1
            return i

        max_prefix_len = 0

        # Convert integers to strings
        arr1_str = list(map(str, arr1))
        arr2_str = list(map(str, arr2))

        # Check all pairs from arr1 and arr2
        for x in arr1_str:
            for y in arr2_str:
                max_prefix_len = max(max_prefix_len, common_prefix_len(x, y))

        return max_prefix_len