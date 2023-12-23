class Solution(object):
    def checkAlmostEquivalent(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        alph_dict = dict()

        for i in range(len(word1)):
            alph_dict[word1[i]] = alph_dict.get(word1[i], 0) + 1
            alph_dict[word2[i]] = alph_dict.get(word2[i], 0) - 1

        for x in alph_dict.values():
            if x > 3 or x < -3:
                return False

        return True