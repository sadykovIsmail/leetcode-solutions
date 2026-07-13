from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(left: int, right: int):
            # 1. BASE CASE: If pointers meet or cross, stop!
            if left >= right:
                return
            print(s)
            # 2. THE WORK: Swap the elements at the current pointers
            s[left], s[right] = s[right], s[left]
            print(s)
            # 3. RECURSIVE CALL: Move inward and repeat
            helper(left + 1, right - 1)
            
        # Kick off the recursion with the outermost indices
        helper(0, len(s) - 1)
        
        # LeetCode tests it in-place without a return, 
        # but returning 's' here just so your print statement works.
        return s 

exa = Solution()
print(exa.reverseString(["H","e", "l", 'l', 'o']))