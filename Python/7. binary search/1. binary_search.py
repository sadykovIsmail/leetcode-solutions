"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return -1
    
# the actual one
def boundary_search(nums: list[int]) -> int:
    left = 0
    right = len(nums) - 1

    # Notice the strictly LESS THAN
    while left < right:
        # Notice the SAFE mid calculation
        mid = left + (right - left) // 2
        
        if condition_is_met(mid):
            # This might be the answer, but there could be a better one to the left.
            # Do NOT cross it out. Keep it in the search space.
            right = mid
        else:
            # This is definitely not the answer. Cross it out completely.
            left = mid + 1

    # Post-processing: left and right are now pointing to the exact same spot.
    # Check if that final spot actually meets your condition.
    if condition_is_met(left):
        return left
    
    return -1