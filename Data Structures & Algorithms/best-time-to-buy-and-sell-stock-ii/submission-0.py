class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        
        # Loop through the prices starting from the second day
        for i in range(1, len(prices)):
            # If the current day's price is higher than yesterday's, take the profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
                
        return max_profit