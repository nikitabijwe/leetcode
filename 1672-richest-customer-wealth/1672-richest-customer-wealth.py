class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        rich=float('-inf')
        
        for i in range(len(accounts)):
            print(accounts[i])
            sum1=sum(accounts[i])
            print(sum1,"sum1")
            if sum1>rich:
                rich=sum1
                print(rich,"rich")
            i+=1
        return rich
        