class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash={}
        for ele in nums:
            if ele in hash:
                hash[ele]+=1
                return True
            else:
                hash[ele]=1
        return False
                
        