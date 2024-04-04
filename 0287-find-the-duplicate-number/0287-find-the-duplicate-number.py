class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         # 'low' and 'high' represent the range of values of the target
#         low = 1
#         high = len(nums) - 1
        
#         while low <= high:
#             cur = (low + high) // 2
#             count = 0

#             # Count how many numbers are less than or equal to 'cur'
#             count = sum(num <= cur for num in nums)
#             if count > cur:
#                 duplicate = cur
#                 high = cur - 1
#             else:
#                 low = cur + 1
                
#         return duplicate
        
    # Phase 1: Detect if there's a cycle in the array
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
                
        # Phase 2: Find the entrance of the cycle
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
            
        return ptr1  # ptr1 (or ptr2) is the duplicate element