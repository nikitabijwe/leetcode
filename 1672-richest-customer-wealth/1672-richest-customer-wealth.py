class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rich=float('-inf')
        
        for i in range(len(accounts)):
            sum1=sum(accounts[i])
            if sum1>rich:
                rich=sum1
            i+=1
        return rich
        
#         max_wealth_so_far = 0
        
#         # Iterate over accounts
#         for account in accounts:
#             # Add the money in each bank
#             curr_customer_wealth = sum(account)
#             # Update the maximum wealth seen so far if the current wealth is greater
#             # If it is less than the current sum
#             max_wealth_so_far = max(max_wealth_so_far, curr_customer_wealth)
            
#         # Return the maximum wealth
#         return max_wealth_so_far