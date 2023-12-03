class Solution:
    def isValid(self, s: str) -> bool:
        dict = {")": "(", "}": "{", "]": "["}

        stack=[]
        
        for char in s:
            if char in dict:
                top_ele=stack.pop() if stack else '#'
                if dict[char]!=top_ele:
                    return False
            else:
                stack.append(char)
        return not stack