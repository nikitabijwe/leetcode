class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count=0
        n=len(nums)
        i=0
        j=n-1
  
        while i<j:
            if nums[i]+nums[j] < target:
                count+=j-i
                i+=1
            else:
                j-=1
        return count