class Solution(object):
    def maximumProfit(self, present, future, budget):
        """
        :type present: List[int]
        :type future: List[int]
        :type budget: int
        :rtype: int
        """
                    
    
        dp = [0] * (budget+1)
        for p, f in zip(present, future):
            for j in range(budget, p-1, -1):
                dp[j] = max(dp[j], dp[j-p] + f-p)
        return dp[-1]