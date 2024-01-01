class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count=len(nums)
        
        idx=1
        
        for i in range(1, count):
            if nums[i-1]!=nums[i]:
                nums[idx]=nums[i]
                print(nums[idx],"nums[idx]")
                idx+=1
        print(idx, "idx")
        return idx
        
                
            