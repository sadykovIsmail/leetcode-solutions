"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            return 0
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            return -1
        left, right = 0, len(nums) - 1
        while left != right:
            mid = left + (right - left) // 2
            print(left, right, mid)
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid] or nums[left] == target:
                if nums[mid - 1] < target and nums[left] > target and nums[left] != target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[right] >= target and nums[mid + 1] <= target:
                left = mid + 1
            else:
                return -1
        if nums[left] == target:
            return left
        return -1  
            

arr = [4,5,6,7,0,1,2]
exa = Solution()
# left, right = 0, len(arr) -1
# mid = left + (right - left) // 2
print(exa.search(arr, 0))



from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # We use <= so we don't miss the case where left == right
        while left <= right:
            mid = left + (right - left) // 2
            
            # Bingo! We found it.
            if nums[mid] == target:
                return mid
            
            # 1. Check if the Left side is the perfectly sorted half
            if nums[left] <= nums[mid]:
                # Is the target inside this safe, sorted left side?
                if nums[left] <= target < nums[mid]: 
                    right = mid - 1  # Yes, discard the right side.
                else:
                    left = mid + 1   # No, it must be in the right side.
            
            # 2. Otherwise, the Right side MUST be the sorted one
            else:
                # Is the target inside this safe, sorted right side?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Yes, discard the left side.
                else:
                    right = mid - 1  # No, it must be in the left side.
                    
        # If the loop finishes and we haven't returned mid, it's not here.
        return -1