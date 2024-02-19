class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return ans.values()
        
        
# For "eat":
# count: [1, 0, 0, ..., 1, 0, 0]
# This count tuple becomes a key, and "eat" is appended to the corresponding list.
# For "tea":

# count: [1, 0, 0, ..., 1, 0, 0] (same as "eat")
# Appended to the same list as "eat".
# For "tan":

# count: [1, 0, 1, ..., 0, 0, 0]
# A different count tuple, so a new key is created, and "tan" is appended.
# The same process continues for the remaining strings.