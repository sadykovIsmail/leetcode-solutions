"""
973. K Closest Points to Origin
Medium
Topics
premium lock icon
Companies
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

 

Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:

1 <= k <= points.length <= 104
-104 <= xi, yi <= 104
"""
from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        heap = []
        result = dict()
        for num in points:
            num1, num2 = num
            distance =  num1 ** 2 + num2 ** 2
            if len(heap) < k:
                heapq.heappush(heap, distance * -1)
                result[distance] = num
            else:
                if heap[0] * - 1 > distance:
                    heapq.heappush(heap, distance * -1)
                    result[distance] = num
                    item = heapq.heappop(heap) * -1
                    del result[item]
        return list(result.values())
exa = Solution()
print(exa.kClosest([[3,3],[5,-1],[-2,4]], 2))


# the actual answer

from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
            
        heap = []
        # We delete the result dictionary entirely!
        
        for num in points:
            num1, num2 = num
            distance = num1 ** 2 + num2 ** 2
            
            if len(heap) < k:
                # Push a TUPLE: (negative_distance, the_point)
                heapq.heappush(heap, (distance * -1, num))
            else:
                # heap[0][0] looks at the negative_distance of the top tuple
                if (heap[0][0] * -1) > distance:
                    heapq.heappush(heap, (distance * -1, num))
                    heapq.heappop(heap)
                    
        # When we are done, grab the points (index 1) out of the tuples left in the heap
        return [item[1] for item in heap]

exa = Solution()
print(exa.kClosest([[3,3],[5,-1],[-2,4]], 2))