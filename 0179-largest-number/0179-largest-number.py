class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            # Compare two concatenations: xy and yx
            if x + y > y + x:
                return True  # x should come before y
            else:
                return False
        nums_str = [str(num) for num in nums]
    
        # Implement bubble sort based on our custom compare function
        n = len(nums_str)
        for i in range(n):
            for j in range(0, n - i - 1):
                if not compare(nums_str[j], nums_str[j + 1]):
                    # Swap if nums_str[j] + nums_str[j + 1] < nums_str[j + 1] + nums_str[j]
                    nums_str[j], nums_str[j + 1] = nums_str[j + 1], nums_str[j]
        
        # Join the sorted numbers
        result = ''.join(nums_str)
        
        # Handle edge case where all numbers are zeros
        return result if result[0] != '0' else '0'