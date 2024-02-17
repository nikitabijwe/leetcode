class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
            
        rotated_str_builder = []
        
        for c in reversed(num):
            if c not in rotated_digits:
                return False
            rotated_str_builder.append(rotated_digits[c])
            
        rotated_string = "".join(rotated_str_builder)
        return rotated_string == num