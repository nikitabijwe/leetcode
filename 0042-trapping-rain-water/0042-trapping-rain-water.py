class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # height = [4,2,0,3,2,5]
        # max_op=(4-2)+(4-0)+(4-3)+(4-2)=2+4+1+2=9

#         n = len(height)

#         if n == 0:
#             return 0
#         left_max = [0] * n
#         right_max = [0] * n
#         left_max[0] = height[0]
#         for i in range(1, n):
#             left_max[i] = max(left_max[i - 1], height[i])
#         right_max[n - 1] = height[n - 1]
#         for i in range(n - 2, -1, -1):
#             right_max[i] = max(right_max[i + 1], height[i])
#         total_water = 0
#         for i in range(n):
#             total_water += min(left_max[i], right_max[i]) - height[i]
#         return total_water
        res=0
        n=len(height)
    
        if n==0:
            return 0
        
        left= [0] * n
        
        left [0]= height[0]
        for i in range(1, n):
            left[i]= max(left[i-1], height[i])
        right= [0] * n
        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i]=max(right[i+1], height[i])
            
        for i in range(n):
            res+=min(left[i], right[i]) - height[i]
        return res
            
        
        
