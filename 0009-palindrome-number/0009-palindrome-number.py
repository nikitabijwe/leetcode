class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle negative numbers (they can't be palindromes)
        if x < 0:
            return False

        # Reverse the second half of the number
        reversed_half = 0
        original_x = x

        while x > 0:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # If the length of the original number is odd, we can ignore the middle digit
        # For example: 12321 -> original_x = 123, reversed_half = 321
        # If the length is even, both halves should be the same
        return original_x == reversed_half or original_x == reversed_half // 10
