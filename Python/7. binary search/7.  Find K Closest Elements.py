"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3

Output: [1,2,3,4]

Example 2:

Input: arr = [1,1,2,3,4,5], k = 4, x = -1

Output: [1,1,2,3]

 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
"""
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        numL = round(k / 2)
        numR = k - numL
        while left + numL < right:
            mid = (left + right) / 2
            if arr[mid] == x:
                left = mid - numL
                right = mid + numR
                return arr[numL:numR+1]
            elif arr[mid] < x:
                left = mid
            elif arr[mid] > x:
                right = mid
            

"""
the actual answer

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Step 1: Binary Search (Template 3) to find the closest starting point
        left, right = 0, len(arr) - 1
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if arr[mid] < x:
                left = mid
            else:
                right = mid
                
        # After the loop, left and right point to the two elements closest to x.
        # Step 2: Two Pointers (Expanding Window)
        # We need to expand our bounds until we have exactly k elements.
        
        # We loop k - 1 times because we will ultimately select a range of k elements
        # Currently, if we just pick the closer of left or right, we have 1 element.
        # We need to expand our window until it encompasses k elements.
        
        # Let's set our initial window boundaries
        l, r = left, right 
        
        # Keep expanding until the window size is exactly k
        # The number of elements inside the window (exclusive of l and r) is (r - l - 1)
        while (r - l - 1) < k:
            # If we hit the left edge, we are forced to expand right
            if l < 0:
                r += 1
            # If we hit the right edge, we are forced to expand left
            elif r == len(arr):
                l -= 1
            # Otherwise, compare the distances and expand towards the closer one
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                l -= 1  # Left is closer (or equal and smaller), so stretch left
            else:
                r += 1  # Right is closer, so stretch right
                
        # The window boundaries are currently l and r. 
        # Because we expanded outward, the actual closest elements are strictly BETWEEN l and r.
        return arr[l + 1 : r]
"""
