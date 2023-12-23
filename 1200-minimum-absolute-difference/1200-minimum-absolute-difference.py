class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        
        Input: arr = [4,2,1,3]
        Output: [[1,2],[2,3],[3,4]]
        """
        
        arr.sort()
        min_diff= float('inf')
        
        result=[]

        
        for i in range(len(arr)-1):
            min_diff= min(min_diff, arr[i+1] - arr[i])
            
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
            
            
            
            
            
                
                



        
                
                
                