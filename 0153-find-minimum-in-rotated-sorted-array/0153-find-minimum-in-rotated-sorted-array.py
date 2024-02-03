class Solution:
    def findMin(self, nums: List[int]) -> int:
        ele = nums[0]
        
        for i in range(len(nums)):
            if nums[i] < ele:
                ro = i - 0
                
                return nums[i]
                break
            
            
        return nums[0]
        
                