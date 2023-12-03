class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        sum=0
        prev=0
        
        for char in reversed(s):
            curr_val = roman_dict[char]
            
            if curr_val < prev:
                sum-=curr_val
            else:
                sum+=curr_val
                
            prev=curr_val
            
        return sum
            
            