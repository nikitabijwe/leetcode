class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        count=Counter(arr)

        
        n=len(count)

        count = sorted(count.values())
        
        for ele in count:
            k-=ele
            if k>=0:
                n-=1
            else:
                break
        return n
        