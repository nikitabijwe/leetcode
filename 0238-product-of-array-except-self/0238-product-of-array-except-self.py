class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        answer = [0] * n
        
        answer[0]=1
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i -1]
            
        r = 1
        for i in reversed(range(n)):
            answer[i] = answer[i] * r
            r *= nums[i]
            
        return answer
            
            
#             nums = [1, 2, 3, 4]
#             answer= [1, 1, 2, 6]
#             answer = [nums[i-1]* answer[i-1]]
            
#             r=24
#             r = nums[i] * r
            
#             answer= [24, 12, 8, 6]
            
#             answer =. r * nums[i]
            
            
            
    
            
        

            