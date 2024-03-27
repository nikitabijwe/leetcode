class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        op=0
        # for i in range(len(operations)):
        #     if operations[i] == "X++" or operations[i] == "++X":
        #         op+=1
        #     else:
        #         op-=1
        # return op
    
    # OR
        
        for i in operations:
            if "+" in i:
                op+=1
            else:
                op-=1
        return op
                
                
        