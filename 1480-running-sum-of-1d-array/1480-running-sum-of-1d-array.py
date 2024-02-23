class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # lst=[]
        # lst.append(nums[0])
        # for i in range(1, len(nums)):
        #     lst.append(nums[i]+lst[i-1])
        # return lst
            
            
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
