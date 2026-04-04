"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300]
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ""
        item = ""
        sumItem = ""
        num = "1234567890"
        for i in range(len(s)):
            if s[i] == ']':
                while item != '[':
                    item = stack.pop()
                    if item != '[':
                        result = item + result
                # print(result, stack)

                sumItem = ""
                item = stack.pop()
                while item in num:
                    sumItem = item + sumItem
                    # print(sumItem)
                    if stack:
                        item = stack.pop()
                    else:
                        break
                if item not in num:
                    stack.append(item)

                # print(sumItem, stack)

                result = int(sumItem)*(str(result))
                # print(result)
                stack.append(result)
                # print(stack)
                item, result = "", ""
            else:
                stack.append(s[i])
        # print(stack)
        while stack:
            item = stack.pop() + item
        return item

# ex = Solution()
# print(ex.decodeString("100[leetcode]")) #"abcabccdcdcdef"

