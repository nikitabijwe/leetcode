class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val=float('inf')
        max_val=0
        
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            elif prices[i] - min_val > max_val:
                max_val= prices[i] - min_val
        return max_val
        
      