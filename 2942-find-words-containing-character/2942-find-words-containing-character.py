class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """

#         ans=[]
#         for i in range(len(words)):
#             for char in words[i]:
#                 if char ==x:
#                     ans.append(i)
#                     break
#         return ans


        ans=[]
        for i, char in enumerate(words):
            if x in char:
                ans.append(i)
        return ans
        
            