class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_count = {}
        
        # Step 1: Count the number of occurrences of each prefix
        for word in words:
            prefix = ""
            for char in word:
                prefix += char
                if prefix in prefix_count:
                    prefix_count[prefix] += 1
                else:
                    prefix_count[prefix] = 1
        
        # Step 2: Calculate the sum of scores for each word based on the prefixes
        result = []
        for word in words:
            prefix = ""
            score = 0
            for char in word:
                prefix += char
                score += prefix_count[prefix]
            result.append(score)
        
        return result

        