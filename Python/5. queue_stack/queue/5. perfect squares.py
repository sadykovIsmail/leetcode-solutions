"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
 

Constraints:

1 <= n <= 10^4
"""
from collections import deque
import math
class Solution:
    result = 0
    def numSquares(self, n: int) -> int:
        if n <= 3:
            self.result += n
            return self.result
        head = n
        queue = deque([(head, 1)])
        if head % 2 == 0:

            while queue:
                num, num2 = queue.popleft()
                print(num)
                for i in range(1, int(num)):
                    if num % i == 0:
                        new_item = num/2
                        if new_item ** 2 == num:
                            print("new_item", new_item)
                            self.result += num2
                            return self.result
                        else:
                            queue.append((num/i, i * num2))
            
        else:
            for i in range(head, 0, -1):
                print("i", i)
                
                print("new_number", i)
                if int(math.sqrt(i)) ** 2 == i:
                    item = head - i
                    print("item", item)
                    self.result += 1
                    self.numSquares(item)
                    break

        return self.result

                




example = Solution()
print(example.numSquares(6))

"""
The answer:
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        # 1. Precompute all perfect squares up to n to save time
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
            
        # 2. Setup the BFS queue and visited set
        queue = deque([(n, 0)])  # (current_remainder, steps_taken)
        visited = {n}
        
        # 3. Process the queue
        while queue:
            curr, steps = queue.popleft()
            
            # If we've hit exactly 0, we found our shortest path!
            if curr == 0:
                return steps
            
            # 4. Generate next moves (neighbors) by subtracting squares
            for square in squares:
                next_val = curr - square
                
                # If we go below 0, we've subtracted too much. 
                # Since 'squares' is sorted in ascending order, we can just break early.
                if next_val < 0:
                    break
                    
                # If it's a valid new number, add it to the queue
                if next_val not in visited:
                    visited.add(next_val)
                    queue.append((next_val, steps + 1))
                    
        return -1
"""