"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 
Input: nums = [1, 2, 4, 4, 4, 4, 7, 9], target = 4

Output: [2, 5]

Input: nums = [10, 11, 12, 13, 14], target = 12

Output: [2, 2]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[left] == target:
                if nums[right] == target:
                    return [left, right]
                if nums[mid + 1] == target:
                    right = mid + 1
                right = mid
            elif nums[right] == target:
                if nums[mid - 1] == target:
                    left = mid - 1
                left = mid
            else:
                left += 1
                right -= 1

        if nums[left] == target and nums[right] == target:
            return [left, right]
        elif nums[left] == target and nums[right] != target:
            return [left, left]
        elif nums[right] == target and nums[left] != target:
            return [right, right]
        return [-1, -1]
        
exa = Solution()
print(exa.searchRange([1,2,3,3,3,3,4,5,9], 3))
