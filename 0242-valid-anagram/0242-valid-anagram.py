class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
#         if len(s)!=len(t):
#             return false
        
#         s=sorted(s)
#         t=sorted(t)
        
#         return s == t


        if len(s)!=len(t):
            return False
        
        dict={}
        
        for char in s:
            if char not in dict:
                dict[char]=1
            else:
                dict[char]+=1
                
        for char in t:
            if (char not in dict) or (dict[char]==0):
                return False
            dict[char]-=1
        return True
        
        
        
#         class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         word_count = {}
#         for c in s:
#             if c not in word_count:
#                 word_count[c] = 1
#             else:
#                 word_count[c] += 1

#         for c in t:
#             if (c not in word_count) or (word_count[c] == 0):
#                 return False
#             word_count[c] -= 1

#         return True