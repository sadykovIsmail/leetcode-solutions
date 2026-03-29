from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = ['x'] * len(temperatures)
        for i, cur in enumerate(temperatures):
            print(i, cur)
            while stack:
                item, step = stack.pop()
                if item < cur:
                    output[step] = i - step
                    
                else:
                    stack.append((item, step))
                    stack.append((cur, i))
                    break
            else:
                stack.append((cur, i))
        while stack:
            item, step = stack.pop()
            output[step] = 0
        return output
    
example = Solution()
print(example.dailyTemperatures([73,74,75,71,69,72,76,73]))