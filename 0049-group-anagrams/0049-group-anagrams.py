class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
            
#         dict=collections.defaultdict(list)
        
#         for ele in strs:
#             dict[tuple(sorted(ele))].append(ele)
#         return dict.values()

        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()