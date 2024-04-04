class Solution(object):
    def minMovesToMakePalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        output = 0
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                left, right = s[l], s[r]
                swap = None
                # Find string to match with left boundary
                for i in range(l + 1, r):
                    if s[i] == right:
                        swap = i
                        break
                # Find string to match with right boundary
                for j in range(r - 1, l, -1):
                    if s[j] == left and (not swap or swap - l > r - j):
                        swap = -j
                        break
                # If swapping with left boundary
                if swap >= 0:
                    s = s[0:l] + s[swap] + s[l:swap] + s[swap + 1:]
                    output += swap - l
                # Else swap with right boundary
                else:
                    swap = -swap
                    s = s[0:swap] + s[swap + 1:r + 1] + s[swap] + s[r + 1:]
                    output += r - (swap)
            l += 1
            r -= 1

        return output
