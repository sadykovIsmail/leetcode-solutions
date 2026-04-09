"""
215. Kth Largest Element in an Array
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)
        while k > 0:
            item = heapq.heappop(heap) * -1
            k -= 1
        return item

exa = Solution()
print(exa.findKthLargest([3,2,1,5,6,4], 2))


# The best answer
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        
        for num in nums:
            # 1. Push the new person into the VIP club
            heapq.heappush(heap, num)
            
            # 2. If the club exceeds capacity 'k', kick out the smallest person
            if len(heap) > k:
                heapq.heappop(heap)
                
        # 3. The absolute smallest person left in the VIP club is our answer
        return heap[0]

# Your testing style
exa = Solution()
print(exa.findKthLargest([3, 2, 1, 5, 6, 4], 2)) # Output should be 5