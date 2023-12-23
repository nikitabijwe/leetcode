class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums=set()
        
        for num in nums:
            if num!=0 and num not in unique_nums:
                unique_nums.add(num)
        return len(unique_nums)