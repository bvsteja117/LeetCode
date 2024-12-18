class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        answer = prices.copy()  # Initialize with original prices
        
        for i in range(n):
            # Find the first discount candidate to the right of current item
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    # Apply discount
                    answer[i] = prices[i] - prices[j]
                    break
        
        return answer
        