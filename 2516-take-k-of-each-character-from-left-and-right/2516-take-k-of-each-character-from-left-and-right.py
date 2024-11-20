class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        count = {'a': 0, 'b': 0, 'c': 0}
        
        # Count total frequency of each char
        for c in s:
            count[c] += 1
            
        # Check if possible to get k of each
        if count['a'] < k or count['b'] < k or count['c'] < k:
            return -1
        
        ans = n  # Start assuming we need all characters
        l = 0
        window = {'a': 0, 'b': 0, 'c': 0}  # Count chars in current window
        
        # For each right boundary
        for r in range(n):
            window[s[r]] += 1  # Add right char to window
            
            # Shrink window from left while valid
            while window[s[r]] > count[s[r]] - k:
                window[s[l]] -= 1
                l += 1
                
            # Update answer: total length - window size
            ans = min(ans, n - (r - l + 1))
        
        return ans