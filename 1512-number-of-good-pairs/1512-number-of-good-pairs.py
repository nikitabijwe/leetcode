class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict = defaultdict(int)
        ans = 0
        
        for num in nums:
            ans+=dict[num]
            dict[num]+=1
        return ans