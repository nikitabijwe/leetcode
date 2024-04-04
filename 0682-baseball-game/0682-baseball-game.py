class Solution(object):
    def calPoints(self, ops):
        """
        :type operations: List[str]
        :rtype: int
        """
        # Initialize an empty stack to store valid points
        stack = []
        
        # Iterate through each operation
        for op in ops:
            if op == '+':  # If the operation is '+', add the sum of the last two valid points to the stack
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':  # If the operation is 'C', remove the last valid point from the stack
                stack.pop()
            elif op == 'D':  # If the operation is 'D', double the last valid point and add it to the stack
                stack.append(2 * stack[-1])
            else:  # If the operation is a number, convert it to an integer and add it to the stack
                stack.append(int(op))

        # Return the sum of all valid points in the stack
        return sum(stack)