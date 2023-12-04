# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:

#         degree=0
#         for ele in len(nums):
#             if nums[ele] not in lst:
#                 lst.append(nums[ele])
#                 else:
#                     increase the count of number
                    
#         degree= max count 
        
                
                
        
#         length=len(nums)
        
#         for i in len(nums):
#             result=length- nums[degree]
            
#         return result
    
    #         1. find max occurence of digits
#         2. maintain a count , which will update any small value > 0
        
#         3. 
        
#         length - (sum of index of first and last occurence)
        
        
#         1,2,2,2,3,4,5,5,2
        
#         num of occurence of 2 = 4
        
#         length=9
        
#         result=9-(1)=8

from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Create a dictionary to store the first and last occurrences of each number
        first_occurrence = {}
        last_occurrence = {}
        
        # Create a dictionary to store the count of each number
        count = defaultdict(int)
        
        # Iterate through the array to populate the dictionaries
        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            count[num] += 1
        
        # Find the degree of the array
        degree = max(count.values())
        
        # Initialize the result with the maximum possible length
        result = len(nums)
        
        # Iterate through the count dictionary to find the minimum length subarray
        for num, cnt in count.items():
            if cnt == degree:
                result = min(result, last_occurrence[num] - first_occurrence[num] + 1)
        
        return result