class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {'(': ')', '{': '}', '[': ']'}
        
        for i in range(len(s)):
            print("i", s[i])
            if s[i] in open.keys():
                stack.append(s[i])
            else:
                print(stack)
                if stack:
                    item = stack.pop()
                    if open[item] != s[i]:
                        return False
                else:
                    return False
        if stack:
            return False
        else:

            return True
examp = Solution()
print(examp.isValid(")"))