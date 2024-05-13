class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)  # Length of the input string
        ans = 0  # Variable to store the length of the longest substring without repeating characters
        # Dictionary to store the index of the last occurrence of each character in the substring
        mp = {}

        i = 0  # Pointer to the start of the current substring
        # Iterate over each character in the string
        for j in range(n):
            # If the current character is already in the substring (indicating a repeat)
            if s[j] in mp:
                # Update the start pointer to the maximum of its current position and the index of the last occurrence of the current character
                i = max(mp[s[j]], i)

            # Update the length of the longest substring found so far
            ans = max(ans, j - i + 1)
            # Store the index of the current character in the dictionary, with the next index as the value
            mp[s[j]] = j + 1

        return ans  # Return the length of the longest substring without repeating characters
