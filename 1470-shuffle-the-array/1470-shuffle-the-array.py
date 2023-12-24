class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result= [0] * (2*n)
        print(result)
        
        for i in range(n):
            print(range(n), "n")
            result[2*i]=nums[i]
            result[2*i+1]=nums[n+i]
        return result