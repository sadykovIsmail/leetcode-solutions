
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for item in tokens:
            if item in operators:
                int1 = int(stack.pop())
                int2 = int(stack.pop())
                #print("int1", int1)
                
                if item == '+':
                    sum = int1 + int2
                    stack.append(sum)
                    # print("second +", sum, started)
                elif item == '-':
                    sum = int2 - int1
                    stack.append(sum)
                elif item == '*':
                    sum = int2 * int1
                    stack.append(sum)
                elif item == '/':
                    sum = int(int2 / int1)
                    stack.append(sum)
                    #print("second /", sum, started)
            else:
                stack.append(item)
        sum = 0
        while stack:
            sum += int(stack.pop())
        return sum 
    
example = Solution()
print(example.evalRPN(["2","1","+","3","*"]))
                    