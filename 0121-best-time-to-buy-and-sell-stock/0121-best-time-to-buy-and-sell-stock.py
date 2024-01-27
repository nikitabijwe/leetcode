class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        min_p= float('inf')
        
        for i in range(len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
            elif prices[i] - min_p > profit:
                profit = prices[i] - min_p
        return profit
        
            
        
        
            