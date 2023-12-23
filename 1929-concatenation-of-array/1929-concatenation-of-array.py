class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # return nums+nums
        
        ans = []
        for i in range(2):
            for y in range(len(nums)):
                ans.append(nums[y])
        return ans