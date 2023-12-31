class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
#         seen = set(sentence)
        
#         if len(seen)==26:
#             return True
#         return False



        # We iterate over 'sentence' for 26 times, one for each letter 'curr_char'.
        for i in range(26):
            curr_char = chr(ord('a') + i)

            # If 'sentence' doesn't contain 'curr_char', it is not a pangram.
            if sentence.find(curr_char) == -1:
                return False
        
        # If we manage to find all 26 letters, it is a pangram.
        return True