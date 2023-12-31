class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val=0
        total=0
        
        for num in nums:
            total+=num
            min_val=min(min_val, total)
        return -min_val+1