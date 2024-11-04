class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        i = 0
        
        while i < len(word):
            char = word[i]
            count = 1
            while i + count < len(word) and word[i + count] == char and count < 9:
                count += 1
            
            comp += str(count) + char
            
            i += count
        
        return comp
                